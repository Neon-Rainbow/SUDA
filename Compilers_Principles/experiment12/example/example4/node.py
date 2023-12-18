#! /usr/bin/env python
# coding=utf-8
class node:

    def __init__(self, data):
        self._data = data
        self._children = []
        self._value = None

    def getdata(self):
        return self._data

    def setvalue(self, value):
        self._value = value

    def getvalue(self):
        return self._value

    def getchild(self, i):
        return self._children[i]

    def getchildren(self):
        return self._children

    def add(self, node):
        self._children.append(node)

    def print_node(self, prefix):
        print('  ' * prefix, '+', self._data)
        for child in self._children:
            child.print_node(prefix + 1)


def num_node(data):
    t = node(data)
    t.setvalue(float(data))
    return t
