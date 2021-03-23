'''
@Author: Baron
@Date: 2020-06-17
@LastEditTime: 2020-06-17 17:06:08
@Description: example for module ujson
@FilePath: example_json.py
'''
import ujson

inp = {'bar': ('baz', None, 1, 2)}
>>> print(type(inp))
<class 'dict'>

# 将Dict转换为json
s = ujson.dumps(inp)
>>> print(s， type(s))
{"bar": ["baz", null, 1, 2]}, <class 'str'>

# 将json转换为Dict
outp = ujson.loads(s)

# ujson.dump()和juson.load()主要用来读写json文件函数，正对于读写json文件