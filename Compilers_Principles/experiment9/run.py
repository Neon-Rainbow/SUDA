from AST2PDF.HTML2PDF import Converter
import sys

if __name__ == "__main__":
    tex_filename = ""
    pdf_output_filename = ""
    html_output_filename = ""
    arguments = sys.argv[1:]
    if len(arguments) > 0:
        tex_filename = arguments[0]
        pdf_output_filename = arguments[1]
        if len(arguments) > 2:
            html_output_filename = arguments[2]
        Converter(tex_filename, pdf_output_filename,html_output_filename)
    else:
        if tex_filename and pdf_output_filename:
            Converter(tex_filename, pdf_output_filename,html_output_filename)
        else:
            print(
                f"""
            命令行参数不足.应该输入两个参数,分别是tex文件的路径和pdf文件的输出路径.
            你输入了{len(arguments)}个参数,分别是
            tex_filename:{tex_filename} 
            pdf_output_filename{pdf_output_filename} 
            html_output_filename{html_output_filename}
            应该输入形如 python3 run.py tex文件路径 pdf文件输出路径 html文件输出路径(可选)
            例如:       python3 run.py data/example2.tex output/example2.pdf output/example2.html
            若不想使用命令行参数,请直接修改run.py中的main函数中的
            tex_filename = ""
            pdf_output_filename = ""
            (可选)html_output_filename = ""
            的内容
            """)
