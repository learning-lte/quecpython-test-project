'''
@Author: Baron
@Date: 2020-06-22
@LastEditTime: 2020-06-22 17:16:20
@Description: example for module urandom
@FilePath: example_urandom.py
'''
import urandom as random

#urandom.randint(start, end)
# 随机1 ~ 4之间
print(random.randint(1, 4))

#random between 0~1
print(random.random())

#urandom.unifrom(start, end)
# 在开始和结束之间生成浮点数
print(random.uniform(2, 4))

#urandom.randrange(start, end, step)
#2-bit binary,the range is [00~11] (0~3)
print(random.getrandbits(2))

#8-bit binary,the range is [0000 0000~1111 11111] (0~255)
print(random.getrandbits(8))

#urandom.randrange(start, end, step)
# 从开始到结束随机生成递增的正整数
print(random.randrange(2, 8, 2))

#urandom.choice(obj)
#随机生成对象中元素的数量
print(random.choice("QuecPython"))