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
    screen =ImageGrab.grab(area_grab)
    screen =cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
    res = cv2.matchTemplate(screen,target,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
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
        screen =cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
        res = cv2.matchTemplate(screen,target,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val >0.9:
            pyautogui.click(x=(area_grab[0] +max_loc[0] +img_size[0]//2) ,y=(area_grab[1] +max_loc[1] +img_size[1]//2))
            break

class myConf(object):
    def __init__(self):
        cf = configparser.ConfigParser()
        cf.read(r"rsc\conf")
        self.coor_login_telcom =self.loadcontent(cf ,'login' ,'coor_login_telcom')
        self.coor_login_notelcom =self.loadcontent(cf ,'login' ,'coor_login_notelcom')
        self.coor_login_closefirstpage =self.loadcontent(cf ,'login' ,'coor_login_closefirstpage')

        self.coor_login_checkie =self.loadcontent(cf ,'login' ,'coor_login_checkie')
        self.coor_login_agree =self.loadcontent(cf ,'login' ,'coor_login_agree')
        self.coor_login_orderid =self.loadcontent(cf ,'login' ,'coor_login_orderid')
        self.coor_login_orderpass =self.loadcontent(cf ,'login' ,'coor_login_orderpass')
        self.coor_login_code =self.loadcontent(cf ,'login' ,'coor_login_code')
        self.area_login_code =self.loadcontent(cf ,'login' ,'area_login_code')
        self.coor_login_longin =self.loadcontent(cf ,'login' ,'coor_login_longin')
        self.check_login_against =cf.get('login' ,'check_login_against')
        self.coor_login_confirmagainst =self.loadcontent(cf ,'login' ,'coor_login_confirmagainst')
        self.coor_login_identy =self.loadcontent(cf ,'login' ,'coor_login_identy')
        self.coor_login_againstcode =self.loadcontent(cf ,'login' ,'coor_login_againstcode')
        self.area_login_againstcode =self.loadcontent(cf ,'login' ,'area_login_againstcode')
        self.coor_login_againstlongin =self.loadcontent(cf ,'login' ,'coor_login_againstlongin')

        self.coor_main_kickconfirm =self.loadcontent(cf ,'main' ,'coor_main_kickconfirm')
        self.check_main_kick =cf.get('main' ,'check_main_kick')
        self.coor_main_firststep1 =self.loadcontent(cf ,'main' ,'coor_main_firststep1')
        self.coor_main_firststep2 =self.loadcontent(cf ,'main' ,'coor_main_firststep2')
        self.coor_main_firststepconfirm =self.loadcontent(cf ,'main' ,'coor_main_firststepconfirm')
        self.area_main_firststepcode =self.loadcontent(cf ,'main' ,'area_main_firststepcode')
        self.coor_main_firststepcode =self.loadcontent(cf ,'main' ,'coor_main_firststepcode')
        self.coor_main_firststepcodeconfirm =self.loadcontent(cf ,'main' ,'coor_main_firststepcodeconfirm')
        self.check_main_confirm =cf.get('main' ,'check_main_confirm')

        self.coor_main_seconddeltaprice =self.loadcontent(cf ,'main' ,'coor_main_seconddeltaprice')
        self.coor_main_secondaddprice =self.loadcontent(cf ,'main' ,'coor_main_secondaddprice')
        self.coor_main_secondconfirmprice =self.loadcontent(cf ,'main' ,'coor_main_secondconfirmprice')
        self.check_main_secondcodehere =cf.get('main' ,'check_main_secondcodehere')
        self.area_main_secondstepcode =self.loadcontent(cf ,'main' ,'area_main_secondstepcode')
        self.coor_main_secondstepcode =self.loadcontent(cf ,'main' ,'coor_main_secondstepcode')
        self.coor_main_secondstepcodeconfirm =self.loadcontent(cf ,'main' ,'coor_main_secondstepcodeconfirm')

    def loadcontent(self ,cf ,opt ,sub):
        content =cf.get(opt ,sub)
        return json.loads(content)




# theConf = myConf()
# time.sleep(5)
# print(check_img(theConf.check_main_kick))