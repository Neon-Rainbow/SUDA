#! /usr/bin/env python
# coding=utf-8

import ply.lex as lex
import ply.yacc as yacc
from AST.Node import Node


def clear_text(text):
    """
    Strip lines and join them into a single string.

    Args:
        text: The text to be processed.

    Returns:
        A string.
    """
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    return ' '.join(lines)


# TOKENS
tokens = ('TITLE', 'AUTHOR', 'ABS', 'DOC', 'SECTION', 'SUBSECTION', 'ITEMIZE',
          'ITEM', 'TEXT', 'BEGIN', 'END', 'LB', 'RB')


# DEFINE OF TOKENS
def t_DOC(t):
    r"""document"""
    return t


def t_ABS(t):
    r"""abstract"""
    return t


t_TITLE = r'\\title'
t_SECTION = r'\\section'
t_SUBSECTION = r'\\subsection'
# t_TEXT = r'[a-zA-Z\s\.\,]+(?<!\\)'
t_TEXT = r'[a-zA-Z\s\.\,1-9\':]+'
t_BEGIN = r'\\begin'
t_END = r'\\end'
t_LB = r'\{'
t_RB = r'\}'
t_AUTHOR = r'\\author'
t_ITEMIZE = r'\\itemize'
t_ITEM = r'\\item'

# IGNORED
t_ignore = " \t"


def t_error(t):
    print(f"Illegal character : {t.value[0]}")
    t.lexer.skip(1)


# PARSE
def p_doc(t):
    r"""doc : BEGIN LB DOC RB content END LB DOC RB"""
    if len(t) == 10:
        t[0] = Node('[DOC]')
        t[0].add(t[5])


def p_content(t):
    r"""content : title abs sections
                | title author abs sections"""
    if len(t) == 4:
        t[0] = Node('[CONTENT]')
        t[0].add(t[1])
        t[0].add(t[2])
        # section_node = Node('[SECTIONS]')
        # section_node.add(t[3])
        # t[0].add(section_node)

        # t[0].add(t[3])

        section_node = Node('[SECTIONS]')
        for section in t[3]:
            section_node.add(section)
        t[0].add(section_node)
    elif len(t) == 5:
        t[0] = Node('[CONTENT]')
        t[0].add(t[1])
        t[0].add(t[2])
        t[0].add(t[3])
        # section_node = Node('[SECTIONS]')
        # section_node.add(t[4])
        # t[0].add(section_node)

        # t[0].add(t[4])

        section_node = Node('[SECTIONS]')
        for section in t[4]:
            section_node.add(section)
        t[0].add(section_node)


def p_title(t):
    r"""title : TITLE LB TEXT RB"""
    if len(t) == 5:
        t[0] = Node('[TITLE]')
        t[0].add(Node(t[3]))


def p_author(t):
    r"""author : AUTHOR LB TEXT RB"""
    if len(t) == 5:
        t[0] = Node('[AUTHOR]')
        t[0].add(Node(t[3]))


def p_abs(t):
    r"""abs : BEGIN LB ABS RB TEXT END LB ABS RB"""
    if len(t) == 10:
        t[0] = Node('[ABSTRACT]')
        t[0].add(Node(t[5]))


def p_sections(t):
    """sections : sections section
                | section"""
    # if len(t) == 3:
    #     t[0] = Node('[SECTIONS]')
    #     t[0].add(t[1])
    #     t[0].add(t[2])
    # if len(t) == 2:
    #     t[0] = Node('[SECTIONS]')
    #     t[0].add(t[1])
    if len(t) == 3:
        t[1].append(t[2])
        t[0] = t[1]
    elif len(t) == 2:
        t[0] = [t[1]]


# def p_section(t):
#     r"""section : SECTION LB TEXT RB TEXT """
#     if len(t) == 6:
#         t[0] = Node(f"[SECTION]({t[3]})")
#         t[0].add(Node(t[5]))

def p_section(t):
    r"""section : SECTION LB TEXT RB TEXT maybe_subsections
                | SECTION LB TEXT RB TEXT itemize TEXT maybe_subsections"""
    if len(t) == 7:
        t[0] = Node(f"[SECTION]({t[3]})")
        t[0].add(Node(t[5]))
        if t[6]:
            subsection_node = Node('[SUBSECTIONS]')
            for subsection in t[6]:
                subsection_node.add(subsection)
            t[0].add(subsection_node)
    elif len(t) == 8:
        t[0] = Node(f"[SECTION]({t[3]})")
        t[0].add(Node(t[5]))
        t[0].add(t[6])
        t[0].add(t[7])


def p_maybe_subsections(t):
    """maybe_subsections : maybe_subsections subsection
                         | subsection
                         | """
    # if len(t) == 3:
    #     t[0]: Node = Node('[SUBSECTIONS]')
    #     t[0].add(t[1])
    #     t[0].add(t[2])
    # if len(t) == 2:
    #     t[0] = Node('[SUBSECTIONS]')
    #     t[0].add(t[1])
    if len(t) == 3:
        t[1].append(t[2])
        t[0] = t[1]
    elif len(t) == 2:
        t[0] = [t[1]]
    elif len(t) == 1:
        t[0] = []


def p_subsection(t):
    r"""subsection : SUBSECTION LB TEXT RB TEXT"""
    if len(t) == 6:
        t[0]: Node = Node(f"[SUBSECTION]({t[3]})")
        t[0].add(t[5])


def p_itemize(t):
    r"""itemize : BEGIN LB ITEMIZE RB item_list END LB ITEMIZE RB"""
    t[0]: Node = Node('[ITEMIZE]')
    for item in t[5]:
        t[0].add(item)


def p_item_list(t):
    """item_list : item_list item
                 | item"""
    if len(t) == 3:
        t[1].append(t[2])
        t[0] = t[1]
    elif len(t) == 2:
        t[0] = [t[1]]


def p_item(t):
    r"""item : ITEM TEXT"""
    t[0]: Node = Node('[ITEM]')
    t[0].add(Node(t[2]))


def p_error(t):
    print(f"Syntax error at {t.value}")


def createNode(filename: str = "../data/example.tex") -> Node:
    """
    Main function to read the LaTeX file and parse its contents.

    Returns:
        A parse tree.
    """
    lex.lex()
    parser = yacc.yacc()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = clear_text(file.read())
        parse_tree = parser.parse(data)
        parse_tree.printNode(0)
        return parse_tree
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    createNode()
