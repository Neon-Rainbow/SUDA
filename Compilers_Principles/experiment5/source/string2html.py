"""
This file is used to convert python code to HTML to achieve code highlighting
"""

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter


def string2html(code: str) -> str:
    """
    convert python code to HTML to achieve code highlighting

    Args:
        code:python code which needs to be highlighted

    Returns:
        html:HTML-formatted string with code highlighting
    """
    formatter = HtmlFormatter(style="xcode")
    result = highlight(code, PythonLexer(), formatter)
    css = formatter.get_style_defs('.highlight')
    html = f"""
    <html>
    <head>
    <style>
    {css}
    </style>
    </head>
    <body>
    {result}
    </body>
    </html>
    """
    return html
