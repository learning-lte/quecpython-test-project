# -*- coding: UTF-8 -*-
'''
@Author: Randy
@Date: 2020-10-12
@LastEditTime: 2020-10-12
@Description: API test for tts
@FilePath: tts_play_volume_speed_stress.py
'''
'''
-------------------------------------------------------------------------------
脚本逻辑:
    1.单个或成对接口循环执行2H
    2.接口包含init&close,play&getstate&stop,getSpeed&setSpeed,getVolume&setVolume
    3.输出异常返回结果
脚本统计:
    1.接口函数调用崩溃log
测试前准备:
    无
-------------------------------------------------------------------------------
'''

import audio
import utime
import urandom

interval = 7200    #运行持续时长

print('Current audio peripheral: 0-microphone;')
print('tts_api_stress for 2H: init&close;')
start_time = utime.time()
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        break
    if duration%600 == 0:
        print('keep running... current duration: %s;'%duration)
        utime.sleep(1)
    try:
        TTS = audio.TTS(0)   # 0-话筒，1-耳机，2-喇叭
        TTS.close()
    except Exception as e:
        print('init&close::[error]%s||result_api:: False;'%e)

print('Current audio peripheral: 1-headset;')
print('tts_api_stress for 2H: play&getstate&stop;')
TTS = audio.TTS(1)
start_time = utime.time()
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        break
    if duration%600 == 0:
        print('keep running... current duration: %s;'%duration)
        utime.sleep(1)
    try:
        TTS.play(2,0,1,"移远通信，万物互联")
        TTS.getState()
        TTS.stop()
    except Exception as e:
        print('play&state&stop::[error]%s||result_api:: False;'%e)

print('Current audio peripheral: 2-speaker;')
print('tts_api_stress for 2H: 随机插入队列音频play;')
TTS = audio.TTS(2)
start_time = utime.time()
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        TTS.stop()
        break
    if duration%600 == 0:
        print('keep running... current duration: %s;'%duration)
        utime.sleep(1)
    try:
        TTS.play(urandom.randint(0, 4),urandom.randint(0, 1),urandom.randint(1,3),"移远通信万物互联移远通信万物互联移远通信万物互联"
                                                                                "移远通信万物互联移远通信万物互联移远通信万物互联"
                                                                                "移远通信万物互联移远通信万物互联移远通信万物互联")
        TTS.play(urandom.randint(0, 4), urandom.randint(0, 1), urandom.randint(1, 3), 'abcdefghi0123456789abcdefghi0123456789'
                                                                                      'abcdefghi0123456789abcdefghi0123456789'
                                                                                      'abcdefghi0123456789abcdefghi0123456789'
                                                                                      'abcd1234') #128字节数据
    except Exception as e:
        print('play::[error]%s||result_api:: False;'%e)

print('Current audio peripheral: 2-speaker;')
print('tts_api_stress for 2H: getSpeed&setSpeed;')
TTS = audio.TTS(2)
start_time = utime.time()
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        break
    if duration%600 == 0:
        print('keep running... current duration: %s;'%duration)
        utime.sleep(1)
    try:
        TTS.getSpeed()
        TTS.setSpeed(5)
    except Exception as e:
        print('getSpeed&setSpeed::[error]%s||result_api:: False;'%e)

print('Current audio peripheral: 2-speaker;')
print('tts_api_stress for 2H: getVolume&setVolume;')
TTS = audio.TTS(2)
start_time = utime.time()
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        break
    if duration%600 == 0:
        print('keep running... current duration: %s;'%duration)
        utime.sleep(1)
    try:
        for i in range(10):
            a = TTS.getVolume()
            b = TTS.setVolume(5)
            if a == -1:
                print('TTS.getVolume():: False||result_api:: False;')
            if b == -1:
                print('TTS.setVolume():: False||result_api:: False;')
    except Exception as e:
        print('getVolume&setVolume::[error]%s||result_api:: False;'%e)