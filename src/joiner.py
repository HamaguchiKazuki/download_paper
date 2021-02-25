#
# Created on Thu Feb 25 2021
#
# Copyright (c) 2021 Kazuki Hamaguchi
#

import glob
import os
import PyPDF2

class Joiner():
    def pdf_join(self, input_pdf_dir):
        err = None
        pdf_path_list = glob.glob(os.path.join(input_pdf_dir, "*.pdf"))

        merger = PyPDF2.PdfFileMerger()
        for pdf_path in pdf_path_list:
            try:
                merger.append(pdf_path)
            except Exception as err:
                return err

        merged_pdf = f"{input_pdf_dir}.pdf"
        try:
            merger.write(merged_pdf)
        except Exception as err:
            return err
        merger.close()
        return err
