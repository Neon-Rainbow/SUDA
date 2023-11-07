"""
将Latex文档转换为HTML格式的字符串,同时根据参数决定是否将HTML输出到../output/{tex_file_name}.html中
"""

import re

from AST.Node import Node
import LatexParser.LatexParser as LatexParser


def Node2Html(node: Node) -> str:
    """
    将Node对象转换为HTML格式的字符串。

    Args:
        node: Node对象。用来表示Latex文档的AST

    Returns:
        HTML格式的字符串。
    """
    html_output: str = ""
    doc_node: Node = node
    html_output += "<!DOCTYPE html>\n<html>\n<body>\n"
    root_content_node: Node = node.getChildren()[0]
    for section_node in root_content_node.getChildren():
        if section_node.getData() == '[TITLE]':
            html_output += f"""<div class="title">{section_node.getChildren()[0].getData()}</div>\n"""
        elif section_node.getData() == '[AUTHOR]':
            html_output += f"""<div class="author">{section_node.getChildren()[0].getData()}</div>\n"""
        elif section_node.getData() == '[ABSTRACT]':
            html_output += f"""
    <div class="abstract">
        <h2>Abstract</h2>
        <p>
            {section_node.getChildren()[0].getData()}
        </p>
    </div>\n"""
        elif section_node.getData().startswith('[SECTIONS]'):
            sections: list[Node] = section_node.getChildren()
            current_section_title: str = ""
            current_section_content: str = ""
            isSection: bool = False
            for section in sections:
                if section.getData().startswith('[SECTION]'):
                    isSection = True
                    current_section_title: str = section.getData()[10:-1]
                else:
                    current_section_title: str = section.getData()[13:-1]
                for content_item in section.getChildren():
                    items_html = ""
                    if content_item.getData() != '[ITEMIZE]':
                        current_section_content = f"""
        {current_section_content}
        <p>
            {section.getChildren()[0].getData()}
        </p>
        """
                    else:
                        for list_item in content_item.getChildren():
                            items_html = f"""
                            {items_html}
                            <li>{list_item.getChildren()[0].getData()}</li>"""
                        current_section_content = f"""
        {current_section_content}
        <ul>{items_html}</ul>
        """
                if isSection:
                    isSection = False
                    html_output += f"""
    <div class="section">
        <h2>{current_section_title}</h2>
            {current_section_content}
    </div>  
    """
                else:
                    html_output += f"""
    <div class="subsection">
        <h3>{current_section_title}</h3>
            {current_section_content}
    </div>
    """
                current_section_title = ""
                current_section_content = ""

    html_output += "</body>\n</html>"

    return html_output


def Latex2Node(tex_file: str) -> Node:
    """
    读取{tex_file}中的Latex内容,将其转换为其对应的Node对象
    Args:
        tex_file: Latex文件的路径

    Returns:
        Node对象,用来表示Latex文档的AST
    """
    latex_parser: Node = LatexParser.createNode(tex_file)
    return Node2Html(latex_parser)


def Latex2Html(tex_file_name: str, html_output_filename: str = "") -> str:
    """
    读取{tex_file_name}中的Latex内容,将其转换为其对应的HTML格式,同时根据参数来决定是否将HTML
    输出到../output/{tex_file_name}.html中

    Args:
        tex_file_name: Latex文件的路径
        html_output_filename: html文件的输出路径.不输入该参数时不输出html文件

    Returns:
        HTML格式的字符串,可能会将字符串输出到{html_output_filename}中
    """
    latex_parser: Node = LatexParser.createNode(tex_file_name)
    html = Node2Html(latex_parser)
    pattern = r'/([^/]*?)\.tex'
    file_name = re.findall(pattern, tex_file_name)[0]
    if html_output_filename:
        with open(f"{html_output_filename}", "w") as f:
            f.write(html)
    return html


if __name__ == '__main__':
    Latex2Html("../data/example2.tex")
