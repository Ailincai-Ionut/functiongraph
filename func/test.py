from declarations import *


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


a = Addition()
print("test:", getPrio("+"))
l = to_postfix1("10^2")
print(l)
for el in l:
    if isinstance(el, Operand):
        print(el.getValue())
    elif isinstance(el, Operation):
        print(el.getSymbol())
