import re


def f106():
    a = '<composer>Wolfgang Amadeus Mozart</composer>\n<author>Samuel Beckett</author>\n<city>London</city>'
    delate = re.compile('</.+>|<')
    a1 = re.sub(delate, '', a)
    delate2 = re.compile('>')
    a2 = re.sub(delate2, ':', a1)
    return a2


print(f106())