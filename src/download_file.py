#
# Created on Mon Feb 15 2021
#
# Copyright (c) 2021 Kazuki Hamaguchi
#

import os

import requests
from requests.models import ITER_CHUNK_SIZE


def download_file(url_path, save_dir, iter_chunk_size=ITER_CHUNK_SIZE):
    """download a file.

    Args:
        url_path (str): [description]
        save_dir (str): [description]
        iter_chunk_size (int, optional): [description]. Defaults to ITER_CHUNK_SIZE.
    """
    os.makedirs(save_dir, exist_ok=True)
    res = requests.get(url_path)
    try:
        res.raise_for_status()
    except Exception as err:
        print(err)
    pdf_name = os.path.basename(url_path)
    pdf_save_path = os.path.join(save_dir, pdf_name)
    with open(pdf_save_path, "wb") as pdf_data:
        for chunk_pdf_data in res.iter_content(iter_chunk_size):
            pdf_data.write(chunk_pdf_data)
