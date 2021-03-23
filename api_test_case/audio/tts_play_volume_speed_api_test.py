# -*- coding: UTF-8 -*-
'''
@Author: Randy
@Date: 2020-09-08
@LastEditTime: 2020-09-08
@Description: API test for tts
@FilePath: tts_play_volume_speed_api_test.py
'''

import audio
import utime

def tts_cb(event):
    if event == 2:
        print('TTS-play start.;')
    elif event == 4:
        print('TTS-play finish.;')
    elif event == 3:
        print('TTS-play stop.;')
    elif event == 5:
        print('TTS-play fail.;')

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
    print('%s:: %s||result_api:: %s;'%(api,result1,result2))
    utime.sleep(0.05)

api_list = [
    'TTS.play(1,1,2,"1223")',
    'TTS.getState()',
    'TTS.play(2,0,1,"移远通信，万物互联")',
    'TTS.play(3,1,3,"AAAAAAAAAAAAAAAA")',
    'TTS.play(4,1,2,"移远通信，万物互联")',
    'TTS.stop()',
    'TTS.getVolume()',
    'TTS.setVolume(0)',
    'TTS.getVolume()',
    'TTS.setVolume(5)',
    'TTS.getVolume()',
    'TTS.setVolume(10)',
    'TTS.getVolume()',
    'TTS.getSpeed()',
    'TTS.setSpeed(10)',
    'TTS.getSpeed()',
    'TTS.setSpeed(0)',
    'TTS.getSpeed()',
    'TTS.setSpeed(5)',
    'TTS.getSpeed()',
    'TTS.play(1,1,2,"nihao")',
    'TTS.close()'
            ]
for i in range(3):
    if i == 0:
        print('Current audio peripheral: 0-microphone;')
    elif i == 1:
        print('Current audio peripheral: 1-headset;')
    elif i == 2:
        print('Current audio peripheral: 2-speaker;')
    TTS = audio.TTS(i)   # 0-话筒，1-耳机，2-喇叭
    TTS.setCallback(tts_cb)
    for i in api_list:
        api_test(i)