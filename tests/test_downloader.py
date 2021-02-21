#
# Created on Tue Feb 16 2021
#
# Copyright (c) 2021 Kazuki Hamaguchi
#

import unittest
from src.downloader import Downloader
import os

TEST_FILE_URL = "https://raw.githubusercontent.com/HamaguchiKazuki/download_paper/main/tests/example.com/content/papers/sample.txt"


class TestDownloadFile(unittest.TestCase):

    def test_download_file(self):
        test_url_path = TEST_FILE_URL
        test_dir = "tests/test_dir"
        d = Downloader()
        err = d.get_file(test_url_path, test_dir)
        if not err == None:
            self.assertFalse(err)
        test_file_path = os.path.join(
            test_dir, os.path.basename(test_url_path))
        with open(test_file_path, "r") as f:
            file_data = f.read()
        expected = 'sample.'
        self.assertEqual(file_data, expected)
