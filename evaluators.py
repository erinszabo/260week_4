# import unittest

class Stack:  # a stack of blocks
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):  # place a new block on the stack O(1)
        self.items.append(item)

    def pop(self):  # look at and remove the top block O(1), bottom block O(n)
        return self.items.pop()

    def peek(self):  # just look at the top block O(1), bottom block O(n)
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def infixToPostfix(infixexpr):
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.is_empty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.is_empty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    try:
        for token in tokenList:
            if token in "0123456789":
                operandStack.push(int(token))
            else:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = doMath(token, operand1, operand2)
                operandStack.push(result)
        return operandStack.pop()

    except:
        return "invalid input"


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


""" TESTING BELOW """

# class TestMethods(unittest.TestCase):
#    def test_doMath(self):
#        self.assertEqual(,)
