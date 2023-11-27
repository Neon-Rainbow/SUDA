#! /usr/bin/env python
# coding=utf-8

v_table = {}  # variable table


def update_v_table(name, value):
    v_table[name] = value


def trans(node):
    # Translation

    # Assignment
    if node.getdata() == '[ASSIGNMENT]':
        ''' statement : VARIABLE '=' NUMBER'''
        value = node.getchild(2).getvalue()
        node.getchild(0).setvalue(value)
        # update v_table
        update_v_table(node.getchild(0).getdata(), value)




    # Operation
    elif node.getdata() == '[OPERATION]':
        '''operation : VARIABLE '=' VARIABLE '+' VARIABLE
                     | VARIABLE '=' VARIABLE '-' VARIABLE'''
        arg0 = v_table[node.getchild(2).getdata()]
        arg1 = v_table[node.getchild(4).getdata()]
        op = node.getchild(3).getdata()

        if op == '+':
            value = arg0 + arg1
        else:
            value = arg0 - arg1

        node.getchild(0).setvalue(value)
        # update v_table
        update_v_table(node.getchild(0).getdata(), value)



    # Print
    elif node.getdata() == '[PRINT]':
        '''print : PRINT '(' VARIABLE ')' '''
        arg0 = v_table[node.getchild(2).getdata()]
        print(arg0)

    # If
    elif node.getdata() == '[IF]':
        r'''if : IF '(' condition ')' '{' statements '}' '''
        children = node.getchildren()
        trans(children[0])
        condition = children[0].getvalue()
        if condition:
            for c in children[1:]:
                trans(c)

    # While
    elif node.getdata() == '[WHILE]':
        r'''while : WHILE '(' condition ')' '{' statements '}' '''
        children = node.getchildren()
        while trans(children[0]):
            for c in children[1:]:
                trans(c)


    # Condition
    elif node.getdata() == '[CONDITION]':
        '''condition : VARIABLE '>' VARIABLE
                     | VARIABLE '<' VARIABLE'''

        arg0 = v_table[node.getchild(0).getdata()]
        arg1 = v_table[node.getchild(2).getdata()]
        op = node.getchild(1).getdata()
        if op == '>':
            node.setvalue(arg0 > arg1)
        elif op == '<':
            node.setvalue(arg0 < arg1)

    else:
        for c in node.getchildren():
            trans(c)

    return node.getvalue()
