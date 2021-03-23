# PWM使用示例

from misc import PWM

/*
* 参数1：gpio号 （6 、7 、10 、11 、31 、32）//仅这几个gpio具有pwm功能
* 参数2：high_time //pwm 高电平时间
* 参数3：cycle_time //pwm 整个周期时间
*/

pwm = PWM(31, 100, 200)  # 初始化一个pwm对象

pwm.open()  # 使能pwm输出
pwm.close()  # 关闭pwm输出