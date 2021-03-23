# coding: utf-8
"""
@Author: Trent
@Date: 2020-10-12
@LastEditTime: 2020-10-12
@Description: api test for module request
@FilePath: request_post_get_put_head_patch_delete_stress.py
"""
'''
-------------------------------------------------------------------------------
脚本逻辑:
    1.单个或成对接口循环执行2H
    2.接口包含get&text&close,post&content&close,put&json&close,head&text&close,patch&text&close,delete&text&close,
    3.输出异常返回结果
脚本统计:
    1.接口函数调用崩溃log
测试前准备:
    无
-------------------------------------------------------------------------------
'''
import request
import utime
import _thread

interval = 3600    # 运行持续时长

runtimes = 0
print('[start] request_api_stress: get&text&close;')
start_time = utime.time()
while 1:
    duration = utime.time() - start_time
    if duration > interval:
        print('[end] request_api_stress: get&text&close,runtimes: %s;'%runtimes)
        runtimes = 0
        break
    if duration % 100 == 0:
        print('keep running... current duration: %sH;' % (duration/3600))
    try:
        response = request.get('http://httpbin.org/get')
        response.text
        response.close()
        print(_thread.get_heap_size())
        runtimes += 1
    except Exception as e:
        response.close()
        print('runtimes: %s,get&text:: %s||result_api:: False;' % (runtimes,e))
    utime.sleep(1)

print('[start] request_api_stress: post&content&close;')
start_time = utime.time()
while 1:
    duration = utime.time() - start_time
    if duration > interval:
        print('[end] request_api_stress: post&content&close,runtimes: %s;' % runtimes)
        runtimes = 0
        break
    if duration % 100 == 0:
        print('keep running... current duration: %sH;' % (duration/3600))
    try:
        response = request.post('http://httpbin.org/post')
        response.content
        response.close()
        print(_thread.get_heap_size())
        runtimes += 1
    except Exception as e:
        response.close()
        print('runtimes: %s,post&text&close:: %s||result_api:: False;' %(runtimes,e))
    utime.sleep(1)

print('[start] request_api_stress: put&json&close;')
start_time = utime.time()
while 1:
    duration = utime.time() - start_time
    if duration > interval:
        print('[end] request_api_stress: put&json&close,runtimes: %s;' % runtimes)
        runtimes = 0
        break
    if duration % 100 == 0:
        print('keep running... current duration: %sH;' % (duration/3600))
    try:
        response = request.put('http://httpbin.org/put')
        response.json
        response.close()
        runtimes += 1
    except Exception as e:
        response.close()
        print('runtimes: %s,put&json&close: %s,result_api: False;' %(runtimes,e))
    utime.sleep(1)

print('[start] request_api_stress: head&text&close;')
start_time = utime.time()
while 1:
    duration = utime.time() - start_time
    if duration > interval:
        print('[end] request_api_stress: head&text&close,runtimes: %s;' % runtimes)
        runtimes = 0
        break
    if duration % 100 == 0:
        print('keep running... current duration: %sH;' % (duration/3600))
    try:
        response = request.head('http://httpbin.org/get')
        response.text
        response.close()
        runtimes += 1
    except Exception as e:
        response.close()
        print('runtimes: %s,head&text&close:: %s||result_api:: False;' %(runtimes,e))
    utime.sleep(1)

print('[start]request_api_stress: patch&text&close')
start_time = utime.time()
while 1:
    duration = utime.time() - start_time
    if duration > interval:
        print('[end] request_api_stress: patch&text&close,runtimes: %s;' % runtimes)
        runtimes = 0
        break
    if duration % 100 == 0:
        print('keep running... current duration: %sH;' % (duration/3600))
    try:
        response = request.patch('http://httpbin.org/patch')
        response.text
        response.close()
        runtimes += 1
    except Exception as e:
        response.close()
        print('runtimes: %s,patch&text&close:: %s||result_api:: False;' %(runtimes,e))
    utime.sleep(1)

print('[start]request_api_stress: delete&text&close;')
start_time = utime.time()
while 1:
    duration = utime.time() - start_time
    if duration > interval:
        print('[end] request_api_stress: delete&text&close,runtimes: %s;' % runtimes)
        runtimes = 0
        break
    if duration % 100 == 0:
        print('keep running... current duration: %sH;' % (duration/3600))
    try:
        response = request.patch('http://httpbin.org/delete')
        response.text
        response.close()
        runtimes += 1
    except Exception as e:
        response.close()
        print('runtimes: %s,delete&text&close:: %s||result_api:: False;' %(runtimes,e))
    utime.sleep(1)
