#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
-------------------------------------------------------------------------------
脚本名称:  common_function
需求来源:
    主要定义一些公用的函数
测试目的：
    实现一些小功能
修改记录:
    初始版本V1.0 2019/8/25 loren.jia
脚本逻辑:
    无
脚本统计:
    无
测试前准备:
    无
-------------------------------------------------------------------------------
'''

import sys
import datetime
import re
import winsound
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
import wrapper_library_ec100y.common_log_queue_dict as common_log_queue_dict
import zipfile
import pika

info = common_log_queue_dict.DictObject().info()
setting = common_log_queue_dict.DictObject().setting()
debug = True

def duration(time_per, time_now):
    '''
    计算时间差值
    :param time_per: 开始时间
    :param time_now: 结束时间
    :return: 时间差值 s
    '''
    try:
        time_start = datetime.datetime.strptime(str(time_per).strip(),
                                                '%Y-%m-%d %H:%M:%S.%f')
    except Exception as e:
        print("异常信息time_start:", e)
        time_start = datetime.datetime.strptime(str(time_per).strip(),
                                                '%Y-%m-%d %H:%M:%S')
    try:
        time_end = datetime.datetime.strptime(str(time_now).strip(),
                                              '%Y-%m-%d %H:%M:%S.%f')
    except Exception as e:
        print("异常信息time_end:", e)
        time_end = datetime.datetime.strptime(str(time_now).strip(),
                                              '%Y-%m-%d %H:%M:%S')
    data_str = time_end - time_start
    if re.compile("(\d+) day").findall(str(data_str)):
        days = ','.join(re.compile("(\d+) day").findall(str(data_str)))
    else:
        days = 0
    if re.compile("\d+:\d+:\d+.\d+").findall(str(data_str)):
        hours = ','.join(re.compile("(\d+):\d+:\d+.\d+").findall(str(data_str)))
        minutes = ','.join(re.compile("\d+:(\d+):\d+.\d+").findall(str(data_str)))
        seconds = ','.join(re.compile("\d+:\d+:(\d+).\d+").findall(str(data_str)))
        microseconds = ','.join(re.compile("\d+:\d+:\d+.(\d+)").findall(str(data_str)))
    elif re.compile("\d+:\d+:\d+").findall(str(data_str)):
        hours = ','.join(re.compile("(\d+):\d+:\d+").findall(str(data_str)))
        minutes = ','.join(re.compile("\d+:(\d+):\d+").findall(str(data_str)))
        seconds = ','.join(re.compile("\d+:\d+:(\d+)").findall(str(data_str)))
        microseconds = 0
    else:
        hours = 0
        minutes = 0
        seconds = 0
        microseconds = 0
    dur = int(days) * 86400 +\
          int(hours) * 3600 +\
          int(minutes) * 60 +\
          int(seconds) + \
          int(microseconds) / 1000000
    return dur

def time_format():
    '''
    格式化时间
    :return: 返回一个格式化的时间 如2019_06_27_09_24_30
    '''
    time_str = str(datetime.datetime.now())[0:19]
    time = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    # 根据字符串本身的格式进行转换
    time = time.strftime('%Y_%m_%d_%H_%M_%S')
    #装换成需要的格式2019_06_27_09_24_30
    return time

def sound_Beep():
    '''
    beep蜂鸣器
    :return:  可用于警报
    '''
    sound_list = (800, 1600)
    for i in sound_list:
        duration = 500  # millisecond
        freq = i
        winsound.Beep(freq, duration)
    return

def send_mail(Script,info_data):
    '''
    发送邮件
    :param info_data:  字典类参数
    :return:  发送邮件给收件人
    '''
    
    myqueue = common_log_queue_dict.SignalObject()
    try:
        headr = "<th><strong></strong></th>"
        notes = "<td>SUM/AVG</td>"
        notes2 = '<td bgcolor="#a7a7a7">FAIL_TIMES</td>'
        Runtimes = common_log_queue_dict.DictObject().parameter()['Runtimes']
        dict = common_log_queue_dict.DictObject().statistics()
        for i in dict.keys():
            try:
                headr += '<th><strong>' + i + '</strong></th>'
                notes += ' <td>' + str(dict[i][0]) + '</td>'
                if re.search('Runtime',str(dict[i][1]),re.I|re.M):
                    notes2 += '<td bgcolor="#838362">' + str(dict[i][1]) + '</td>'
                else:
                    notes2 += '<td bgcolor="#a7a7a7">' + str(dict[i][1]) + '</td>'
            except:
                pass
        
        myqueue.abnormal_log_msg().put("Send email notification executor ")
        my_sender = '1532857309@qq.com'  # 发件人邮箱账号
        my_pass = 'zbgnlmrmmhchiaib'  # 发件人邮箱密码
        receiver =setting["module"]['executor'] # 收件人邮箱账号
        if not str(receiver).upper().endswith("QUECTEL.COM"):
            print(str(receiver).upper())
            return
        
        myqueue.abnormal_log_msg().put("executor:%s" % receiver)
        msg = MIMEMultipart('mixed')  # 定义邮件类型
        msg['Subject'] = '【%s-压力测试通知(测试版本：%s)-%.18s】'\
                         %(Script,info['Revision'],
                           str(datetime.datetime.now()))  ##邮件主题
        msg['From'] = formataddr(["压力测试通知",my_sender])  ##发送人
        msg['To'] = receiver  ##接收人
        html = """
        <html>
            <head></head>
            <style type="text/css">
                table {
                    font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
                    width: 100%;
                    border-collapse: collapse;
                }
                td, th {
                    font-size: 1em;
                    border: 1px solid #5B4A42;
                    padding: 3px 7px 2px 7px;
                }
    
                th {
                    font-size: 1.1em;
                    text-align: center;
                    padding-top: 5px;
                    padding-bottom: 4px;
                    background-color: #24A9E1;
                    color: #ffffff;
                }
                table.hovertable {
                    font-family: verdana,arial,sans-serif;
                    font-size:11px;
                    color:#333333;
                    border-width: 1px;
                    border-color: #999999;
                    border-collapse: collapse;
                }
                table.hovertable th {
                    background-color:#c3dde0;
                    border-width: 1px;
                    padding: 8px;
                    border-style: solid;
                    border-color: #a9c6c9;
                }
                table.hovertable tr {
                    background-color:#d4e3e5;
                }
                table.hovertable td {
                    border-width: 1px;
                    padding: 8px;
                    border-style: solid;
                    border-color: #a9c6c9;
                }
            </style>
            <body >
                <h2>您在进行的压力返回一个结果：""" +str(info_data)+ """</h2>
                <br>
                <br>
                <tr>
                    <td>模块信息如下：</td>
                </tr>
                <table>
                    <tr>
                        <th>Revision</th>
                        <td>"""+info['Revision']+"""</td>
                    </tr>
                    <tr>
                        <th>SubEdition</th>
                        <td>"""+info['SubEdition']+"""</td>
                    </tr>
                    <tr>
                        <th>IMEI</th>
                        <td>"""+info['IMEI']+"""</td>
                    </tr>
                    <tr>
                        <th>IMSI</th>
                        <td>"""+info['IMSI']+"""</td>
                    </tr>
                    <tr>
                        <th>QCCID</th>
                        <td>"""+info['QCCID']+"""</td>
                    </tr>
                    
                </table>
                <table>
                     <tr>
                        <th>UART_PORT</th>
                        <th>AT_PORT</th>
                        <th>Funcs</th>
                        <th>RUNTIME</th>
                        <th>START_TIME</th>
                        <th>END_TIME</th>
                        <th>DURATION</th>
                    </tr>
                    <tr>
                        <td>"""+setting["module"]['uart_port']+"""</td>
                        <td>"""+setting["module"]['usb_port']+"""</td>
                        <td>"""+Script+"""</td>
                        <td>"""+str(Runtimes)+"""</td>
                        <td>"""+str(info['Start_time'])[:19]+"""</td>
                        <td>"""+str(info['End_time'])[:19]+"""</td>
                        <td>"""+str(duration(info['Start_time'],
                                             info['End_time']))+"""</td>
                    </tr>
                </table>
                <br>
                <br>
                <tr>
                    <td>数据统计：</td>
                </tr>
                <table>
                    <tr>""" + headr + """</tr>
                    <tr> """ + str(notes) + """</tr>
                    <tr>""" + str(notes2) + """</tr>
                </table>
                <br>
                <hr>
                <h3 style="color: firebrick">温馨提示:
                本邮件是自动发出的，勿需回复！</h3>
            </body>
        </html>
                """
    
        
        bbox = (0, 0, 1920, 1080)
        # im = ImageGrab.grab(bbox)
        # im.save('as.png')
        # 构造图片链接
        # sendimagefile = open(r'as.png', 'rb').read()
        # image = MIMEImage(sendimagefile)
        # image.add_header('Content-ID', '<image1>')
        # msg.attach(image)
        text_html = MIMEText(html, 'html', 'utf-8')
        msg.attach(text_html)
        # 构造附件
        # path = os.path.split(os.path.realpath(__file__))[0]
        # filenames = os.listdir(path+"\\log")
        # base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # conf_PATH = base_dir + "/log"
        # filenames = os.listdir(conf_PATH)
        # for filename in filenames:
        #     if re.search('.log', filename):
        #         sendfile = open(conf_PATH + "/" + filename, 'rb').read()
        #         text_att = MIMEText(sendfile, 'base64', 'utf-8')
        #         text_att["Content-Type"] = 'application/octet-stream'
        #         text_att.add_header('Content-Disposition', 'attachment', filename=filename)
        #         msg.attach(text_att)
        try:
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)
            # 发件人邮箱中的SMTP服务器，端口是25
            server.login(my_sender, my_pass)
            # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender, [receiver, ], msg.as_string())
            # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()
            # 关闭连接
            myqueue.abnormal_log_msg().put("Email 发送成功")
        except Exception:
            pass
    except Exception as e:
        print(e)
    return

def mkdir( path):
    """
    创建文件夹
    :param path: 文件夹路径
    :return:
    """
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
        pass
    return

def my_print(*args, sep=' ', end='\n', file=None):
    """
    重新print方法
    :param args: 参数
    :param sep: 开始
    :param end: 结束为
    :param file: 文件
    :return:
    """
    base_dir = os.getcwd()
    base_dir = str(base_dir)+'\\debuglog\\'

    log_file = base_dir +"log.log"
    if os.path.isfile(log_file):
        if os.path.getsize(log_file) >1024*1024*100:
            os.remove(log_file)
    else:
        mkdir(base_dir)

    line = sys._getframe().f_back.f_lineno
    # file_name = sys._getframe(1).f_code.co_filename
    file_name = str(sys._getframe(1).f_code.co_filename).rsplit("/")[-1]
    file_name = file_name.rsplit("\\")[-1]
    data = ''
    try:
        if len(args) == 1:
            data = args[0]
        if len(args) > 1 :
            for i in range(len(args)) :
                if i == 0 :
                    data = str(args[i])
                else:
                    data += ','+str(args[i])

        if debug:
            sys.stdout.write(f'[{file_name}:{line}] '
                             f'[{str(datetime.datetime.now())[:23]}] '
                             f'\033[0;94m{data}\033[0m\n')

        with open(log_file,'a+') as f:
            try:
                f.write(f'[{file_name}:{line}] [{str(datetime.datetime.now())[:23]}] {data}\n')
            except:
                pass
    except :
        with open(log_file,'a+') as f:
            f.write(f'[{file_name}:{line}] [{str(datetime.datetime.now())[:23]}] {data}{args}\n')

    return


class zip:
    def get_zip(self,files,zip_name):
        zp=zipfile.ZipFile(zip_name,'w', zipfile.ZIP_DEFLATED)
        for file in files:
            zp.write(file)
            zp.close()
        # print('压缩完成')

def getVersion():
    credentials = pika.PlainCredentials('mq', '123456')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='10.66.91.99', port=9174, virtual_host='/', credentials=credentials))
    channel = connection.channel()
    # 申明消息队列，消息在这个队列传递，如果不存在，则创建队列
    channel.queue_declare(queue='python-version', durable=True)
    version = []
    # 定义一个回调函数来处理消息队列中的消息，这里是打印出来
    # 对消息进行处理
    def messagehandle(msg):
        # tmp = readjson()
        # print(msg)
        version.append(msg.decode())
    def callback(ch, method, properties, body):
        ch.basic_ack(delivery_tag=method.delivery_tag)

        messagehandle(body)
        channel.stop_consuming()
    # 告诉rabbitmq，用callback来接收消息
    channel.basic_consume('python-version', callback)

    # 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理
    channel.start_consuming()
    return version[0]

# print(getVersion())