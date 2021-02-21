#
# Created on Sat Feb 20 2021
#
# Copyright (c) 2021 Kazuki Hamaguchi
#

import unittest
from src.searcher import CvfSearcher

class TestCvfSearcher(unittest.TestCase):

    def test_cvpr_searcher(self):
        cvpr_sercher = CvfSearcher(conference_name="CVPR")
        year_list = ["2013", "2014", "2015", "2016", "2017", "2018", "2019",  "2020"]
        paper_url_list, err = cvpr_sercher.find_paper_url_list(year_list)
        if not err == None:
            self.assertFalse(err)
        ## Make sure they are all pdf files.
        checked_paper_list = [paper for paper in paper_url_list if ".pdf" in paper]
        self.assertListEqual(checked_paper_list, paper_url_list)

    def test_wacv_searcher(self):
        wacv_sercher = CvfSearcher(conference_name="WACV")
        year_list = ["2020", "2021"]
        paper_url_list, err = wacv_sercher.find_paper_url_list(year_list)
        if not err == None:
            self.assertFalse(err)

        checked_paper_list = [paper for paper in paper_url_list if ".pdf" in paper]
        self.assertListEqual(checked_paper_list, paper_url_list)


    def test_iccv_searcher(self):
        iccv_sercher = CvfSearcher(conference_name="ICCV")
        year_list = ["2013", "2015", "2017", "2019"]
        paper_url_list, err = iccv_sercher.find_paper_url_list(year_list)
        if not err == None:
            self.assertFalse(err)

        checked_paper_list = [
            paper for paper in paper_url_list if ".pdf" in paper]
        self.assertListEqual(checked_paper_list, paper_url_list)
