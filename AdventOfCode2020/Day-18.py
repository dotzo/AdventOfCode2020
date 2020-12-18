# Day 18

# Description

import os
import sys
import ast

__inputfile__ = 'Day-18-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip().split('\n') # Takes the inputfile as a string

test1 = '''1 + 2 * 3 + 4 * 5 + 6\n'''

class part1(ast.NodeTransformer):
    def visit_BinOp(self, node):
        self.generic_visit(node)
        if type(node.op) is ast.Sub:
            newnode = ast.BinOp(left=node.left, op=ast.Mult(), right=node.right)
            ast.copy_location(newnode, node)
            ast.fix_missing_locations(newnode)
            return newnode
        else:
            return node

class part2(ast.NodeTransformer):
    def visit_BinOp(self, node):
        self.generic_visit(node)
        if type(node.op) is ast.Sub:
            newnode = ast.BinOp(left=node.left, op=ast.Mult(), right=node.right)
            ast.copy_location(newnode, node)
            ast.fix_missing_locations(newnode)
            return newnode
        elif type(node.op) is ast.Div:
            newnode = ast.BinOp(left=node.left, op=ast.Add(), right=node.right)
            ast.copy_location(newnode, node)
            ast.fix_missing_locations(newnode)
            return newnode
        else:
            return node


def doPart1(s):
    res = 0
    for line in s:
        line = line.replace('*','-')
        tree = ast.parse(line, mode = "eval")
        tree = part1().visit(tree)
        res += eval(compile(tree, filename = "<ast>", mode="eval"))
    return res

def doPart2(s):
    res = 0
    for line in s:
        line = line.replace('*','-')
        line = line.replace('+','/')
        tree = ast.parse(line, mode = "eval")
        tree = part2().visit(tree)
        res += eval(compile(tree, filename = "<ast>", mode="eval"))
    return res



if __name__ == "__main__":
    print("Part 1:")
    print(doPart1(input_str))
    print("Part 2:")
    print(doPart2(input_str))