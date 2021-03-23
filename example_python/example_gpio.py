# GPIO使用示例

from machine import Pin

/*
* 参数1：gpio号 （0~127）
* 参数2：direction （0：输入模式  1：输出模式）
* 参数3：pull  （0：PULL_DISABLE  1：PULL_PU  2：PULL_PD）
* 参数4：level  （0：low  1：high）
*/
gpio1 = Pin(1, 1, 0, 0)

gpio1.on() # 当为gpio输出模式时，设置gpio1 输出高
gpio1.value() # 获取gpio的当前高低状态
>>> 1

gpio1.off() # 当为gpio输出模式时，设置gpio1 输出低
gpio1.value()
>>> 0