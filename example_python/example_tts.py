'''
@Author: Pawn
@Date: 2020-08-19
@Description: example for module TTS
@FilePath: example_tts.py
'''
from audio import TTS

/*
* 参数1：device （0：话筒，1：耳机，2：喇叭）
*/
tts = TTS(1)
tts.init() //仅需调用一次即可
/*
* 参数1：模式 （1：UNICODE16(Size end conversion)  2：UTF-8  3：UNICODE16(Don't convert)）
* 参数2：数据字符串 （带播放字符串）
*/	
tts.play(2, "quectel")
