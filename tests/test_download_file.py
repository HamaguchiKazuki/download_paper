#
# Created on Tue Feb 16 2021
#
# Copyright (c) 2021 Kazuki Hamaguchi
#

import unittest
from src.download_file import download_file
import os


class TestDownloadFile(unittest.TestCase):

    def test_download_file(self):
        test_url_path = "https://raw.githubusercontent.com/HamaguchiKazuki/download_paper/feature/download_file/tests/example.com/content/papers/sample.txt"
        test_dir = "tests/test_dir"
        download_file(test_url_path, test_dir)
        test_file_path = os.path.join(
            test_dir, os.path.basename(test_url_path))
        with open(test_file_path, "r") as f:
            file_data = f.read()
        expected = 'sample.'
        self.assertTrue(file_data, expected)
