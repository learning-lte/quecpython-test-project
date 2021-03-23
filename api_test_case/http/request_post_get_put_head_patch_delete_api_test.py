# coding: utf-8
'''
@Author: Trent.Zhang
@Date: 2020-09-23
@LastEditTime: 2020-09-23
@Description: example for module request
@FilePath: request_post_get_put_head_patch_delete_api_test.py
'''
import request
import utime
import _thread


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
                "request.post('http://httpbin.org/get')",
                "request.post('http://httpbin.org/get').text",
                "request.post('http://httpbin.org/get').content",
                "request.post('http://httpbin.org/get').json",
                "request.get('https://myssl.com')",
                "request.get('https://myssl.com').text",
                "request.get('https://myssl.com').content",
                "request.get('https://myssl.com').json",
                "request.put('http://httpbin.org/get')",
                "request.put('http://httpbin.org/get').text",
                "request.put('http://httpbin.org/get').content",
                "request.put('http://httpbin.org/get').json",
                "request.head('https://myssl.com')",
                "request.head('https://myssl.com').text",
                "request.head('https://myssl.com').content",
                "request.head('https://myssl.com').json",
                "request.patch('https://myssl.com')",
                "request.patch('https://myssl.com').text",
                "request.patch('https://myssl.com').content",
                "request.patch('https://myssl.com').json",
                "request.delete('https://myssl.com')",
                "request.delete('https://myssl.com').text",
                "request.delete('https://myssl.com').content",
                "request.delete('https://myssl.com').json",
        ]
        for i in list:
            api_test(i)
            print(_thread.get_heap_size())
