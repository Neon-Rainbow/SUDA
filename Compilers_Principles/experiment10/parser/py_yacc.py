#! /usr/bin/env python
# coding=utf-8
import ply.yacc as yacc
from nodes.node import Node, num_node
from lexer.py_lex import *


# YACC for parsing Python

def simple_node(t, name):
    t[0] = Node(name)
    for i in range(1, len(t)):
        t[0].add(Node(t[i]))
    return t[0]


def p_program(t):
    """program : statements"""
    if len(t) == 2:
        t[0] = Node('[PROGRAM]')
        t[0].add(t[1])


def p_statements(t):
    """statements : statements statement
                  | statement"""
    # 我就没见过有人AST是这样画的,这个真的是编译原理老师写的代码吗
    if len(t) == 3:
        t[0] = Node('[STATEMENTS]')
        t[0].add(t[1])
        t[0].add(t[2])
    elif len(t) == 2:
        t[0] = Node('[STATEMENTS]')
        t[0].add(t[1])


def p_statement(t):
    """ statement : assignment
                  | operation
                  | print"""
    if len(t) == 2:
        t[0] = Node(['STATEMENT'])
        t[0].add(t[1])


def p_assignment(t):
    """assignment : VARIABLE '=' NUMBER"""
    if len(t) == 4:
        t[0] = Node('[ASSIGNMENT]')
        t[0].add(Node(t[1]))
        t[0].add(Node(t[2]))
        t[0].add(num_node(t[3]))


def p_operation(t):
    """operation : VARIABLE '=' VARIABLE '+' VARIABLE
                 | VARIABLE '=' VARIABLE '-' VARIABLE
                 | VARIABLE '=' VARIABLE '*' VARIABLE
                 | VARIABLE '=' VARIABLE '/' VARIABLE
                 | VARIABLE '=' VARIABLE "-" NUMBER "+" VARIABLE
    """
    if len(t) == 6:
        t[0] = simple_node(t, '[OPERATION]')
    else:
        t[0] = simple_node(t, "[OPERATION]")

def p_print(t):
    """
    print   : PRINT '(' VARIABLE ')'
            | PRINT "(" VARIABLE "," VARIABLE "," VARIABLE ")"
    """

    if len(t) == 5:
        t[0] = Node("[PRINT]")
        t[0].add(Node(t[3]))
    else:
        t[0] = Node("[PRINT]")
        t[0].add(Node(t[3]))
        t[0].add(Node(t[5]))
        t[0].add(Node(t[7]))


def p_error(t):
    print(f"Syntax error at {t.value}")


yacc.yacc()
