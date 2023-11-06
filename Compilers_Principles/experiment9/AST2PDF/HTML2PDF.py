from fpdf import FPDF, HTMLMixin
from AST2HTML import Latex2Html


class MyFPDF(FPDF, HTMLMixin):
    pass


def Html2PDF(html: str, output_filename):
    pdf = MyFPDF()
    # Add a page
    pdf.add_page()
    # Set font
    pdf.set_font("Arial", size=12)
    # Add a cell
    pdf.write_html(html)
    # Save the pdf with name .pdf
    pdf.output(output_filename)


if __name__ == "__main__":
    html_str = Latex2Html("../data/example2.tex", isPrint=True)
    Html2PDF(html_str, "../output/example2.pdf")
