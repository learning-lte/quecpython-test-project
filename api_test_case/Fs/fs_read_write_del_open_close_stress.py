# -*- coding: UTF-8 -*-
'''
@Author: Randy
@Date: 2020-09-08
@LastEditTime: 2021-01-08
@Description: API test for fs
@FilePath: fs_read_write_del_open_close_stress.py
'''

import uos
import urandom
import utime

interval = 7200    #运行持续时长
runtimes = 0 #运行次数

def fs_open_close():
    try:
        f = open('/usr/1', 'r')
        f.close()
        #print('fs .open(),.close(),result_api: True;')
    except Exception as e:
        print('fs .open(),.close()::||result_api:: Flase;')

def fs_write_close():
    try:
        f = open('/usr/1', 'w')
        f.write('移远通信！@#￥%&*（）')
        f.close()
        #print('fs .write(),.close(),result_api: True;')
    except Exception as e:
        print('fs .write(),.close()::||result_api:: Flase;')

def fs_write_difftype_close():
    name, info = '2.txt', b'0123456ABCdef'
    try:
        # rb wb 创建覆盖二进制读写测试
        info = b'0123456ABCdef'
        if (name in uos.listdir('/usr')):
            uos.remove('/usr/%s' % name)
        f = open('/usr/2.txt', 'wb')
        f.write(info)
        f.close()
        f = open('/usr/2.txt', 'rb')
        w_data = f.read()
        if w_data != info:
            print('fs .write() type:rb wb ::write(%s),actual read(%s)||result_api:: Flase;' % (w_data, info))
        f.close()

        # r w 创建覆盖读写测试
        info = '0123456ABCdef'
        if (name in uos.listdir('/usr')):
            uos.remove('/usr/%s'%name)
        f = open('/usr/2.txt', 'w')
        f.write(info)
        f.close()
        f = open('/usr/2.txt', 'r')
        w_data = f.read()
        if w_data != info:
            print('fs .write() type:r w ::write(%s),actual read(%s)||result_api:: Flase;'%(w_data,info))
        f.close()

        # w+ 创建覆盖读写测试
        name, info = '2.txt', '0123456ABCdef'
        if (name in uos.listdir('/usr')):
            uos.remove('/usr/%s' % name)
        f = open('/usr/2.txt', 'w+')
        f.write(info)
        f.close()
        f = open('/usr/2.txt', 'w+')
        w_data = f.read()
        if  info in w_data:
            print('fs .write() type:w+ ::write(%s),actual read(%s)||result_api:: Flase;' % (w_data, info))
        f.close()

        # r a 创建追加读写测试
        info = '0123456ABCdef'
        if (name in uos.listdir('/usr')):
            uos.remove('/usr/%s' % name)
        f = open('/usr/2.txt', 'a')
        f.write(info)
        f.close()
        f = open('/usr/2.txt', 'a')
        f.write(name)
        f.close()
        f = open('/usr/2.txt', 'r')
        w_data = f.read()
        if w_data != (info+name):
            print('fs .write() type:r a ::write(%s),actual read(%s)||result_api:: Flase;' % (w_data, info))
        f.close()

        # rb ab 创建追加二进制读写测试
        info = b'0123456ABCdef'
        name = b'2.txt'
        if ('2.txt' in uos.listdir('/usr')):
            uos.remove('/usr/2.txt')
        f = open('/usr/2.txt', 'ab')
        f.write(info)
        f.close()
        f = open('/usr/2.txt', 'ab')
        f.write(name)
        f.close()
        f = open('/usr/2.txt', 'rb')
        w_data = f.read()
        if w_data != (info + name):
            print('fs .write() type:rb ab ::write(%s),actual read(%s)||result_api:: Flase;' % (w_data, info))
        f.close()

        # ab+ 创建追加二进制读写测试
        info = b'0123456ABCdef'
        name = b'2.txt'
        if ('2.txt' in uos.listdir('/usr')):
            uos.remove('/usr/2.txt')
        f = open('/usr/2.txt', 'ab+')
        f.write(info)
        f.close()
        f = open('/usr/2.txt', 'ab+')
        f.write(name)
        f.close()
        f = open('/usr/2.txt', 'ab+')
        w_data = f.read()
        if w_data != (info + name):
            print('fs .write() type:ab+ ::write(%s),actual read(%s)||result_api:: Flase;' % (w_data, info))
        f.close()

    except Exception as e:
        print('fs .write(),difftype::fail||result_api:: Flase;')

def fs_read_close():
    try:
        f = open('/usr/1', 'r')
        f.read()
        f.close()
        #print('fs .read(),.close(),result_api: True;')
    except Exception as e:
        print('fs .read(),.close()::||result_api:: Flase;')

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
        #print('fs .read(),.write(),.close(),result_api: True;')
    except Exception as e:
        print('fs .read(),.write(),.close()::||result_api:: Flase;')

def print_flash_size(FLASH):
    '''
    获取 flash 分区大小
    :param FLASH: 分区路径
    :return: flash_free,flash_total: 剩余分区大小，总分区大小 bytes
    '''
    statvfs_fields = ['bsize', 'frsize', 'blocks', 'bfree', 'bavail', 'files', 'ffree', ]
    info = dict(zip(statvfs_fields, uos.statvfs(FLASH)))
    flash_total = info['bsize'] * info['blocks']
    flash_free = info['frsize'] * info['bfree']
    print('flash total : ' + str(info['bsize'] * info['blocks'] / 1024) + ' kb;')
    print('flash free : ' + str(info['frsize'] * info['bfree'] / 1024) + ' kb;')
    return flash_free,flash_total

def write_full_clear():
    while 1:
        lenth = urandom.randint(1,1024)
        total,free = print_flash_size('/usr')
        if free > lenth:
            f = open('/usr/3', 'ab')
            f.write(uos.urandom(lenth))
            f.close()
        else:
            break
    uos.remove('/usr/3')


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
    #utime.sleep(0.5)


if __name__ == '__main__':
    print_flash_size('/usr')
    start_time = utime.time()
    a = 0
    print('####fs_open_close_api_stress...####;')
    f = open('/usr/1', 'w')
    f.write('abcdefghijklmnopqrstuvwxyz123456789')
    f.close()
    while 1:
        duration = utime.time() - start_time
        if duration > interval and interval != 0:
            break
        if runtimes != 0 and a == runtimes:
            break
        else:
            a = a + 1

        fs_open_close()
        if duration % 600 == 0:
            print('------------Runtimes: %s ------------;' % a)
            print('keep running... current duration: %s H;' % float(duration / 3600))
            utime.sleep(1)

    start_time = utime.time()
    a = 0
    print('####fs_open_write_close_api_stress...####;')
    f = open('/usr/1', 'w')
    f.write('abcdefghijklmnopqrstuvwxyz123456789')
    f.close()
    while 1:
        duration = utime.time() - start_time
        if duration > interval and interval != 0:
            break
        if runtimes != 0 and a == runtimes:
            break
        else:
            a = a + 1

        fs_write_close()
        if duration % 600 == 0:
            print('------------Runtimes: %s ------------;' % a)
            print('keep running... current duration: %s H;' % float(duration / 3600))
            utime.sleep(1)

    start_time = utime.time()
    a = 0
    print('####fs_open_write_difftype_close_api_stress...####;')
    f = open('/usr/1', 'w')
    f.write('abcdefghijklmnopqrstuvwxyz123456789')
    f.close()
    while 1:
        duration = utime.time() - start_time
        if duration > interval and interval != 0:
            break
        if runtimes != 0 and a == runtimes:
            break
        else:
            a = a + 1

        fs_write_difftype_close()
        if duration % 600 == 0:
            print('------------Runtimes: %s ------------;' % a)
            print('keep running... current duration: %s H;' % float(duration / 3600))
            utime.sleep(1)

    start_time = utime.time()
    a = 0
    print('####fs_open_read_close_api_stress...####;')
    f = open('/usr/1', 'w')
    f.write('abcdefghijklmnopqrstuvwxyz123456789')
    f.close()
    while 1:
        duration = utime.time() - start_time
        if duration > interval and interval != 0:
            break
        if runtimes != 0 and a == runtimes:
            break
        else:
            a = a + 1

        fs_read_close()
        if duration % 600 == 0:
            print('------------Runtimes: %s ------------;' % a)
            print('keep running... current duration: %s H;' % float(duration / 3600))
            utime.sleep(1)

    start_time = utime.time()
    a = 0
    print('####fs_write_full_clear_api_stress...####;')
    while 1:
        duration = utime.time() - start_time
        if duration > interval and interval != 0:
            break
        if runtimes != 0 and a == runtimes:
            break
        else:
            a = a + 1

        fs_read_close()
        if duration % 600 == 0:
            print('------------Runtimes: %s ------------;' % a)
            print('keep running... current duration: %s H;' % float(duration / 3600))
            utime.sleep(1)

    start_time = utime.time()
    a = 0
    print('####fs_uos_api_stress...####;')
    while 1:
        duration = utime.time() - start_time
        if duration > interval and interval != 0:
            break
        if runtimes != 0 and a == runtimes:
            break
        else:
            a = a + 1

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
        if duration % 600 == 0:
            print('------------Runtimes: %s ------------;' % a)
            print('keep running... current duration: %s H;' % float(duration/3600))
            utime.sleep(1)
