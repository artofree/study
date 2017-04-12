import inspect ,ctypes ,configparser ,json ,sys
from PIL import ImageGrab, Image
import numpy as np
import cv2 ,pyautogui, datetime, time, threading, requests
from io import BytesIO as StringIO

area_grab =[500 ,60 ,1400 ,750]
method = eval('cv2.TM_CCOEFF_NORMED')

def _async_raise(tid, exctype):
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

import os ,zipfile
def zipDir(dirPath, zipPath):
    zipf = zipfile.ZipFile(zipPath , mode='w')
    lenDirPath = len(dirPath)
    for root, _ , files in os.walk(dirPath):
        for file in files:
            filePath = os.path.join(root, file)
            zipf.write(filePath , filePath[lenDirPath :] )
    zipf.close()

def unzip(source ,target):
    source_zip=source
    target_dir=target
    myzip=zipfile.ZipFile(source_zip)
    myfilelist=myzip.namelist()
    for name in myfilelist:
        f_handle=open(os.path.join(target_dir, name),"wb")
        f_handle.write(myzip.read(name))
        f_handle.close()
    myzip.close()

def check_img(url):
    target =Image.open(url)
    target =cv2.cvtColor(np.array(target, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
    # try:
    #     screen = ImageGrab.grab(area_grab)
    # # except (OSError ,MemoryError):
    # except OSError:
    #     return 0
    screen =ImageGrab.grab(area_grab)
    screen =cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
    res = cv2.matchTemplate(screen,target,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # print(max_val)
    if max_val >0.9:
        # return max_loc
        return 1
    else:
        return 0

def click_img(url):
    target =Image.open(url)
    img_size =target.size
    target =cv2.cvtColor(np.array(target, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
    while 1:
        screen =ImageGrab.grab(area_grab)
        # try:
        #     screen = ImageGrab.grab(area_grab)
        # # except (OSError, MemoryError):
        # except OSError:
        #     continue
        screen =cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
        res = cv2.matchTemplate(screen,target,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val >0.9:
            xc ,yc=area_grab[0] +max_loc[0] +img_size[0]//2 ,(area_grab[1] +max_loc[1] +img_size[1]//2)
            pyautogui.click(xc ,yc)
            break


class myConf(object):
    def __init__(self):
        # self.coor_login_telcom =[880 ,390]
        self.coor_login_telcom =[857 ,480]
        self.coor_login_notelcom =[1050 ,390]
        self.coor_login_closefirstpage =[810 ,40]

        self.coor_login_checkie =[1250 ,745]
        self.coor_login_agree =[1200 ,740]
        self.coor_login_orderid =[1120 ,270]
        self.coor_login_orderpass =[1120 ,325]
        self.coor_login_code =[1120 ,380]
        self.area_login_code =[1200 ,360 ,1320 ,395]
        self.coor_login_longin =[1150 ,450]
        #如果卡这里可能是下面两个配置任一出错
        self.check_login_against =r'rsc\check_login_against.png'
        self.coor_login_confirmagainst =[1125 ,610]
        self.coor_login_identy =[1120 ,380]
        self.coor_login_againstcode =[1120 ,435]
        self.area_login_againstcode =[1200 ,415 ,1320 ,450]
        self.coor_login_againstlongin =[1150 ,501]

        #如果卡这里可能是下面两个配置任一出错
        self.check_main_kick =r'rsc\check_main_kick.png'
        self.coor_main_kickconfirm =[1150 ,555]

        self.coor_main_firststep1 =[1200 ,385]
        self.coor_main_firststep2 =[1200 ,445]
        self.coor_main_firststepconfirm =[1310 ,440]
        self.area_main_firststepcode =[960 ,410 ,1150 ,540]
        self.coor_main_firststepcode =[1250 ,490]
        self.coor_main_firststepcodeconfirm =[1066 ,570]
        #错误则第一次出价结果框不消失
        self.check_main_confirm =r'rsc\check_main_confirm.png'

        #错误看不到价格
        self.coor_main_secondtestaddprice =[1160 ,450]
        #错误则验证码框不消失
        self.coor_main_secondetestcancel =[1245 ,567]

        #错误不会出验证码对话框
        self.coor_main_seconddeltaprice =[1190, 380]
        #错误看不到将出的价格
        self.coor_main_secondaddprice =[1315, 375]
        #错误不会出验证码对话框
        self.coor_main_secondconfirmprice =[1310, 485]
        #错误则不会有code.png
        self.check_main_secondcodehere =r'rsc\check_main_secondcodehere.png'
        self.check_main_refreshcode =r'rsc\check_main_refreshcode.png'
        #错误则code.png内容不对，需要重置区域坐标
        self.area_main_secondstepcode =[960, 400, 1200, 545]
        #错误则验证码框光标不闪
        self.coor_main_secondstepcode =[1250, 480]
        #错误则不出价
        self.coor_main_secondstepcodeconfirm =[1065, 570]




    # def loadcontent(self ,cf ,opt ,sub):
    #     content =cf.get(opt ,sub)
    #     return json.loads(content)




# theConf = myConf()
# time.sleep(5)
# print(check_img(theConf.check_main_kick))