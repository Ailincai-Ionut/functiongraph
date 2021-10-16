
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


class Operation:
    prio = None

    def __init__(self):
        self.prio = None
        self.symbol = None

    def evaluate(self, op1, op2):
        return None

    def getSymbol(self):
        return self.symbol

    def getPriority(self):
        return self.prio


class Addition(Operation):
    def __init__(self):
        self.prio = 1
        self.symbol = "+"

    def evaluate(self, op1, op2):
        return op1 + op2


class Difference(Operation):
    def __init__(self):
        self.prio = 1
        self.symbol = "-"

    def evaluate(self, op1, op2):
        return op1 - op2


class Multiplication(Operation):
    def __init__(self):
        self.prio = 2
        self.symbol = "*"

    def evaluate(self, op1, op2):
        return op1 * op2


class Division(Operation):
    def __init__(self):
        self.prio = 2
        self.symbol = "/"

    def evaluate(self, op1, op2):
        return op1 / op2


class Power(Operation):
    def __init__(self):
        self.prio = 2
        self.symbol = "^"

    def evaluate(self, op1, op2):
        return op1 ** op2


class OpenBracket(Operation):
    def __init__(self):
        self.prio = 0
