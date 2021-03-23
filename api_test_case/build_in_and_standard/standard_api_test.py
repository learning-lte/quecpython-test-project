"""
@Author: trent.zhang
@Date: 2020-11-17
@LastEditTime: 2020-10-17
@FilePath: standard_api_test.py
"""
import utime
import uos
import gc
import ubinascii
import urandom
import math
import ustruct
import ujson
import sys
import uhashlib
import ucollections
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


if __name__ == '__main__':
    print("------------------uos---------------------;")
    list = [
        "uos.listdir()",
        "uos.mkdir('/usr/testdir')",
        "uos.statvfs('/usr/testdir')",
        "uos.uname()",
        "uos.urandom(5)",
        "uos.rename('/usr/testdir', '/usr/testdir1')",
        "uos.rmdir('/usr/testdir1')",
        "uos.getcwd()",
    ]
    for i in list:
        api_test(i)
    print("------------------gc---------------------;")

    list = [
        "gc.enable()",
        "gc.collect()",
        "gc.mem_alloc()",
        "gc.mem_free()",
    ]
    for i in list:
        api_test(i)
    print("------------------ubinascii---------------------;")
    list = [
        "ubinascii.hexlify('\x11\x22123')",
        "ubinascii.hexlify('abcdfg')",
        "ubinascii.hexlify('\x11\x22123', ' ')",
        "ubinascii.hexlify('\x11\x22123', ',')",
        "ubinascii.unhexlify('313222')",
    ]
    for i in list:
        api_test(i)
    print("------------------ucollections---------------------;")
    list = [
        """ucollections.namedtuple("mytuple", ("id", "name"))(1, "foo").name""",
        "ucollections.deque((),5).append(1)",
        # "ucollections.deque((),5).popleft()",
    ]
    for i in list:
        api_test(i)
    print("------------------urandom---------------------;")
    list = [
        "urandom.choice('QuecPython')",
        "urandom.getrandbits(1)",
        "urandom.randint(1, 4)",
        "urandom.random()",
        "urandom.randrange(0, 8, 2)",
        "urandom.seed(20)",
        "urandom.uniform(3, 5)",
    ]
    for i in list:
        api_test(i)
    print("------------------math---------------------;")
    list = [
        "math.pow(2, 3)",
        "math.acos(0.6)",
        "math.asin(-1)",
        "math.atan(-8)",
        "math.atan2(-0.50,0.48)",
        "math.ceil(4.1)",
        "math.copysign(5, 0)",
        "math.cos(3)",
        "math.degrees(5)",
        "math.exp(1)",
        "math.fabs(-3.88)",
        "math.floor(8.7)",
        "math.fmod(15, 3)",
        "math.modf(17.592)",
        "math.frexp(52)",
        "math.isfinite(8)",
        "math.isinf(123)",
        "math.isnan(23)",
        "math.ldexp(2, 1)",
        "math.log(2)",
        "math.radians(90)",
        "math.sqrt(4)",
        "math.tan(9)",
        "math.trunc(7.123)",
    ]
    for i in list:
        api_test(i)
    print("------------------ustruct---------------------;")
    list = [
        "ustruct.calcsize('i')",
        "ustruct.pack('ii', 7, 9)",
        "ustruct.unpack('ii', b'\x07\x00\x00\x00\t\x00\x00\x00')",

    ]
    for i in list:
        api_test(i)
    print("------------------ujson---------------------;")
    list = [
        """ujson.dumps("['foo', {'bar': ('baz', None, 1, 2)}]")""",
        """ujson.loads(ujson.dumps("['foo', {'bar': ('baz', None, 1, 2)}]"))"""
    ]
    for i in list:
        api_test(i)
    print("------------------utime---------------------;")
    list = [
        "utime.localtime()",
        "utime.localtime(646898736)",
        "utime.mktime((2020, 9, 29, 8, 54, 42, 1, 273))",
        "utime.sleep(0.05)",
        "utime.sleep_ms(1)",
        "utime.sleep_us(1)",
        "utime.ticks_ms()",
        "utime.ticks_us()",
        "utime.ticks_cpu()",
        "utime.ticks_diff(utime.ticks_us(), utime.ticks_us())",
        "utime.time()"
    ]
    for i in list:
        api_test(i)
    print("------------------sys---------------------;")
    list = [
        "sys.argv",
        "sys.byteorder",
        "sys.implementation",
        "sys.maxsize",
        "sys.modules",
        "sys.platform",
        "sys.stdin",
        "sys.stdout",
        "sys.version",
        "sys.version_info",
    ]
    for i in list:
        api_test(i)
    print("------------------uhashlib---------------------;")
    list = [
        "uhashlib.sha256()",
        "uhashlib.sha256().update(b'QuecPython')",
        "uhashlib.sha256().digest()",
        "ubinascii.hexlify(uhashlib.sha256().digest())"
    ]
    for i in list:
        api_test(i)
