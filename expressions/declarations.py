import math


class Operand:
    def getValue():
        return None


class Constant(Operand):
    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value


class Variable(Operand):
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def getName(self):
        return self.name


class Operation:
    prio = None

    def __init__(self):
        self.prio = None
        self.symbol = None
        self.func = False
        self.mulOut = False

    def evaluate(self, op1, op2):
        if op1 is None or op2 is None:
            return None
        return self.getResult(op1, op2)

    def isFunc(self):
        return self.func

    def getSymbol(self):
        return self.symbol

    def getPriority(self):
        return self.prio

    def getResult(self, op1, op2):
        return None

    def isMultiple(self):
        return self.mulOut


class Addition(Operation):
    def __init__(self):
        self.prio = 1
        self.symbol = "+"
        self.func = False
        self.mulOut = False

    def getResult(self, op1, op2):
        return op1 + op2


class Difference(Operation):
    def __init__(self):
        self.prio = 1
        self.symbol = "-"
        self.func = False
        self.mulOut = False

    def getResult(self, op1, op2):
        return op1 - op2


class Multiplication(Operation):
    def __init__(self):
        self.prio = 2
        self.symbol = "*"
        self.func = False
        self.mulOut = False

    def getResult(self, op1, op2):
        return op1 * op2


class Division(Operation):
    def __init__(self):
        self.prio = 2
        self.symbol = "/"
        self.func = False
        self.mulOut = False

    def getResult(self, op1, op2):
        if op2 == 0:
            return None
        return op1 / op2


class Power(Operation):
    def __init__(self):
        self.prio = 2
        self.symbol = "^"
        self.func = False
        self.mulOut = False

    def getResult(self, op1, op2):
        return op1**op2


class Logarithm(Operation):
    def __init__(self):
        self.prio = 3
        self.symbol = "log"
        self.func = True
        self.mulOut = False

    def getResult(self, op1, op2):
        if op1 <= 0 or op1 == 1:
            return None
        return math.log(op2, op1)


class Min(Operation):
    def __init__(self):
        self.prio = 3
        self.symbol = "min"
        self.func = True
        self.mulOut = False

    def getResult(self, op1, op2):
        return min([op1, op2])


class Max(Operation):
    def __init__(self):
        self.prio = 3
        self.symbol = "max"
        self.func = True
        self.mulOut = False

    def getResult(self, op1, op2):
        return max([op1, op2])


class Sin(Operation):
    def __init__(self):
        self.prio = 3
        self.symbol = "sin"
        self.func = True
        self.mulOut = False

    def getResult(self, op1, op2):
        return math.sin(op1)


class Cos(Operation):
    def __init__(self):
        self.prio = 3
        self.symbol = "cos"
        self.func = True
        self.mulOut = False

    def getResult(self, op1, op2):
        return math.cos(op1)


class Tan(Operation):
    def __init__(self):
        self.prio = 3
        self.symbol = "tan"
        self.func = True
        self.mulOut = False

    def getResult(self, op1, op2):
        return math.tan(op1)


class ArcSin(Operation):
    def __init__(self):
        self.prio = 3
        self.symbol = "arcsin"
        self.func = True
        self.mulOut = False

    def getResult(self, op1, op2):
        if op1 > 1 or op1 < -1:
            return None
        return math.asin(op1)


class ArcCos(Operation):
    def __init__(self):
        self.prio = 3
        self.symbol = "arccos"
        self.func = True
        self.mulOut = False

    def getResult(self, op1, op2):
        if op1 > 1 or op1 < -1:
            return None
        return math.acos(op1)


class ArcTan(Operation):
    def __init__(self):
        self.prio = 3
        self.symbol = "arctan"
        self.func = True
        self.mulOut = False

    def getResult(self, op1, op2):
        if op1 > 1 or op1 < -1:
            return None
        return math.atan(op1)


class SquareRoot(Operation):
    def __init__(self):
        self.prio = 3
        self.symbol = "sqrt"
        self.func = True
        self.mulOut = False

    def getResult(self, op1, op2):
        if op1 < 0:
            return None
        # Implement multiple possible solutions
        # return [math.sqrt(op1), -math.sqrt(op1)]
        return math.sqrt(op1)


class OpenBracket(Operation):
    def __init__(self):
        self.prio = 0
        self.func = False
