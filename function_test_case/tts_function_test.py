"""
@Author: Trent.zhang
@Date: 2021-01-15
@LastEditTime: 2021-01-15
@Description: Function test for TTS
@FilePath: tts_Function_Test.py
"""
"""
Demo for Function
改造测试用例时可参考此Demo
"""
import audio  # 导入的功能模块
import sys
import utime

ucs_01 = '006100620063006400650066006700680069006A006B006C006D006E006F0070007100720073007400750076007700780079007A004100420043004400450046004700480049004A004B004C004D004E004F0050005100520053005400550056005700580059005A'
ucs_02 = '00310032003300340035003600370038003900300039003800370036003500340033003200310030003100320033003400350036003700380039'
ucs_03 = '0030003100320033003400350036003700380039006100620063006400650066006700680069006A006B006C006D006E006F0070007100720073007400750076007700780079007A'
ucs_04 = '67AF85E480016811660F9E26FF0C665A996D67099C7C6709867EFF0C7A7A8C036B6A4F10897F74DCFF0C59159633897F4E0BFF0C4F604E11FF0C6CA14E8BFF0C6211778EFF0C54C854C8'
ucs_05 = '00310032003300340035003600370038FF0C67AF85E480016811660F9E26FF0C665A996D67099C7C6709867EFF0C7A7A8C030077006900660069897F74DCFF0C59159633897F4E0BFF0C4F604E11FF0C6CA14E8BFF0C6211778E002C54C854C8006100620063006400650066006700680069006A006B54C854C80030003900380037003600350034003300320031006E006F0070007100720073007400750076007700780079007A'
utf_01 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
utf_02 = '12345678909876543210123456789'
utf_03 = 'abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz0987654321'
utf_04 = '您将听到：枯藤老树昏鸦，晚饭有鱼有虾，空调歪伐西瓜，夕阳西下，你丑，没事，我瞎，哈哈'
utf_05 = '您将听到：12345678，枯藤老树昏鸦，晚饭有鱼有虾，空调wifi西瓜，夕阳西下，你丑，没事，我瞎,哈哈abcdefghijk哈哈0987654321nopqrstuvwxyz'


class TTSFunctionTest(object):
    """
    由于EC600S没有耳机插孔故测试使用话柄进行测试
    """
    def __init__(self):
        self.ucs_list = [ucs_01, ucs_02, ucs_03, ucs_04, ucs_05]
        self.utf_list = [utf_01, utf_02, utf_03, utf_04, utf_05]
        self.tts = audio.TTS(0)

    def TTS_01_001(self):  # 待执行函数
        '''
        :return: 话柄播放
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                tts = audio.TTS(0)
                for str in self.ucs_list:
                    a = tts.play(1, 0, 1, str)
                    utime.sleep(2)
                    tts.stop()
                    info.append(a)
                if info == [0, 0, 0, 0, 0]:
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

    def TTS_01_002(self):  # 待执行函数
        '''
        :return: 耳机播放
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                tts = audio.TTS(1)
                for str in self.ucs_list:
                    a = tts.play(1, 0, 1, str)
                    utime.sleep(2)
                    tts.stop()
                    info.append(a)
                if info == [0, 0, 0, 0, 0]:
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

    def TTS_01_003(self):  # 待执行函数
        '''
        :return: 喇叭播放
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                tts = audio.TTS(2)
                for str in self.ucs_list:
                    a = tts.play(1, 0, 1, str)
                    utime.sleep(2)
                    tts.stop()
                    info.append(a)
                if info == [0, 0, 0, 0, 0]:
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

    def TTS_02_001(self):  # 待执行函数
        '''
        :return: 话柄播放
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                tts = audio.TTS(0)
                for str in self.utf_list:
                    a = tts.play(1, 0, 2, str)
                    utime.sleep(2)
                    tts.stop()
                    info.append(a)
                if info == [0, 0, 0, 0, 0]:
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

    def TTS_02_002(self):  # 待执行函数
        '''
        :return: 耳机播放
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                tts = audio.TTS(1)
                for str in self.utf_list:
                    a = tts.play(1, 0, 2, str)
                    utime.sleep(2)
                    tts.stop()
                    info.append(a)
                if info == [0, 0, 0, 0, 0]:
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

    def TTS_02_003(self):  # 待执行函数
        '''
        :return: 喇叭播放
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                tts = audio.TTS(2)
                for str in self.utf_list:
                    a = tts.play(1, 0, 2, str)
                    utime.sleep(2)
                    tts.stop()
                    info.append(a)
                if info == [0, 0, 0, 0, 0]:
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

    def TTS_03_001(self):  # 待执行函数
        '''
        :return:未播放TTS查询播放状态
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = self.tts.getState()
                if info == 0:
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

    def TTS_03_002(self):  # 待执行函数
        '''
        :return:播放TTS查询播放状态
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                a = self.tts.play(1, 0, 2, utf_01)
                info.append(a)
                b = self.tts.getState()
                info.append(b)
                self.tts.stop()
                if info == [0, 1]:
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

    def TTS_04_001(self):  # 待执行函数
        '''
        :return:播放TTS查询播放状态
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                for i in range(5):
                    a = self.tts.play(1, 0, 2, utf_01)
                    info.append(a)
                    self.tts.stop()
                    utime.sleep(0.5)
                if info == [0, 0, 0, 0, 0]:
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

    def TTS_05_001(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = ''
                if info == '864430010001091':
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
        return info,result

    def TTS_05_002(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = ''
                if info == '864430010001091':
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

    def TTS_05_003(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = ''
                if info == '864430010001091':
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

    def TTS_05_004(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = ''
                if info == '864430010001091':
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

    def TTS_05_005(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = ''
                if info == '864430010001091':
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

    def TTS_06_001(self):  # 待执行函数
        '''
        :return:可打断模式
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                a = self.tts.play(0, 1, 2, utf_01)
                utime.sleep(0.5)
                b = self.tts.play(1, 1, 2, utf_01)
                utime.sleep(0.5)
                self.tts.stop()
                info.append(a)
                info.append(b)
                if info == [0, 0]:
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

    def TTS_06_002(self):  # 待执行函数
        '''
        :return:可打断模式
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                a = self.tts.play(2, 1, 2, utf_01)
                utime.sleep(0.5)
                b = self.tts.play(2, 1, 2, utf_01)
                utime.sleep(0.5)
                self.tts.stop()
                info.append(a)
                info.append(b)
                if info == [0, 0]:
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

    def TTS_06_003(self):  # 待执行函数
        '''
        :return:可打断模式
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                a = self.tts.play(4, 1, 2, utf_01)
                utime.sleep(0.5)
                b = self.tts.play(3, 1, 2, utf_01)
                self.tts.stop()
                utime.sleep(0.5)
                self.tts.stop()
                info.append(a)
                info.append(b)
                if info == [0, 1]:
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

    def TTS_06_004(self):  # 待执行函数
        '''
        :return:不可打断模式
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                a = self.tts.play(0, 0, 2, utf_01)
                utime.sleep(0.05)
                b = self.tts.play(1, 0, 2, utf_01)
                utime.sleep(1)
                self.tts.stop()
                utime.sleep(1)
                self.tts.stop()
                info.append(a)
                info.append(b)
                if info == [0, 1]:
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

    def TTS_06_005(self):  # 待执行函数
        '''
        :return:不可打断模式
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                a = self.tts.play(2, 0, 2, utf_01)
                b = self.tts.play(2, 0, 2, utf_01)
                utime.sleep(1)
                self.tts.stop()
                utime.sleep(1)
                self.tts.stop()
                info.append(a)
                info.append(b)
                if info == [0, 1]:
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

    def TTS_06_006(self):  # 待执行函数
        '''
        :return:不可打断模式
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                a = self.tts.play(3, 0, 2, utf_01)
                b = self.tts.play(4, 0, 2, utf_01)
                utime.sleep(1)
                self.tts.stop()
                utime.sleep(1)
                self.tts.stop()
                info.append(a)
                info.append(b)
                if info == [0, 1]:
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

    def TTS_06_007(self):  # 待执行函数
        '''
        :return:队列播放
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                a = self.tts.play(1, 0, 2, utf_01)
                b = self.tts.play(0, 1, 2, utf_01)
                c = self.tts.play(1, 0, 2, utf_01)
                d = self.tts.play(2, 0, 2, utf_01)
                e = self.tts.play(3, 0, 2, utf_01)
                f = self.tts.play(3, 1, 2, utf_01)
                for i in range(6):
                    utime.sleep(2)
                    self.tts.stop()
                info.append(a)
                info.append(b)
                if info == [0, 1]:
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

    def TTS_06_008(self):  # 待执行函数
        '''
        :return:可打断模式优先级为0播放队列
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                for i in range(10):
                    a = self.tts.play(0, 1, 2, utf_01)
                    utime.sleep(0.02)
                    info.append(a)
                utime.sleep(1)
                self.tts.stop()
                if 1 in info:
                    result = False
                else:
                    result = True
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def TTS_06_009(self):  # 待执行函数
        '''
        :return:可打断模式优先级为1播放队列
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                for i in range(11):
                    a = self.tts.play(1, 1, 2, utf_01)
                    utime.sleep(0.05)
                    info.append(a)
                utime.sleep(1)
                self.tts.stop()
                if 1 in info:
                    result = False
                else:
                    result = True
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def TTS_06_010(self):  # 待执行函数
        '''
        :return:可打断模式优先级为2播放队列
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                for i in range(11):
                    a = self.tts.play(2, 1, 2, utf_01)
                    utime.sleep(1)
                    info.append(a)
                utime.sleep(0.05)
                self.tts.stop()
                if 1 in info:
                    result = False
                else:
                    result = True
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def TTS_06_011(self):  # 待执行函数
        '''
        :return:可打断模式优先级为3播放队列
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                for i in range(11):
                    a = self.tts.play(3, 1, 2, utf_01)
                    utime.sleep(0.05)
                    info.append(a)
                utime.sleep(1)
                self.tts.stop()
                if 1 in info:
                    result = False
                else:
                    result = True
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def TTS_06_012(self):  # 待执行函数
        '''
        :return:可打断模式优先级为4播放队列
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                for i in range(11):
                    a = self.tts.play(4, 1, 2, utf_01)
                    utime.sleep(0.05)
                    info.append(a)
                utime.sleep(1)
                self.tts.stop()
                if 1 in info:
                    result = False
                else:
                    result = True
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def TTS_06_013(self):  # 待执行函数
        '''
        :return:不可打断模式优先级为0播放队列
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                while True:
                    a = self.tts.play(0, 0, 2, utf_01)
                    utime.sleep(0.05)
                    info.append(a)
                    if a == -2:
                        break
                    else:
                        pass
                utime.sleep(0.05)
                for i in info:
                    utime.sleep(1)
                    self.tts.stop()
                if -2 in info:
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

    def TTS_06_014(self):  # 待执行函数
        '''
        :return:不可打断模式优先级为1播放队列
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                while True:
                    a = self.tts.play(1, 0, 2, utf_01)
                    utime.sleep(0.05)
                    info.append(a)
                    if a == -2:
                        break
                    else:
                        pass
                utime.sleep(0.05)
                for i in info:
                    utime.sleep(1)
                    self.tts.stop()
                if -2 in info:
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

    def TTS_06_015(self):  # 待执行函数
        '''
        :return:不可打断模式优先级为2播放队列
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                while True:
                    a = self.tts.play(2, 0, 2, utf_01)
                    utime.sleep(0.05)
                    info.append(a)
                    if a == -2:
                        break
                    else:
                        pass
                utime.sleep(0.05)
                for i in info:
                    utime.sleep(1)
                    self.tts.stop()
                utime.sleep(0.01)
                if -2 in info:
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

    def TTS_06_016(self):  # 待执行函数
        '''
        :return:不可打断模式优先级为3播放队列
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                while True:
                    a = self.tts.play(3, 0, 2, utf_01)
                    utime.sleep(0.05)
                    info.append(a)
                    if a == -2:
                        break
                    else:
                        pass
                utime.sleep(0.05)
                for i in info:
                    utime.sleep(1)
                    self.tts.stop()
                if -2 in info:
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

    def TTS_06_017(self):  # 待执行函数
        '''
        :return:不可打断模式优先级为4播放队列
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                while True:
                    a = self.tts.play(4, 0, 2, utf_01)
                    utime.sleep(0.05)
                    info.append(a)
                    if a == -2:
                        break
                    else:
                        pass
                utime.sleep(0.05)
                for i in info:
                    utime.sleep(1)
                    self.tts.stop()
                if -2 in info:
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

    def TTS_08_001(self):  # 待执行函数
        '''
        :return:建立多线程mqtt+uart+TTS稳定性
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []

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

    def TTS_09_01(self):  # 待执行函数
        '''
        :return:建立多线程mqtt+uart+TTS稳定性
        '''
        runflag = 1

        if runflag:
            try:
                # --------------valid code--------------
                def tts_cb(event):
                    if event == 2:
                        print('TTS-play start.')
                    if event == 3:
                        print('TTS-play stop.')
                    elif event == 4:
                        print('TTS-play finish.')
                info = self.tts.setCallback(tts_cb)
                if info == 0:
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

    def TTS_09_02(self):  # 待执行函数
        '''
        :return:建立多线程mqtt+uart+TTS稳定性
        '''
        runflag = 1

        if runflag:
            try:
                # --------------valid code--------------
                info = self.tts.play(1, 0, 2, 'QuecPython')
                utime.sleep(5)
                self.tts.stop()
                if info == 0:
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

    def TTS_09_03(self):  # 待执行函数
        '''
        :return:建立多线程mqtt+uart+TTS稳定性
        '''
        runflag = 1

        if runflag:
            try:
                # --------------valid code--------------
                info = self.tts.play(1, 0, 2, 'QuecPython')
                utime.sleep(0.5)
                self.tts.stop()
                if info == 0:
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

    def method(self): # 必备函数
        '''
        返回类中除内置方法外的所有方法名
        :return:
        '''
        return (list(filter(lambda m: not m.startswith("__") and not m.endswith("__") and callable(getattr(self, m)),
                            dir(self))))

    def run(self): # 必备函数
        '''
        主执行函数
        :return:
        '''
        case_list = []
        for i in self.method(): # 遍历类中方法
            if 'TTS' in i:  # 注意修改此为testcase名称
                case_list.append(i)  # 筛选出testcase
        case_list.sort()  # testcase排序
        for i in case_list:
            a,b = getattr(self, i)()  # 遍历执行case
            print('%s:: %s||result_case:: %s;' % (i, a, b))  # 输出执行log供外部框架解析
            utime.sleep(3)


if __name__ == '__main__':
    TTSFunctionTest().run()
