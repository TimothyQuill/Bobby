"""
The purpose of this file is to read in a PDF report,
perform general cleaning and formatting, then output it.
"""

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io


def pdf2txt(pdf_path):
    in_file = open(pdf_path, 'rb')
    res_mgr = PDFResourceManager()
    ret_data = io.StringIO()
    TxtConverter = TextConverter(res_mgr, ret_data, laparams=LAParams())
    interpreter = PDFPageInterpreter(res_mgr, TxtConverter)

    for page in PDFPage.get_pages(in_file):
        interpreter.process_page(page)

    return ret_data.getvalue()


pdf_path = '/Users/tim/Downloads/report_examples/cctv_report_1.pdf'
txt = pdf2txt(pdf_path)
print(txt)