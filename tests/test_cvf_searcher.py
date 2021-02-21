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

    def test_out_of_range_year(self):
        cvpr_sercher = CvfSearcher(conference_name="CVPR")
        wacv_sercher = CvfSearcher(conference_name="WACV")
        iccv_sercher = CvfSearcher(conference_name="ICCV")
        out_of_range_year = ["1800"]
        _, cvpr_err = cvpr_sercher.find_paper_url_list(out_of_range_year)
        _, wacv_err = wacv_sercher.find_paper_url_list(out_of_range_year)
        _, iccv_err = iccv_sercher.find_paper_url_list(out_of_range_year)
        is_exist_cvpr_err = (not cvpr_err == None)
        is_exist_wacv_err = (not wacv_err == None)
        is_exist_iccv_err = (not iccv_err == None)
        if all([is_exist_cvpr_err, is_exist_wacv_err, is_exist_iccv_err]):
            self.assertTrue(
                f"is_exist_cvpr_err, is_exist_wacv_err, is_exist_iccv_err,{[is_exist_cvpr_err, is_exist_wacv_err, is_exist_iccv_err]}")
        else:
            self.assertFalse(
                f"allow out of range year. is_exist_cvpr_err, is_exist_wacv_err, is_exist_iccv_err,{[is_exist_cvpr_err, is_exist_wacv_err, is_exist_iccv_err]}")
