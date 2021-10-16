from declarations import *


operations = {"+": Addition,
              "-": Difference,
              "*": Multiplication,
              "/": Division,
              "^": Power,
              "(": OpenBracket,
              "log": Logarithm,
              "min": Min,
              "max": Max
              }


def getOperation(operation):
    return operations[operation]


def getPrio(operation):
    return operations[operation]().getPriority()


def to_postfix1(expression):
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
            if expression[i].isalpha():
                to = i
                while to < len(expression) - 1 and expression[to + 1].isalpha():
                    to += 1
                if expression[i:to + 1] in operations:
                    while len(opstack) > 0 and getPrio(expression[i:to + 1]) <= opstack[-1].getPriority():
                        if not isinstance(opstack[-1], OpenBracket):
                            postfix.append(opstack.pop())
                        else:
                            opstack.pop()
                    opstack.append(getOperation(expression[i:to + 1])())
                else:
                    # this shit is gonna break for operations like min(x,y)
                    # TODO: fix this shit pls
                    postfix.append(Variable(expression[i:to + 1], 0))
            if expression[i].isnumeric():
                to = i
                while to < len(expression) - 1 and (expression[to + 1].isnumeric() or expression[to + 1] == "."):
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


def evaluate_func(expression, intervals={}):
    # is for one variable only now
    values = []
    index_list = []
    for i in range(len(expression)):
        if isinstance(expression[i], Variable):
            index_list.append(i)
    for i in index_list:
        if expression[i].getName() in intervals:
            r = intervals[expression[i].getName()]
            x = r[0]
            while x < r[1]:
                new_ex = expression.copy()
                new_ex[i].setValue(x)
                values.append(evaluate_post(new_ex))
                x += r[2]
    return values


l = to_postfix1("2+x")
print(evaluate_post(l))
print(evaluate_func(l, {"x": [1, 10, .1]}))
'''for el in l:
    if isinstance(el, Operand):
        print(el.getValue())
    elif isinstance(el, Operation):
        print(el.getSymbol())'''
