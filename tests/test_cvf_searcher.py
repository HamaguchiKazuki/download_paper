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
        year_list = ["2013", "2018"]
        paper_url_list, err = cvpr_sercher.find_paper_url_list(year_list)
        if not err == None:
            self.assertFalse(err)

        # Make sure they are all pdf files.
        checked_paper_list = [
            paper for paper in paper_url_list if ".pdf" in paper]
        self.assertListEqual(checked_paper_list, paper_url_list)

        expected_list = ["https://openaccess.thecvf.com/content_cvpr_2013/papers/Kim_Deformable_Spatial_Pyramid_2013_CVPR_paper.pdf",
                         "https://openaccess.thecvf.com/content_cvpr_2018/papers/Das_Embodied_Question_Answering_CVPR_2018_paper.pdf"]
        for expected in expected_list:
            checked_a_paper = [
                paper for paper in paper_url_list if expected in paper]
            if checked_a_paper == []:
                self.assertFalse(f"no hit expected paper,{expected}")
            else:
                self.assertEqual(checked_a_paper[0], expected)

    def test_wacv_searcher(self):
        wacv_sercher = CvfSearcher(conference_name="WACV")
        year_list = ["2020", "2021"]
        paper_url_list, err = wacv_sercher.find_paper_url_list(year_list)
        if not err == None:
            self.assertFalse(err)

        checked_paper_list = [
            paper for paper in paper_url_list if ".pdf" in paper]
        self.assertListEqual(checked_paper_list, paper_url_list)

        expected_list = ["https://openaccess.thecvf.com/content_WACV_2020/papers/Nabavi_Unsupervised_Learning_of_Camera_Pose_with_Compositional_Re-estimation_WACV_2020_paper.pdf",
                         "https://openaccess.thecvf.com/content/WACV2021/papers/Fortin_Towards_Contextual_Learning_in_Few-Shot_Object_Classification_WACV_2021_paper.pdf"]
        for expected in expected_list:
            checked_a_paper = [
                paper for paper in paper_url_list if expected in paper]
            if checked_a_paper == []:
                self.assertFalse(f"no hit expected paper,{expected}")
            else:
                self.assertEqual(checked_a_paper[0], expected)

    def test_iccv_searcher(self):
        iccv_sercher = CvfSearcher(conference_name="ICCV")
        year_list = ["2013", "2019"]
        paper_url_list, err = iccv_sercher.find_paper_url_list(year_list)
        if not err == None:
            self.assertFalse(err)

        checked_paper_list = [
            paper for paper in paper_url_list if ".pdf" in paper]
        self.assertListEqual(checked_paper_list, paper_url_list)

        expected_list = ["https://openaccess.thecvf.com/content_iccv_2013/papers/Shankar_Semantic_Transform_Weakly_2013_ICCV_paper.pdf",
                         "https://openaccess.thecvf.com/content_ICCV_2019/papers/Yu_Free-Form_Image_Inpainting_With_Gated_Convolution_ICCV_2019_paper.pdf"]
        for expected in expected_list:
            checked_a_paper = [
                paper for paper in paper_url_list if expected in paper]
            if checked_a_paper == []:
                self.assertFalse(f"no hit expected paper,{expected}")
            else:
                self.assertEqual(checked_a_paper[0], expected)

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
