#
# Created on Thu Feb 25 2021
#
# Copyright (c) 2021 Kazuki Hamaguchi
#


import unittest
from src.joiner import Joiner
import PyPDF2
import os

TEST_PDF_DIR = "tests/test_join_pdf/conference"


class TestJoiner(unittest.TestCase):

    def test_pdf_join(self):
        test_pdf_dir = TEST_PDF_DIR
        j = Joiner()
        err = j.pdf_join(test_pdf_dir)
        if not err == None:
            self.assertFalse(err)

        test_predict_pdf_path = f"{TEST_PDF_DIR}.pdf"
        test_correct_pdf_path = "tests/test_join_pdf/correct_merged.pdf"
        predict_pdf = PyPDF2.PdfFileReader(test_predict_pdf_path)
        correct_pdf = PyPDF2.PdfFileReader(test_correct_pdf_path)

        self.assertEqual(predict_pdf.getNumPages(), correct_pdf.getNumPages())
