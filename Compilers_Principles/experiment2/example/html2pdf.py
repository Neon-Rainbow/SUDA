#! /usr/bin/env python
# coding=utf-8
from fpdf import FPDF, HTMLMixin


class MyFPDF(FPDF, HTMLMixin):
    pass


def html2pdf(html_text, path):
    pdf = MyFPDF()
    pdf.add_page()
    pdf.write_html(html_text)
    pdf.output(path, 'F')
