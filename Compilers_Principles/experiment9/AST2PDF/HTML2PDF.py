from fpdf import FPDF, HTMLMixin
from .AST2HTML import Latex2Html
import sys
import os


class MyFPDF(FPDF, HTMLMixin):
    pass


def Html2PDF(html: str, output_filename: str) -> None:
    """
    将html格式的字符串转换为pdf格式的文件,并将其保存到{output_filename}中
    Args:
        html: html格式的字符串
        output_filename: 输出的pdf文件的路径

    Returns:
        None
    """
    pdf = MyFPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.write_html(html)
    pdf.output(output_filename)


def Converter(tex_filename: str, pdf_output_filename: str, html_output_filename: str = "") -> None:
    """
    将tex文件转换为pdf文件
    Args:
        tex_filename: tex文件的路径
        pdf_output_filename: 输出的pdf文件的路径
        html_output_filename: 输出的html文件的路径

    Returns:
        None
    """
    html_str = Latex2Html(tex_filename, html_output_filename=html_output_filename)
    Html2PDF(html_str, pdf_output_filename)


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    project_root = os.path.join(script_dir, '..')
    sys.path.insert(0, os.path.abspath(project_root))
    Converter("../data/example2.tex", "../output/example2.pdf")
