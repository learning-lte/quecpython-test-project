# -*- coding: UTF-8 -*-
'''
@Author: Randy
@Date: 2020-12-24
@LastEditTime: 2020-12-24
@Description: API test for sms
@FilePath: sms_send_rev_query_delete_api_test.py
'''
import sms
import utime

cellnumber = '13156590859' # 手机号

def cb(args):
     flag = args[0]
     if flag == 0x1001:   # args[0]为0x1001时，有效参数及意义如下
         print('### msglen={},msg={};'.format(args[2], args[1]))
     elif flag == 0x1002: # args[0]为0x1002时，有效参数及意义如下
        print('$$$ numtype={:0>3d},numplan={:0>4d},len={},digits={};'.format(args[1],args[2],args[3],args[4]))
     elif flag == 0x1003:  # args[0]为0x1003时，有效参数及意义如下
        print('type={}, storage={}, index={}'.format(args[1], args[2], args[3]))

def common_test():
    api_test('sms.getCenterAddr()')
    a = sms.getCenterAddr()
    api_test("sms.setCenterAddr('123456789')")
    re = sms.setCenterAddr(a.replace('+86',''))
    if re != 0:
        print('sms.setCenterAddr:: %s||result_api:: False;'%re)
    else:
        print('sms.setCenterAddr:: %s||result_api:: True;' % re)
    api_test('sms.setCallback(cb)')

def api_test(api):
    result1 = 'error'
    try:
        result1 = eval(api)
    except Exception as err:
        print('[error]'+str(err)+';')
        result1 = '[error]%s'%(str(err))
    if result1 != ('error' and -1):
        result2 = True
    else:
        result2 = False
    print('%s:: %s||result_api:: %s;'%(api, result1, result2))

if __name__ == '__main__':
    common_test()
    list = [
            "sms.setSaveLoc('SM', 'SM', 'ME')",
            "sms.getSaveLoc()",
            "sms.sendTextMsg('%s', 'send text msg by USC2 mode.这是包含中文字符的短信！', 'UCS2')"%cellnumber,
            "sms.sendTextMsg('+86%s', 'send text msg by GSM mode.', 'gsm')"%cellnumber,
            "sms.sendPduMsg('%s', 'send pdu msg by GSM mode.', 'GSM')"%cellnumber,
            "sms.sendPduMsg('+86%s', 'send pdu msg by UCS2 mode.这是包含中文字符的短信！', 'UcS2')"%cellnumber,
            "sms.getMsgNums()",
            "sms.searchPduMsg(0)",
            "sms.searchTextMsg(0)",
            # "sms.getPduLength(sms.searchPduMsg(0))",  # 2021.2.19 api文档已屏蔽此接口，不再测试
            # "sms.setRcvDealmode(0)",
            # "sms.setRcvDealmode(1)",
            # "sms.setRcvDealmode(2)",
            # "sms.setRcvDealmode(3)",
    ]

    for i in list:
        api_test(i)
        utime.sleep(0.5)