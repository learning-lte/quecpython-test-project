"""
@Author: Trent.Zhang
@Date: 2021-01-12
@LastEditTime: 2021-01-12
@Description: Function test for demo
@FilePath: Demo_Function_Test.py
"""
"""
Demo for Function
改造测试用例时可参考此Demo
"""
import request  # 导入的功能模块
import sys
import utime
import ujson

class RequestFunction():

    def __init__(self):
        pass

    def HTTP_01_001(self):
        """
        设置GET的URL(HTTP)带url请求
        :return:
        """
        runflag = 1
        if runflag:
            try:
                info = []
                # --------------valid code--------------
                url = "http://httpbin.org/get"
                response = request.get(url)
                a = response.content.__next__()
                info.append(a)
                response.close()
                response = request.get(url)
                b = response.text.__next__()
                info.append(b)
                response.close()
                response = request.get(url)
                c = response.json()
                info.append(c)
                response.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = str(e)
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_01_002(self):
        """
        设置GET的URL(HTTP)带url，data请求
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                url = "http://httpbin.org/get"
                data = {"key1": "value1", "key2": "value2", "key3": "value3"}
                response = request.get(url, data=ujson.dumps(data))
                a = response.content.__next__()
                info.append(a)
                response.close()
                response = request.get(url)
                b = response.text.__next__()
                info.append(b)
                response.close()
                response = request.get(url)
                c = response.json()
                info.append(c)
                response.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_01_003(self):
        """
        设置GET的URL(HTTP)带url，data，headers请求
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                url = "http://httpbin.org/get"
                data = {"key1": "value1", "key2": "value2", "key3": "value3"}
                headers = {'X-Amzn-Trace-Id': 'Root=1-5f811c4d-54273f913ab3dc0b177b1c8f', 'Host': 'httpbin.org'}
                response = request.get(url, data=ujson.dumps(data),headers=headers)
                a = response.content.__next__()
                info.append(a)
                response.close()
                response = request.get(url)
                b = response.text.__next__()
                info.append(b)
                response.close()
                response = request.get(url)
                c = response.json()
                info.append(c)
                response.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_01_004(self):
        """
        设置GET的URL(HTTPS)
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                url = "https://myssl.com"
                data = {"key1": "value1", "key2": "value2", "key3": "value3"}
                headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
                response = request.get(url, headers=headers)
                a = response.content.__next__()
                info.append(a)
                response.close()
                response = request.get(url)
                b = response.text.__next__()
                info.append(b)
                response.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_01_005(self):
        """
        设置GET的URL(HTTPS)
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                url = "https://myssl.com"
                response = request.get(url)
                response.close()
                info = response.content.__next__()
                if info:
                    result = False
                else:
                    result = True
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = True
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_02_001(self):
        """
        设置POST的URL(HTTP)带url请求
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                url = "http://httpbin.org/get"
                response = request.post(url)
                a = response.content.__next__()
                info.append(a)
                response.close()
                response = request.post(url)
                b = response.text.__next__()
                info.append(b)
                response.close()
                response = request.post(url)
                c = response.json()
                info.append(c)
                response.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = str(e)
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_02_002(self):
        """
        设置POST的URL(HTTP)带url，data请求
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                url = "http://httpbin.org/post"
                data = {"key1": "value1", "key2": "value2", "key3": "value3"}
                response = request.post(url, data=ujson.dumps(data))
                a = response.content.__next__()
                info.append(a)
                response.close()
                response = request.post(url)
                b = response.text.__next__()
                info.append(b)
                response.close()
                response = request.post(url)
                c = response.json()
                info.append(c)
                response.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_02_003(self):
        """
        设置POST的URL(HTTP)带url，data，headers请求
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                url = "http://httpbin.org/post"
                data = {"key1": "value1", "key2": "value2", "key3": "value3"}
                headers = {'X-Amzn-Trace-Id': 'Root=1-5f811c4d-54273f913ab3dc0b177b1c8f', 'Host': 'httpbin.org'}
                response = request.post(url, data=ujson.dumps(data), headers=headers)
                a = response.content.__next__()
                info.append(a)
                response.json()
                response = request.post(url)
                b = response.text.__next__()
                info.append(b)
                response.json()
                response = request.post(url)
                c = response.json()
                info.append(c)
                response.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_02_004(self):
        """
        设置POST的URL(HTTPS)
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                url = "https://myssl.com"
                data = {"key1": "value1", "key2": "value2", "key3": "value3"}
                headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
                response = request.post(url, headers=headers)
                a = response.content.__next__()
                response.close()
                response = request.post(url)
                b = response.text.__next__()
                response.close()
                info.append(a)
                info.append(b)
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_02_005(self):
        """
        设置POST的URL(HTTPS)
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                url = "https://myssl.com"
                response = request.post(url)
                response.close()
                info = response.content.__next__()
                if info:
                    result = False
                else:
                    result = True
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = True
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_03_001(self):
        """
        设置PUT的URL(HTTP)带url请求
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                url = "http://httpbin.org/get"
                response = request.put(url)
                a = response.content.__next__()
                response.close()
                response = request.put(url)
                b = response.text.__next__()
                response.close()
                response = request.put(url)
                c = response.json()
                response.close()
                info.append(a)
                info.append(b)
                info.append(c)
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = str(e)
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_03_002(self):
        """
        设置PUT的URL(HTTP)带url，data请求
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                url = "http://httpbin.org/put"
                data = {"key1": "value1", "key2": "value2", "key3": "value3"}
                response = request.put(url, data=ujson.dumps(data))
                a = response.content.__next__()
                response.close()
                response = request.put(url)
                b = response.text.__next__()
                response.close()
                response = request.put(url)
                c = response.json()
                response.close()
                info.append(a)
                info.append(b)
                info.append(c)
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_03_003(self):
        """
        设置PUT的URL(HTTP)带url，data，headers请求
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                url = "http://httpbin.org/put"
                data = {"key1": "value1", "key2": "value2", "key3": "value3"}
                headers = {'X-Amzn-Trace-Id': 'Root=1-5f811c4d-54273f913ab3dc0b177b1c8f', 'Host': 'httpbin.org'}
                response = request.put(url, data=ujson.dumps(data), headers=headers)
                a = response.content.__next__()
                response.close()
                response = request.put(url)
                b = response.text.__next__()
                response.close()
                response = request.put(url)
                c = response.json()
                response.close()
                info.append(a)
                info.append(b)
                info.append(c)
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_03_004(self):
        """
        设置POST的URL(HTTPS)
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                url = "https://myssl.com"
                data = {"key1": "value1", "key2": "value2", "key3": "value3"}
                headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
                response = request.put(url, headers=headers)
                a = response.content.__next__()
                response.close()
                response = request.put(url)
                b = response.text.__next__()
                response.close()
                info.append(a)
                info.append(b)
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_03_005(self):
        """
        设置PUT的URL(HTTPS)
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                url = "https://myssl.com"
                response = request.put(url)
                response.close()
                info = response.content.__next__()
                if info:
                    result = False
                else:
                    result = True
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = True
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_04_001(self):
        """
        设置HEAD的URL(HTTP)带url请求
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                url = "http://httpbin.org/head"
                response = request.head(url)
                a = response.headers
                response.close()
                info = a
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = str(e)
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_04_002(self):
        """
        设置HEAD的URL(HTTP)带url，data请求
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                url = "http://httpbin.org/put"
                data = {"key1": "value1", "key2": "value2", "key3": "value3"}
                response = request.head(url, data=ujson.dumps(data))
                a = response.headers
                response.close()
                info = a
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_04_003(self):
        """
        设置HEAD的URL(HTTP)带url，data，headers请求
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                url = "http://httpbin.org/head"
                data = {"key1": "value1", "key2": "value2", "key3": "value3"}
                headers = {'X-Amzn-Trace-Id': 'Root=1-5f811c4d-54273f913ab3dc0b177b1c8f', 'Host': 'httpbin.org'}
                response = request.head(url, data=ujson.dumps(data), headers=headers)
                a = response.headers
                response.close()
                info = a
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_04_004(self):
        """
        设置HEAD的URL(HTTPS)
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                url = "https://myssl.com"
                data = {"key1": "value1", "key2": "value2", "key3": "value3"}
                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
                response = request.head(url, data=ujson.dumps(data), headers=headers)
                a = response.headers
                response.close()
                info = a
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_04_005(self):
        """
        设置HRAD的URL(HTTPS)
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                url = "https://myssl.com"
                response = request.head(url)
                response.close()
                utime.sleep(0.5)
                info = response.headers
                if info:
                    result = False
                else:
                    result = True
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = True
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_05_001(self):
        """
        设置PACH的URL(HTTP)带url请求
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                url = "http://httpbin.org/pach"
                response = request.pach(url)
                a = response.content.__next__()
                response.close()
                response = request.patch(url)
                b = response.text.__next__()
                response.close()
                response = request.pach(url)
                c = response.json()
                response.close()
                info.append(a)
                info.append(b)
                info.append(c)
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = str(e)
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_05_002(self):
        """
        设置PACH的URL(HTTP)带url，data请求
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                url = "http://httpbin.org/pach"
                data = {"key1": "value1", "key2": "value2", "key3": "value3"}
                response = request.patch(url, data=ujson.dumps(data))
                a = response.content.__next__()
                response.close()
                response = request.pach(url)
                b = response.text.__next__()
                response.close()
                response = request.pach(url)
                c = response.json()
                response.close()
                info.append(a)
                info.append(b)
                info.append(c)
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_05_003(self):
        """
        设置PACH的URL(HTTP)带url，data，headers请求
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                url = "http://httpbin.org/pach"
                data = {"key1": "value1", "key2": "value2", "key3": "value3"}
                headers = {'X-Amzn-Trace-Id': 'Root=1-5f811c4d-54273f913ab3dc0b177b1c8f', 'Host': 'httpbin.org'}
                response = request.patch(url, data=ujson.dumps(data), headers=headers)
                a = response.content.__next__()
                response.close()
                response = request.pach(url)
                b = response.text.__next__()
                response.close()
                response = request.pach(url)
                c = response.json()
                response.close()
                info.append(a)
                info.append(b)
                info.append(c)
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_05_004(self):
        """
        设置PACH的URL(HTTPS)
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                url = "https://myssl.com"
                data = {"key1": "value1", "key2": "value2", "key3": "value3"}
                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
                response = request.patch(url, data=ujson.dumps(data), headers=headers)
                a = response.content.__next__()
                response.close()
                response = request.pach(url)
                b = response.text.__next__()
                response.close()
                info.append(a)
                info.append(b)
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_05_005(self):
        """
        设置PUT的URL(HTTPS)
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                url = "https://myssl.com"
                response = request.patch(url)
                response.close()
                info = response.content.__next__()
                if info:
                    result = False
                else:
                    result = True
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = True
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_06_001(self):
        """
        设置DELETE的URL(HTTP)带url请求
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                url = "http://httpbin.org/delete"
                response = request.delete(url)
                a = response.content.__next__()
                response.close()
                response = request.delete(url)
                b = response.text.__next__()
                response.close()
                response = request.delete(url)
                c = response.json()
                response.close()
                info.append(a)
                info.append(b)
                info.append(c)
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = str(e)
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_06_002(self):
        """
        设置DELETE的URL(HTTP)带url，data请求
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                url = "http://httpbin.org/delete"
                data = {"key1": "value1", "key2": "value2", "key3": "value3"}
                response = request.delete(url, data=ujson.dumps(data))
                a = response.content.__next__()
                response.close()
                response = request.delete(url)
                b = response.text.__next__()
                response.close()
                response = request.delete(url)
                c = response.json()
                response.close()
                info.append(a)
                info.append(b)
                info.append(c)
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_06_003(self):
        """
        设置DELETE的URL(HTTP)带url，data，headers请求
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                url = "http://httpbin.org/delete"
                data = {"key1": "value1", "key2": "value2", "key3": "value3"}
                headers = {'X-Amzn-Trace-Id': 'Root=1-5f811c4d-54273f913ab3dc0b177b1c8f', 'Host': 'httpbin.org'}
                response = request.delete(url, data=ujson.dumps(data), headers=headers)
                a = response.content.__next__()
                response.close()
                response = request.delete(url)
                b = response.text.__next__()
                response.close()
                response = request.delete(url)
                c = response.json()
                response.close()
                info.append(a)
                info.append(b)
                info.append(c)
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_06_004(self):
        """
        设置DELETE的URL(HTTPS)
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                url = "https://myssl.com"
                data = {"key1": "value1", "key2": "value2", "key3": "value3"}
                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
                response = request.delete(url, data=ujson.dumps(data), headers=headers)
                a = response.content.__next__()
                response.close()
                response = request.delete(url)
                b = response.text.__next__()
                response.close()
                info.append(a)
                info.append(b)
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_06_005(self):
        """
        设置DELETE的URL(HTTPS)
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                url = "https://myssl.com"
                response = request.delete(url)
                response.close()
                info = response.content.__next__()
                if info:
                    result = False
                else:
                    result = True
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = True
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_07_001(self):
        """
        端口号地址访问(单向认证ip+端口号）
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                url = 'https://14.215.177.38:443'
                response = request.get(url)
                info = response.content.__next__()
                response.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_07_002(self):
        """
        ip+端口号+字符串的地址（单项认证）
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                url = 'https://220.180.239.212:8301/trent/'
                response = request.get(url)
                info = response.content.__next__()
                response.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_07_003(self):
        """
        get请求域名+1024字节网站
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                url = 'https://220.180.239.212:8301/trent/'
                response = request.get(url)
                info = response.content.__next__()
                response.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_07_004(self):
        """
        get请求域名+汉字的地址
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                url = 'https://220.180.239.212:8301/trent/'
                response = request.get(url)
                info = response.content.__next__()
                response.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_07_005(self):
        """
        get请求 域名+汉字+特殊字符的地址
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                url = 'https://220.180.239.212:8301/trent/'
                response = request.get(url)
                info = response.content.__next__()
                response.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_07_006(self):
        """
        post请求域名+超过1024字节网站
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                url = 'https://220.180.239.212:8301/trent/'
                response = request.get(url)
                info = response.content.__next__()
                response.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_07_007(self):
        """
        get请求IPV6的域名地址
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                url ="0:0:0:0:0:FFFF:0ED7:B126"
                response = request.get(url)
                info = response.content.__next__()
                response.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_07_008(self):
        """
        错误的url地址访问失败
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                url = "0:0:0:0:0:FFFF:0ED7:B126"
                response = request.get(url)
                info = response.content.__next__()
                response.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_07_009(self):
        """
        get请求 域名+用户名+密码的地址
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                url = "0:0:0:0:0:FFFF:0ED7:B126"
                response = request.get(url)
                info = response.content.__next__()
                response.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_08_001(self):
        """
        建立HTTPS双向认证GET请求
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                url = "0:0:0:0:0:FFFF:0ED7:B126"
                response = request.get(url)
                info = response.content.__next__()
                response.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_08_002(self):
        """
        建立HTTPS双向认证POST请求
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                url = "0:0:0:0:0:FFFF:0ED7:B126"
                response = request.get(url)
                info = response.content.__next__()
                response.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_08_003(self):
        """
        SSL支持的加密算法13种证书全测
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                url = "0:0:0:0:0:FFFF:0ED7:B126"
                response = request.get(url)
                info = response.content.__next__()
                response.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def HTTP_09_001(self):
        """
        反复打开关闭HTTP连接
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                url = "0:0:0:0:0:FFFF:0ED7:B126"
                response = request.get(url)
                info = response.content.__next__()
                response.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def method(self):  # 必备函数
        '''
        返回类中除内置方法外的所有方法名
        :return:
        '''
        return (list(filter(lambda m: not m.startswith("__") and not m.endswith("__") and callable(getattr(self, m)),
                            dir(self))))

    def run(self):  # 必备函数
        '''
        主执行函数
        :return:
        '''
        case_list = []
        for i in self.method(): # 遍历类中方法
            if 'HTTP' in i:  # 注意修改此为testcase名称
                case_list.append(i)  # 筛选出testcase
        case_list.sort()  # testcase排序
        for i in case_list:
            a, b = getattr(self, i)()  # 遍历执行case
            print('%s:: %s||result_case:: %s;' % (i, a, b))  # 输出执行log供外部框架解析
            utime.sleep(3)


if __name__ == '__main__':
    RequestFunction().run()
