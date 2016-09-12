import cv2 ,requests
from PIL import ImageGrab ,Image
import numpy as np
import pyautogui,datetime,time ,threading

p_timeTarget =r'C:\Users\guo\Desktop\thePrj\alltobid\25.png'
code_url =r'C:\Users\guo\Desktop\thePrj\alltobid\code.png'
code_url1 =r'C:\Users\guo\Desktop\thePrj\alltobid\code1.png'
s_checkTime =(500 ,200 ,900 ,600)
first_bTime ,first_eTime ,first_dPrice =38 ,45 ,'500'
second_bTime ,second_eTime ,second_dPrice =47 ,54 ,'700'
s_grabCode =(970 ,380 ,1190 ,545)
c_deltaPrice =(1190 ,380)
c_addPrice =(1315 ,375)
c_confirmPrice =(1310 ,485)
c_typeCode =(1250 ,480)
c_confirmCode =(1065 ,565)


method = eval('cv2.TM_CCOEFF_NORMED')
begin_x =800
begin_y =100
timeTarget =Image.open(p_timeTarget)
timeTarget =cv2.cvtColor(np.array(timeTarget, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
timeStamp =0
firstCodeDict ={}
secondCodeDict ={}
lock = threading.Lock()

def addTime():
    global timeStamp
    while 1:
        time.sleep(1)
        timeStamp +=1

def checkTime():
    # print(datetime.datetime.now())
    global timeTarget
    global timeStamp
    screen =ImageGrab.grab(s_checkTime)
    screen =cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
    res = cv2.matchTemplate(screen,timeTarget,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val >0.99:
        timeStamp =25
        t =threading.Thread(target=addTime)
        t.start()
    # print(datetime.datetime.now())

def click_img(url ,d=0):
    # print(datetime.datetime.now())
    target =Image.open(url)
    img_size =target.size
    target =cv2.cvtColor(np.array(target, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
    screen =ImageGrab.grab((begin_x ,begin_y ,1400 ,800))
    screen =cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
    res = cv2.matchTemplate(screen,target,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if d:
        pyautogui.doubleClick(x=(begin_x +max_loc[0] +img_size[0]//2) ,y=(begin_y +max_loc[1] +img_size[1]//2) ,button='left')
    else:
        pyautogui.click(x=(begin_x +max_loc[0] +img_size[0]//2) ,y=(begin_y +max_loc[1] +img_size[1]//2) ,button='left')
    # print(datetime.datetime.now())

def check_img(url):
    target =Image.open(url)
    target =cv2.cvtColor(np.array(target, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
    screen =ImageGrab.grab((begin_x ,begin_y ,1400 ,800))
    screen =cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
    res = cv2.matchTemplate(screen,target,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val >0.9:
        return max_loc
    else:
        return 0

def getDamatu(theCodeDict):
    dmt=td.DamatuApi("slientcraft","inwcwizard")
    theCode =dmt.decode(code_url,200)
    # print(theCode)
    lock.acquire()
    try:
        # global theCodeDict
        if theCode in theCodeDict:
            theCodeDict[theCode] +=1
        else:
            theCodeDict[theCode] =1
    finally:
        lock.release()

def getLianzhong(theCodeDict):
    url = 'http://bbb4.hyslt.com/api.php?mod=php&act=upload'
    files = {'upload': open(code_url, 'rb')}
    data = {'user_name': 'slientcraft', 'user_pw': 'inwcwizard', 'yzmtype_mark': '19'}
    r = requests.post(url, files=files, data=data)
    theCode =r.json()['data']['val']
    # print(theCode)
    lock.acquire()
    try:
        # global theCodeDict
        if theCode in theCodeDict:
            theCodeDict[theCode] +=1
        else:
            theCodeDict[theCode] =1
    finally:
        lock.release()

def deCode( theCodeDict ,t_Time):
    # global theCodeDict
    global timeStamp
    for i in range(20):
        t =threading.Thread(target=getDamatu, args=(theCodeDict,))
        t.start()
    for i in range(20):
        t =threading.Thread(target=getLianzhong, args=(theCodeDict,))
        t.start()
    print(t_Time-timeStamp)
    time.sleep(t_Time -timeStamp)

    ret =0
    lock.acquire()
    try:
        print(theCodeDict)
        if 'ERROR' in theCodeDict:
            theCodeDict.pop('ERROR')
        if 'IERROR' in theCodeDict:
            theCodeDict.pop('IERROR')
        if -304 in theCodeDict:
            theCodeDict.pop(-304)
        if len(theCodeDict) ==0:
            lock.release()
            return '0'
        theCodeDict = sorted(theCodeDict.items(), key=lambda dic: dic[1])
        print(theCodeDict[-1][0])
        ret =theCodeDict[-1][0]
    finally:
        lock.release()
    return ret

def grabCode():
    target =Image.open(r'C:\Users\guo\Desktop\thePrj\alltobid\tip_end.png')
    tip_loc =check_img(r'C:\Users\guo\Desktop\thePrj\alltobid\tip_begin.png')
    left ,top=begin_x +tip_loc[0] ,begin_y +tip_loc[1]
    tip_loc =check_img(r'C:\Users\guo\Desktop\thePrj\alltobid\tip_end.png')
    right ,bottom =begin_x +tip_loc[0] +target.width ,begin_y +tip_loc[1] +target.height
    tip =ImageGrab.grab((left ,top ,right ,bottom))
    tip =tip.resize((tip.width *2,90))
    code =ImageGrab.grab((1230 ,420 ,1230 +135 ,420 +90))
    code =code.resize((code.width *2 ,code.height *2) ,Image.ANTIALIAS)
    ret =Image.new('RGB', (tip.width +code.width, code.height), (255, 255, 255))
    # ret =Image.new('L', (tip.width +code.width, code.height), 255)
    ret.paste(tip ,(0 ,(ret.height -tip.height) //2 ,tip.width ,(ret.height -tip.height) //2 +tip.height))
    ret.paste(code ,(tip.width,0,ret.width,ret.height))
    ret.save(code_url, "PNG")

def grabCodeNew():
    code =ImageGrab.grab(s_grabCode)
    code.save(code_url, "PNG")

def beginWork():
    pyautogui.click(c_deltaPrice[0] ,c_deltaPrice[1] ,button='left')
    pyautogui.typewrite(first_dPrice)

def firstWork():
    pyautogui.doubleClick(c_deltaPrice[0] ,c_deltaPrice[1] ,button='left')
    pyautogui.typewrite(first_dPrice)
    time.sleep(0.1)
    pyautogui.click(c_addPrice[0] ,c_addPrice[1] ,button='left')
    time.sleep(0.1)
    pyautogui.click(c_confirmPrice[0] ,c_confirmPrice[1] ,button='left')
    time.sleep(first_eTime -timeStamp)
    click_img(r"C:\Users\guo\Desktop\thePrj\alltobid\confirm_code_button.png")
    # print(timeStamp)
    time.sleep(0.5)
    while 1:
        if check_img(r"C:\Users\guo\Desktop\thePrj\alltobid\confirm_code_button.png"):
            click_img(r"C:\Users\guo\Desktop\thePrj\alltobid\confirm_code_button.png")
            return


def secondWork():
    print(timeStamp)
    global second_dPrice
    sleepTime =second_eTime -timeStamp
    if  timeStamp ==49:
        second_dPrice ='600'
    if timeStamp >=50:
        second_dPrice ='500'
        sleepTime =5
    print(sleepTime)
    pyautogui.doubleClick(c_deltaPrice[0] ,c_deltaPrice[1] ,button='left')
    pyautogui.typewrite(second_dPrice)
    time.sleep(0.1)
    pyautogui.click(c_addPrice[0] ,c_addPrice[1] ,button='left')
    time.sleep(0.1)
    pyautogui.click(c_confirmPrice[0] ,c_confirmPrice[1] ,button='left')
    time.sleep(sleepTime)
    click_img(r"C:\Users\guo\Desktop\thePrj\alltobid\confirm_code_button.png")
    code =ImageGrab.grab((558 ,424 ,857 ,518))
    code.save(code_url, "PNG")

#main
pyautogui.click(x=260 ,y=1060 ,button='left')
#beginWork()

while 1:
    #找点对齐时间
    if not timeStamp:
        checkTime()
    #检查有没被T出
    #...
    #到策略点干活
    if timeStamp ==first_bTime:
        firstWork()
    if timeStamp >=second_bTime:
        secondWork()
        break
    time.sleep(0.3)


