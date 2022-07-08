from sympy import * #需要sympy函数库
x, y, z = symbols('x y z')
print( factor(x**3 - x**2 + x - 1) )#键入原式，不能省略乘号
