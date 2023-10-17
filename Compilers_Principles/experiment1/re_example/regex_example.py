#! /usr/bin/env python
#coding=utf-8
import re

p=re.compile(r'<a title="" href="(https://www.sohu.com/a/.+?)" target="_blank">(.+?)</a>')

# read html file
html_content=open('list.html','rb').read()
#print html_content

# regex match
matches=p.findall(html_content)
print len(matches)

for m in matches:
    print m[0],m[1]


