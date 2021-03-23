# -*- coding: UTF-8 -*-
"""
@Author: Randy
@Date: 2021-01-29
@LastEditTime: 2021-01-29
@Description: function test for backup_restore
@FilePath: app_backup_restore.py
"""
'''
-------------------------------------------------------------------------------
脚本逻辑:
    1.开机检查usr目录下是否存在备份文件
    2.任意删除或修改usr目录下的备份文件
    3.重启
脚本统计:
    1.接口函数调用崩溃log
测试前准备:
    1.烧录带有bak镜像的固件包
    2.修改此文件名称为main.py
-------------------------------------------------------------------------------
'''
import uos
import utime
import urandom

########用户配置区#############
runtimes = 0  #运行次数,0为不限制次数
bak_file_list = ['/usr/test.py']  # 备份文件列表, 请注意此文件一定在bak中有备份源文件
##############################


########代码运行区#############
n = 1
while 1:
    start_time = utime.time()
    duration = utime.time() - start_time
    if n > runtimes and runtimes != 0:
        print('-------------Test Done-------------;')
        break
    else:
        print('current runtimes: %s;'%n)
    if duration % 600 == 0:
        print('keep running... current duration: %s current runtimes: %s;' % (duration, n))
        utime.sleep(1)

    try:
        for i in bak_file_list:
            if i in uos.listdir('/usr'):
                if urandom.randint(0,2):  # 随机删除或修改备份文件
                    uos.remove(i)     # 删除
                else:
                    with open(i,'wb+') as f:
                        f.write(b'#test') # 修改备份文件
            else:
                print('##########[ERROR]file:%s restore fail#################;'%i)


    except Exception as e:
        print('backup_restore::runtimes %s,[error]%s||result_api:: False;'%(n, e))

    try:
        aud.getState()
        aud.play(urandom.randint(0, 5), urandom.randint(0, 2), 'U:/music.mp3')
        # aud.stop()
        aud.play(urandom.randint(0, 5), urandom.randint(0, 2), 'U:/music.amr')
        # aud.stop()
    except Exception as e:
        print('audio getstate&play&stop::runtimes%s, erro: %s||result_api:: False;' % (n, e))
    n += 1
    utime.sleep(3)
#############################

