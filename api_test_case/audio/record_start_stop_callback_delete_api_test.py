# coding: utf-8
"""
@Author: Randy
@Date: 2020-12-30
@LastEditTime: 2020-12-30
@Description: api test for module Record
@FilePath: record_start_stop_callback_delete_api_test.py
"""

import audio
import utime

def record_callback(para):
    '''
    录音回调函数
    :param para:
    :return:
    '''
    print("file_name:",para[0])
    print("audio_len:",para[1])
    print("record state:",para[2])

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
    print('%s:: %s||result_api:: %s;' % (api, result1, result2))
    utime.sleep(0.05)


if __name__ == '__main__':
    list = [
        "record.start(10, 1, 8000)",
        "record.stop()",
        "record.start(30, 2, 8000)",
        "record.getFilePath()"
        "record.getData(0, 44)",
        "record.getSize()",
        "record.exists()",
        "record.Delete()",
        "record.isBusy()"
        ]
    record = audio.Record('1',record_callback)
    audio = audio.Audio(0)
    for i in list:
        api_test(i)
        utime.sleep(0.5)
