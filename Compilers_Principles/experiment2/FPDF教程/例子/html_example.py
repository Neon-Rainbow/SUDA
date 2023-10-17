#! /usr/bin/env python
#coding=utf-8
from fpdf import FPDF, HTMLMixin

html = """
<H1 align="center">html2fpdf</H1>
<h2>Basic usage</h2>
<p>You can now easily print text while mixing different
styles : <B>bold</B>, <I>italic</I>, <U>underlined</U>, or
<B><I><U>all at once</U></I></B>!
 
<BR>You can also insert hyperlinks
like this <A HREF="http://www.mousevspython.com">www.mousevspython.comg</A>,
or include a hyperlink in an image. Just click on the one below.<br>
<center>
<A HREF="http://www.mousevspython.com"></A>
</center>
 
<h3>Sample List</h3>
<ul><li>option 1</li>
<ol><li>option 2</li></ol>
<li>option 3</li></ul>
 
<table border="0" align="center" width="50%">
<thead><tr><th width="30%">Header 1</th><th width="70%">header 2</th></tr></thead>
<tbody>
<tr><td>cell 1</td><td>cell 2</td></tr>
<tr><td>cell 2</td><td>cell 3</td></tr>
</tbody>
</table>
"""
 

 
class MyFPDF(FPDF, HTMLMixin):
    pass
 
pdf=MyFPDF()
#First page
pdf.add_page()
pdf.write_html(html)
pdf.output('html.pdf','F')
