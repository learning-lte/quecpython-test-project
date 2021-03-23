'''
@Author: Randy
@Date: 2020-11-16
@LastEditTime: 2020-11-16 13:57
@Description: API TEST FOR DEQUE
@FilePath: deque_append_popleft_api_test.py
'''
# 导入usocket模块
import ucollections
import urandom
import uos

flag = True # 初始值

for m in range(2):  # flag参数  溢出检测
    n = urandom.randint(1,100)  # maxlen
    dq = ucollections.deque((),n,m) # 创建deque对象
    for i in range(n+1):
        try:
            dq.append(uos.urandom(8).decode()) # 添加元素
        except Exception as e:
            if m == 1 and i == n and str(e) == 'full': # 判断是否为正常溢出
                pass
            else:
                print('deque append():[error]%s,result_api: False;'%e)
                flag = False
    else:
        if flag and m == 1:
            print('deque append(),result_api: True;')
        else:
            flag = True
    for i in range(n+1):
        try:
            dq.popleft() # 从deque的左侧移除并返回移除的数据
        except Exception as e:
            if i == n and str(e) == 'empty': # 判断异常原因是否符合期望
                pass
            else:
                print('deque popleft():[error]%s,result_api: False;'%e)
                flag = False
    else:
        if flag and m == 1:
            print('deque popleft(),result_api: True;')
        else:
            flag = True
