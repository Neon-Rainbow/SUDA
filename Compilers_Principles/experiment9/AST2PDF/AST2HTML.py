from AST import Node
import LatexParser.LatexParser as LatexParser


def node_to_html(node: Node):
    """
    Convert a Node instance into an HTML string.

    Args:
        node (Node): The Node instance to convert.

    Returns:
        str: The HTML representation of the Node.
    """
    # if node.getData() == '[DOC]':
    #     return "<!DOCTYPE html>\n<html>\n" + "\n".join(
    #         node_to_html(child) for child in node.getChildren()) + "\n</html>"
    # elif node.getData() == '[CONTENT]':
    #     return "<body>\n" + "\n".join(node_to_html(child) for child in node.getChildren()) + "\n</body>"
    # elif node.getData() == '[TITLE]':
    #     return "<h1>" + "".join(node_to_html(child) for child in node.getChildren()) + "</h1>"
    # elif node.getData() == '[AUTHOR]':
    #     return "<h2>Author: " + "".join(node_to_html(child) for child in node.getChildren()) + "</h2>"
    # elif node.getData() == '[ABSTRACT]':
    #     return "<abstract>\n" + "<p>" + "".join(
    #         node_to_html(child) for child in node.getChildren()) + "</p>\n</abstract>"
    # elif node.getData().startswith('[SECTION]'):
    #     section_title = node.getData()[9:-1]  # Extract the title from the [SECTION](Title) string
    #     return "<section>\n<h2>" + section_title + "</h2>\n" + "\n".join(
    #         node_to_html(child) for child in node.getChildren()) + "\n</section>"
    # elif node.getData().startswith('[SUBSECTION]'):
    #     subsection_title = node.getData()[13:-1]  # Extract the title from the [SUBSECTION](Title) string
    #     return "<subsection>\n<h3>" + subsection_title + "</h3>\n" + "\n".join(
    #         node_to_html(child) for child in node.getChildren()) + "\n</subsection>"
    # elif node.getData() == '[ITEMIZE]':
    #     return "<ul>\n" + "\n".join(node_to_html(child) for child in node.getChildren()) + "\n</ul>"
    # elif node.getData() == '[ITEM]':
    #     return "<li>" + "".join(node_to_html(child) for child in node.getChildren()) + "</li>"
    # elif node.getData().startswith('[TEXT]'):
    #     # This case is not in the original implementation, but assuming we might have such nodes.
    #     return node.getData()[6:]
    # else:
    #     # For plain text nodes, we just return the text.
    #     return node.getData()
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
            section_title_list: list[str] = []
            section_content_list: list[str] = []
            for section in sections:
                section_title: str = section.getData()[10:-1]
                section_content: str = section.getChildren()[0].getData()
                section_title_list.append(section_title)
                section_content_list.append(section_content)
            for j in zip(section_title_list, section_content_list):
                html += f"""
    <div class="section">
        <h2>{j[0]}</h2>
        <p>
            {j[1]}
        </p>
    </div>\n"""


    html += "</body>\n</html>"


    return html


if __name__ == '__main__':
    # Parse the LaTeX file
    latex_parser: Node = LatexParser.createNode("../data/example3.tex")
    # Convert the AST to HTML
    html = node_to_html(latex_parser)

    # Write the HTML to a file
    with open("../output/test.html", "w") as f:
        f.write(html)
