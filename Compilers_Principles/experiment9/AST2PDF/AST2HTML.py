"""
将Latex文档转换为HTML格式的字符串,同时根据参数决定是否将HTML输出到../output/{tex_file_name}.html中
"""

import re

from AST import Node
import LatexParser.LatexParser as LatexParser


def Node2Html(node: Node) -> str:
    """
    将Node对象转换为HTML格式的字符串。

    Args:
        node: Node对象。用来表示Latex文档的AST

    Returns:
        HTML格式的字符串。
    """
    html: str = ""
    doc_node: Node = node
    html += "<!DOCTYPE html>\n<html>\n<body>\n"
    content_node: Node = node.getChildren()[0]
    for i in content_node.getChildren():
        if i.getData() == '[TITLE]':
            html += f"""<div class="title">{i.getChildren()[0].getData()}</div>\n"""
        elif i.getData() == '[AUTHOR]':
            html += f"""<div class="author">{i.getChildren()[0].getData()}</div>\n"""
        elif i.getData() == '[ABSTRACT]':
            html += f"""
    <div class="abstract">
        <h2>Abstract</h2>
        <p>
            {i.getChildren()[0].getData()}
        </p>
    </div>\n"""
        elif i.getData().startswith('[SECTIONS]'):
            sections: list[Node] = i.getChildren()
            section_title: str = ""
            section_content: str = ""
            for section in sections:
                if section.getData().startswith('[SECTION]'):
                    section_title: str = section.getData()[10:-1]
                else:
                    section_title: str = section.getData()[13:-1]
                for j in section.getChildren():
                    item_list = ""
                    if j.getData() != '[ITEMIZE]':
                        section_content = f"""
        {section_content}
        <p>
            {section.getChildren()[0].getData()}
        </p>
        """
                    else:
                        for k in j.getChildren():
                            item_list = f"""
                            {item_list}
                            <li>{k.getChildren()[0].getData()}</li>"""
                        section_content = f"""
        {section_content}
        <ul>
            {item_list}
        </ul>
        """
                html += f"""
    <div class="section">
        <h2>{section_title}</h2>
            {section_content}
    </div>  
    """
                section_title = ""
                section_content = ""

    html += "</body>\n</html>"

    return html


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


def Latex2Html(tex_file_name: str, isPrint: bool = False) -> str:
    """
    读取{tex_file_name}中的Latex内容,将其转换为其对应的HTML格式,同时根据参数来决定是否将HTML
    输出到../output/{tex_file_name}.html中

    Args:
        tex_file_name: Latex文件的路径
        isPrint: 决定是否将html格式的字符串输出到../output/{tex_file_name}.html中

    Returns:
        HTML格式的字符串,可能会将字符串输出到../output/{tex_file_name}.html中
    """
    latex_parser: Node = LatexParser.createNode(tex_file_name)
    html = Node2Html(latex_parser)
    pattern = r'/([^/]*?)\.tex'
    file_name = re.findall(pattern, tex_file_name)[0]
    if isPrint:
        with open(f"../output/{file_name}.html", "w") as f:
            f.write(html)
    return html


if __name__ == '__main__':
    Latex2Html("../data/example2.tex", isPrint=True)
