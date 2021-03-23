'''
@Author: Randy
@Date: 2021-01-09
@LastEditTime: 2021-01-09
@Description: Function Test for FS
@FilePath: fs_write_full_stability.py
'''
import uos
import urandom
import utime

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

if __name__ == '__main__':
    while 1:
        print('######start fs write############')
        write_full_clear()
        print('######write done############')
        utime.sleep(1)