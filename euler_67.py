#! /usr/bin/env pypy

import euler_util

testdata = """3
7 4
2 4 6
8 5 9 3"""
data = open('triangle.txt').read()

class Node:
    def __init__(self, v):
        self.value = v
        self.children = []
    def __str__(self):
        return self.str_offset(0)
    def str_offset(self, offset = 0):
        o = offset * ' ' + str(self.value) 
        for c in self.children:
            o += '\n' + c.str_offset(offset+1)
        return o
    @euler_util.memoized
    def acc_children(self):
        best = None
        for c in self.children:
            v = c.acc_children()
            if best is None or v > best:
                best = v
        return self.value + (best if best is not None else 0)

def parse_data(d):
    root = None
    last_nodes = []
    nodes = []
    for row in map(lambda r: map(int, r.split(' ')), d.rstrip().split('\n')):
        # row is list of nums
        for i in xrange(len(row)):
            n = Node(row[i])
            if root is None: root = n
            
            if i - 1 >= 0: last_nodes[i-1].children.append(n)
            if i < len(last_nodes): last_nodes[i].children.append(n)
            nodes.append(n)
        last_nodes = nodes
        nodes = []
    return root

print(parse_data(testdata).acc_children())
print(parse_data(data).acc_children())

