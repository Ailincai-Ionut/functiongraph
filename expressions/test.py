from func import *


def test():
    assert evaluate("  10.1+ 20") == [30.1]
    assert evaluate("  10 / 20") == [0.5]
    assert evaluate("  10 - 20") == [-10]
    assert evaluate("  10 * 20") == [200]
    assert evaluate("(0-2)^3") == [-8]
    assert evaluate("0-10 + 20 / (2*10)") == [-9]
    # on function type operations it is acceptable op(x,y) and x op y(do not forget the spaces)
    # the functions that requires one paremetre need to be written like this sin(p,0)
    # the second parameter will be ignored
    assert evaluate("min(2,4)") == [2]
    assert evaluate("2max4") == [4]
    assert evaluate("2log4") == [2]
    # if you want to get to 2 for  example, you put the end as 2+somthing
    assert evaluate("log(x,x^2)", [0, 2.1, 1]) == [None, None, 2]
    print("All Good")


test()
print(evaluate("sqrt(3,0)"))
'''for el in l:
    if isinstance(el, Operand):
        print(el.getValue())
    elif isinstance(el, Operation):
        print(el.getSymbol())'''
