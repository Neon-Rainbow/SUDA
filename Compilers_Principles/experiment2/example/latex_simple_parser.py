#! /usr/bin/env python
# coding=utf-8
import re
from html2pdf import html2pdf


# parse by regex

def re_find(p, text):
    m = p.findall(text)
    if len(m) == 1:
        return m[0]
    else:
        return ''


def re_findall(p, text):
    return p.findall(text)


def clear_text(text):
    lines = []
    for line in text.split('\n'):
        line = line.strip()
        if len(line) > 0:
            lines.append(line)
    return ' '.join(lines)


# 1. read tex file
content = open('example.tex', 'r').read()

# 2. extract document part
p_doc = re.compile(r'\\begin{document}(.+?)\\end{document}', re.S)
document = re_find(p_doc, content)

# 3. extract head
p_title = re.compile(r'\\title{(.+?)}', re.S)
title = re_find(p_title, document)

# 4. extract abstract
p_abs = re.compile(r'\\begin{abstract}(.+?)\\end{abstract}', re.S)
abstract = re_find(p_abs, document)
abstract = clear_text(abstract)

# 5. sections
p_sec = re.compile(r'\\section{(.+?)}(.+?)\\section', re.S)  # only for Section 1
section_title, section_content = re_find(p_sec, document)
section_content = clear_text(section_content)

# 6.subsection
p_subsec = r'\\subsection{(.+?)}'
subsec_title = re.findall(p_subsec, document)

subsec_content = []
for item in subsec_title:
    pat = r'\\subsection{%s}(.+?)\\subsubsection' % item
    p_subsec_content = re.compile(pat, re.S)
    lst = p_subsec_content.findall(document)
    if not lst:
        pat = r'\\subsection{' + item + r'}(.+?)\%A'
        p_subsec_content = re.compile(pat, re.S)
        lst = p_subsec_content.findall(document)
    subsec_content.append(lst[0])

# 7.Extract itemize
p_itemize = re.compile(r'\\begin{itemize}(.+?)\\end{itemize}', re.S)
itemize = re.findall(p_itemize, document)

# 8.Extract item
p_item = re.compile(r'\\item(.+?)\n', re.S)

# 9.Extract tabular
p_tabu = re.compile(r'\\begin{tabular}{\\| l \\| l \|}(.+?)\\end{tabular}', re.S)
tabular = re.findall(p_tabu, document)[0]
p_tabu_content = re.compile(r'\\texttt{\\textbackslash (.+)\\{\\emph{(.+)}\\}} & (.+) \\', re.S)
tmp = re.findall(p_tabu_content, tabular)
tmp = tmp[0][0].split('\\texttt{\\textbackslash')
col1 = []  # the first col of table
col2 = []  # the second col of table
for token in tmp:
    lst = token.split('\\')
    col1.append('\\%s{%s}' % (lst[0].strip(), lst[0].strip()))
    if len(lst) > 1:
        col2.append(lst[3].split()[-1])
    else:
        col2.append(len(tmp) - 2)

# 10.Extract textbf label
re_tbf = re.compile(r'\\textbf{(.+?)}', re.S)
tbf = re.findall(re_tbf, document)
for item in tbf:
    if '\n' in item:
        tbf.remove(item)

# 11.Extract emph label
re_emph = re.compile(r'\\emph{(.+?)}', re.S)
emph = re.findall(re_emph, document)
for item in emph:
    if '\n' in item:
        emph.remove(item)

# 12. generate html text
html_text = ''
# title
html_text += '<h1>%s</h1>\n\n' % title
# abstract
html_text += '<p>%s</p>\n\n' % abstract
# section -- 1
html_text += '<h2>%s</h2>\n\n' % section_title
html_text += '<p>%s</p>\n\n' % section_content

# 13.Write subsections
for i in range(len(subsec_title)):
    html_text += '<h3>%s</h3>\n\n' % subsec_title[i]
    html_text += '<p>%s</p>\n\n' % subsec_content[i]
# 14.Write content of itemize label
html_text += '<ul>'
for i in range(len(itemize)):
    tmp = re.findall(p_item, itemize[i])
    for j in range(len(tmp)):
        # Remove or replace nested <em> tags here
        tmp[j] = tmp[j].replace('<em>', '').replace('</em>', '')  # Replace with '' to remove, or with supported tag
        html_text += '<li>%s</li>\n' % tmp[j]
html_text += '</ul>\n\n'
# 15.Write content of tabular label
html_text += '<table border="1">\n'
html_text += "<tr>\n"
html_text += "<th width='40%'>Command</th>\n"
html_text += "<th width='40%'>Level</th>\n"
html_text += "</tr>\n"
for i in range(len(col1)):
    html_text += "<tr>\n"
    html_text += "<td>%s</td>\n" % col1[i]
    html_text += "<td>%s</td>\n" % col2[i]
    html_text += "</tr>\n"
html_text += '</table>\n\n'
# 16.Write textbf label
for item in tbf:
    html_text += '<strong>%s</strong>\n\n' % item
# 17.Write emph label
for item in emph:
    html_text += '<em>%s</em>\n\n' % item

html2pdf(html_text, '2.pdf')
