'''

@author: Ailincai Ionut

This module provides functions for analizing an expression and getting its value
'''
from declarations import *


def evaluate_post_text(expression):
    # This function gets the list from the to_postfix_text and spits the value
    # corresponding to the expression
    # Only Basic operation supported
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
    # This is the version of the to_posfix function that returns a list of
    # strings instead of objects
    # Has the same algorthm, might not work for multiple character operations
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


# The list of all operations
operations = {"+": Addition,
              "-": Difference,
              "*": Multiplication,
              "/": Division,
              "^": Power,
              "(": OpenBracket,
              "log": Logarithm,
              "min": Min,
              "max": Max,
              "sin": Sin,
              "cos": Cos,
              "tan": Tan,
              "arcsin": ArcSin,
              "arccos": ArcCos,
              "arctan": ArcTan,
              "sqrt": SquareRoot
              }


def getOperation(operation):
    # Returns the operation class from the literal form
    return operations[operation]


def getPrio(operation):
    # This function gets the priority of the coresponding operation
    return operations[operation]().getPriority()


def isCorrect(expression):
    nr_open = 0
    nr_closed = 0
    for chr in expression:
        if chr == "(":
            nr_open += 1
        if chr == ")":
            nr_closed += 1

    if nr_open != nr_closed:
        return False

    return True


def expand_expr(expression):
    # implement this shit when you're bored
    final_ex = []
    op_list = []
    i = len(expression)
    while i >= 0:
        nr_open = 0
        nr_closed = 0
        if expression[i:].find("ln("):
            j = i
        i -= 1

    # gets the sin(n)-> sin(n,0) or n! -> fact(n,0)
    return True


def number_var(expression):
    # implement when bored
    return True


def evaluate(expression, interval=[]):
    if len(interval) > 0:
        return get_interval_value(to_postfix(expression), interval)
    else:
        return [evaluate_post(to_postfix(expression))]


def to_postfix(expression):
    # This function gets an expression in the form of a string and
    # converts it into a list of operands and operations in the posfix notation
    # Ex.: 1+1 = 11+ in postfix\

    opstack = []  # the operation stack
    postfix = []  # the output, a list with operands and operations in the posfix form

    # We go through every character
    i = 0
    while i < len(expression):
        if expression[i] == "(":
            opstack.append(getOperation(expression[i])())
        elif expression[i] in operations:
            # if its and operation we pop and add to the output the operations on the opstack
            # that have a lower or equal priority
            # Priority ex: +<*<log
            while len(opstack) > 0 and getPrio(expression[i]) <= opstack[-1].getPriority():
                if not isinstance(opstack[-1], OpenBracket):
                    postfix.append(opstack.pop())
                else:
                    opstack.pop()
            # and we add it to the opstack
            opstack.append(getOperation(expression[i])())
        elif expression[i] == ")":
            while not isinstance(opstack[-1], OpenBracket):
                postfix.append(opstack.pop())
            opstack.pop()
            if len(opstack) > 0 and opstack[-1].isFunc():
                postfix.append(opstack.pop())

        elif expression[i] != " " and expression[i] != ",":
            # Here we check for numerical constants, variables or multiple characters
            # operations
            to = i
            if expression[i].isalpha():
                # Variables and multiple characters operations
                while to < len(expression) - 1 and expression[to + 1].isalpha() and expression[to + 1] != "(":
                    to += 1
                if expression[i:to + 1] in operations:
                    # if it's a multiple characters operation we did the same trick as for normal operations
                    while len(opstack) > 0 and getPrio(expression[i:to + 1]) <= opstack[-1].getPriority():
                        if not isinstance(opstack[-1], OpenBracket):
                            postfix.append(opstack.pop())
                        else:
                            opstack.pop()
                    opstack.append(getOperation(expression[i:to + 1])())
                else:
                    # Here we get a variable
                    postfix.append(Variable(expression[i:to + 1], 0))
            if expression[i].isnumeric():
                # Numerical constants
                while to < len(expression) - 1 and (expression[to + 1].isnumeric() or expression[to + 1] == "."):
                    to += 1
                postfix.append(Constant(float(expression[i:to + 1])))
            i = to
        i += 1
    if len(opstack) > 0:
        # if we still have some operation on the stack we put them in the output
        while len(opstack) > 0:
            postfix.append(opstack.pop())
    return postfix


def evaluate_post(expression):
    # This function evaluates the expression formed by the different
    # classes and gives you the value
    # It will return None if the parameters of the operations used
    # are incorrect
    value = 0
    stack = []
    for el in expression:
        if isinstance(el, Operand):
            stack.append(el.getValue())
        elif isinstance(el, Operation):
            op2 = stack.pop()
            op1 = stack.pop()
            if not el.isMultiple():
                value = el.evaluate(op1, op2)
                stack.append(value)
            # else:
            # maybe multiple stacks???
            # i set sqrt to one output
    return stack.pop()


def get_interval_value(expression, interval):
    # This function expects an expression with only one variable and
    # returns the list of values in the interval [start,end,increment]
    values = []
    index_list = []
    for i in range(len(expression)):
        if isinstance(expression[i], Variable):
            index_list.append(i)
    x = interval[0]
    while x < interval[1]:
        new_ex = expression.copy()
        for i in index_list:
            new_ex[i].setValue(x)
        values.append(evaluate_post(new_ex))
        x += interval[2]
    return values
