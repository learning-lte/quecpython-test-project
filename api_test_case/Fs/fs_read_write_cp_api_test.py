# -*- coding: UTF-8 -*-
'''
@Author: Randy
@Date: 2020-09-08
@LastEditTime: 2020-11-25
@Description: API test for fs
@FilePath: fs_write_read_api_test.py
'''

import uos
import utime
def fs_r_w():
    try:
        f = open('/usr/1', 'w')
        f.write('abcdefghijklmnopqrstuvwxyz123456789')
        f.close()
        f = open('/usr/1', 'r')
        f.read()
        f.close()
        f = open('/usr/1', 'w')
        f.write('移远通信！@#￥%&*（）')
        f.close()
        f = open('/usr/1', 'r')
        f.read()
        f.close()
        print('fs .read(),.write(),.close():: pass||result_api:: True;')
    except Exception as e:
        print('fs .read(),.write(),.close():: fail||result_api:: Flase;')

def api_test(api):
    result1 = '-1'
    try:
        result1 = eval(api)
    except Exception as err:
        print('[error]'+str(err)+';')
    if result1 != '-1':
        result2 = True
    else:
        result2 = False
    print('%s:: %s||result_api:: %s;'%(api, result1, result2))


if __name__ == '__main__':
    fs_r_w()
    list = [
       "uos.mkdir('/usr/user')",
           "uos.listdir('/usr')",
            "uos.ilistdir('/usr') ",
            "uos.chdir('/usr/user')",
            'uos.getcwd()',
            "uos.chdir('/usr')",
            "uos.rename('user', 'user1')",
            "uos.listdir('/usr')",
            "uos.rmdir('user1')",
            "uos.listdir()",
            "uos.stat('/usr')",
            "uos.statvfs('/usr')",
            "uos.urandom(8)",
            "uos.uname()",
    ]

    for i in list:
        api_test(i)