#
# Created on Sat Feb 20 2021
#
# Copyright (c) 2021 Kazuki Hamaguchi
#
import os
import random
import time
import logging

import requests
from bs4 import BeautifulSoup


class Searcher():

    def __init__(self, conference_name):
        self.https = "https://"
        self.top_path = None
        self.conference_name = conference_name

    def find_paper_url_list(self, year_list=[]):
        raise NotImplementedError()


class CvfSearcher(Searcher):

    def __init__(self, conference_name="CVPR"):
        """ crawler papers of CVF conference

        Args:
            conference_name (str, optional): Select CVPR, WACV, ICCV. Defaults to "CVPR".
        """
        self.https = "https://"
        self.top_path = "openaccess.thecvf.com"
        self.conference_name = conference_name

    def find_paper_url_list(self, year_list=["2020"]):
        err = None
        paper_url_list = []
        for year in year_list:
            conference_year = self.conference_name + year
            res_html_days_or_papers = requests.get(
                os.path.join(self.https, self.top_path, conference_year))
            time.sleep(1.0 + random.uniform(0, 1))
            try:
                res_html_days_or_papers.raise_for_status()
            except Exception as err:
                return [], err

            parsed_html_days_or_papers = BeautifulSoup(
                res_html_days_or_papers.text, "html.parser")
            html_days_or_papers = parsed_html_days_or_papers.select('dd a')

            for html_day_or_paper in html_days_or_papers:
                day_or_paper = html_day_or_paper.get("href")
                is_href_empty = (day_or_paper == None)
                if is_href_empty:
                    continue

                is_day = "?day" in day_or_paper
                if is_day:
                    day = day_or_paper
                    day_query_index = day.find("?")
                    conference_day = conference_year + day[day_query_index:]
                    res_html_papers = requests.get(os.path.join(
                        self.https, self.top_path, conference_year, conference_day))
                    time.sleep(1.0 + random.uniform(0, 1))
                    try:
                        res_html_papers.raise_for_status()
                    except Exception as err:
                        return [], err

                    parsed_html_papers = BeautifulSoup(
                        res_html_papers.text, "html.parser")
                    html_papers = parsed_html_papers.select('dd a')
                    for html_paper in html_papers:
                        paper = html_paper.get('href')
                        is_href_empty = (paper == None)
                        if is_href_empty:
                            continue
                        if ".pdf" in paper:
                            is_there_slash_top_level = (paper.find("/") == 0)
                            if is_there_slash_top_level:
                                paper = paper[1:]
                            paper_url = os.path.join(
                                self.https, self.top_path, paper)
                            paper_url_list.append(paper_url)
                else:
                    paper = day_or_paper
                    is_href_empty = (paper == None)
                    if is_href_empty:
                        continue
                    if ".pdf" in paper:
                        is_there_slash_top_level = (paper.find("/") == 0)
                        if is_there_slash_top_level:
                            paper = paper[1:]
                        paper_url = os.path.join(
                            self.https, self.top_path, paper)
                        paper_url_list.append(paper_url)

        return paper_url_list, err
