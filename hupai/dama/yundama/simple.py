import sys
import os
from ctypes import *

YDMApi = windll.LoadLibrary('yundamaAPI')
appId = 1  # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
appKey = c_char_p(b'22cc5376925e9387a23cf797cb9ba745')  # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
username = c_char_p(b'slientcraft')
password = c_char_p(b'inwcwizard')
codetype = 6101
result = c_char_p(b"                              ")
timeout = 60
filename = c_char_p(b'C:\\Users\\artof_000\\Pictures\\1.png')
captchaId = YDMApi.YDM_EasyDecodeByPath(username, password, appId, appKey, filename, codetype, timeout, result)
error = 0
str = ''
try:
    str = result._objects.decode("utf-8")
except:
    error = 1
print("识别结果：%s" % str)
