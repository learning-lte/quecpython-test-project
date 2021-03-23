# 数学运算math函数示例

import math

# x**y运算后的值
>>> math.pow(2,3)
8.0

# 取大于等于x的最小的整数值，如果x是一个整数，则返回x
>>> math.ceil(4.12)
5

# 把y的正负号加到x前面，可以使用0
>>> math.copysign(2,-3)
-2.0

# 求x的余弦，x必须是弧度
>>> math.cos(math.pi/4)
0.7071067811865476

# 把x从弧度转换成角度
>>> math.degrees(math.pi/4)
45.0

# e表示一个常量
>>> math.e
2.718281828459045

# exp()返回math.e(其值为2.71828)的x次方
>>> math.exp(2)
7.38905609893065

# fabs()返回x的绝对值
>>> math.fabs(-0.03)
0.03

# floor()取小于等于x的最大的整数值，如果x是一个整数，则返回自身
>>> math.floor(4.999)
4

# fmod()得到x/y的余数，其值是一个浮点数
>>> math.fmod(20,3)
2.0

# frexp()返回一个元组(m,e),其计算方式为：x分别除0.5和1,得到一个值的范围，2e的值在这个范围内，e取符合要求的最大整数值,然后x/(2e),得到m的值。如果x等于0,则m和e的值都为0,m的绝对值的范围为(0.5,1)之间，不包括0.5和1
>>> math.frexp(75)
(0.5859375, 7)

# isfinite()如果x不是无穷大的数字,则返回True,否则返回False
>>> math.isfinite(0.1)
True

# isinf()如果x是正无穷大或负无穷大，则返回True,否则返回False
>>> math.isinf(234)
False

# isnan()如果x不是数字True,否则返回False
>>> math.isnan(23)
False

# ldexp()返回x*(2**i)的值
>>> math.ldexp(5,5)
160.0

# modf()返回由x的小数部分和整数部分组成的元组
>>> math.modf(math.pi)
(0.14159265358979312, 3.0)

# pi:数字常量，圆周率
>>> print(math.pi)
3.141592653589793

# sin()求x(x为弧度)的正弦值
>>> math.sin(math.pi/4)
0.7071067811865476

# sqrt()求x的平方根
>>> math.sqrt(100)
10.0

# tan()返回x(x为弧度)的正切值
>>> math.tan(math.pi/4)
0.9999999999999999

# trunc()返回x的整数部分
>>> math.trunc(6.789)
6