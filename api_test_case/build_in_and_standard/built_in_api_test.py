"""
@Author: trent.zhang
@Date: 2020-11-17
@LastEditTime: 2020-10-17
@FilePath: built_in_test_case.py
"""
import utime


def api_test(api):
    result1 = 'error'
    try:
        result1 = eval(api)
    except Exception as err:
        print('[error]'+str(err)+';')
    if result1 != 'error':
        result2 = True
    else:
        result2 = False
    print('%s:: %s||result_api:: %s;'%(api, result1, result2))
    utime.sleep(0.05)


def ap1_none(api):
    print('%s:: None||result_api:: NA;' % api)


if __name__ == '__main__':
    list = [
        "abs(1)",
        "all('a')",
        "any('2')",
        "bin(2)",
        "callable(2)",
        "chr(2)",
        'dir()',
        'divmod(7, 2)',
        "enumerate(['Summer','adad'])",
        "filter(5, [3, 4, 5, 6, 7, 8])",
        "globals()['Timer']",
        "hasattr(list, 'append')",
        "hash(9)",
        "hex(1)",
        "id(1)",
        'isinstance (11,int)',
        'iter([1.2])',
        "len('adad')",
        "locals()['Timer']",
        "map(lambda x :x*100,[1,2,3])",
        "max(1,2,3,5)",
        "min(1,2,3,5)",
        'next(iter([1, 2, 3, 4, 5]))',
        "oct(10)",
        "ord('a')",
        "pow(2, 10)",
        'property()',
        "range(0,10,2)",
        "repr('b')",
        "round(1,2)",
        "sorted(['1','2'])",
        "sum([2,3])",
        "range(0,10,2)",
        "zip()",
        'int(1)',
        "float(1)",
        # "complex(1)",
        "bool(1)",
        'type([1,2])',
        'range(2,5)',
        'str([1,2])',
        "bytes(1)",
        "bytearray(1)",
        "dict(a='a', b='b', t='t')",
        "set([1,2,3,2])",
    ]
    for i in list:
        api_test(i)
    list2 = [
        'classmethod()',
        'delattr()',
        'getattr()',
        'isinstance()',
        'setattr()',
        'staticmothed()',
        'super()',
        'object'
    ]
    for a in list2:
        ap1_none(a)
# reversed(),memoryview frozenset, slice
