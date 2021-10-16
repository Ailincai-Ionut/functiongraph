'''

@author: Ailincai Ionut

This module provides functions for analizing the function
in the form of string and evaluating it
'''
from declarations import *


def value_post(expression):
    value = 0
    stack = []
    for el in expression:
        if el.isnumeric():
            stack.append(float(el))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if el == "+":
                value = operand1 + operand2
                stack.append(value)
            if el == "-":
                value = operand1 - operand2
                stack.append(value)
            if el == "*":
                value = operand1 * operand2
                stack.append(value)
            if el == "/":
                value = operand1 / operand2
                stack.append(value)
    return stack.pop()


def to_postfix_text(expression):
    opstack = []
    postfix = []
    i = 0
    while(i < len(expression)):
        if expression[i] in "+-/*":
            if len(opstack) > 0:
                while len(opstack) > 0 and post_values(expression[i]) <= post_values(opstack[-1]):
                    if opstack[-1] != "(":
                        postfix.append(opstack.pop())
                    else:
                        opstack.pop()
            opstack.append(expression[i])
        elif expression[i] == "(":
            opstack.append(expression[i])
        elif expression[i] == ")":
            while opstack[-1] != "(" and len(opstack) > 0:
                postfix.append(opstack.pop())
            opstack.pop()
        elif expression[i] != " ":
            to = i
            while to < len(expression) - 1 and expression[to + 1].isnumeric():
                to += 1
            postfix.append(expression[i:to + 1])
            i = to
        i += 1
    if len(opstack) > 0:
        while len(opstack) > 0:
            postfix.append(opstack.pop())
    return postfix


operations = {"+": Addition,
              "-": Difference,
              "*": Multiplication,
              "/": Division,
              "^": Power,
              "(": OpenBracket,
              }


def getOperation(operation):
    return operations[operation]


def getPrio(operation):
    return operations[operation]().getPriority()


def to_postfix(expression):
    opstack = []
    postfix = []
    i = 0
    while i < len(expression):
        if expression[i] == "(":
            opstack.append(getOperation(expression[i])())
        elif expression[i] in operations:
            while len(opstack) > 0 and getPrio(expression[i]) <= opstack[-1].getPriority():
                if not isinstance(opstack[-1], OpenBracket):
                    postfix.append(opstack.pop())
                else:
                    opstack.pop()
            opstack.append(getOperation(expression[i])())
        elif expression[i] == ")":
            while not isinstance(opstack[-1], OpenBracket):
                postfix.append(opstack.pop())
            opstack.pop()
        elif expression[i] != " ":
            to = i
            while to < len(expression) - 1 and expression[to + 1].isnumeric():
                to += 1
            postfix.append(Constant(float(expression[i:to + 1])))
            i = to
        i += 1
    if len(opstack) > 0:
        while len(opstack) > 0:
            postfix.append(opstack.pop())
    return postfix


def evaluate_post(expression):
    value = 0
    stack = []
    for el in expression:
        if isinstance(el, Operand):
            stack.append(el.getValue())
        elif isinstance(el, Operation):
            op2 = stack.pop()
            op1 = stack.pop()
            value = el.evaluate(op1, op2)
            stack.append(value)
    return stack.pop()


def test():
    assert evaluate_post(to_postfix("  10 + 20")) == 30
    assert evaluate_post(to_postfix("  10 / 20")) == 0.5
    assert evaluate_post(to_postfix("  10 - 20")) == -10
    assert evaluate_post(to_postfix("  10 * 20")) == 200
    assert evaluate_post(to_postfix("(0-2)^3")) == -8
    assert evaluate_post(to_postfix("0-10 + 20 / (2*10)")) == -9
    print("Good")


test()
