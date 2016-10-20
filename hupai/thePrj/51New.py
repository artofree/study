import theLib.damatu as td
import theLib.lib as tl
from PIL import ImageGrab, Image
import numpy as np
import cv2 ,pyautogui, datetime, time, threading, requests
from io import BytesIO as StringIO

checkTimeTarget =1
servUrl ='http://139.219.238.37:8000/'
# servUrl ='http://192.168.0.106:8000/'
p_timeTarget = r'C:\Users\guo\Desktop\thePrj\51\29_23.png'
s_checkTime = (500, 200, 900, 600)
first_bTime, first_eTime, first_dPrice = 38, 45, '600'
second_bTime ,second_eTime, second_dPrice = 47 ,55, '700'
s_grabCode = (970, 380, 1190, 545)
c_deltaPrice = (1190, 380)
c_addPrice = (1315, 375)
c_confirmPrice = (1310, 485)
c_typeCode = (1250, 480)
c_confirmCode = (1065, 565)

method = eval('cv2.TM_CCOEFF_NORMED')
begin_x = 800
begin_y = 100
timeTarget = Image.open(p_timeTarget)
timeTarget = cv2.cvtColor(np.array(timeTarget, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
timeStamp = 0
lock = threading.Lock()

def checkTime():
    global timeTarget
    while 1:
        screen = ImageGrab.grab(s_checkTime)
        screen = cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
        res = cv2.matchTemplate(screen, timeTarget, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val > 0.99:
            requests.get(url=servUrl +'setTimeStamp')
            return
        time.sleep(0.2)
if checkTimeTarget:
    t = threading.Thread(target=checkTime)
    t.start()

#与服务对时，如果服务器时间大于0
def getTimeStamp():
    global timeStamp
    while 1:
        timeStamp =float(requests.get(url=servUrl +'getTimeStamp').text)
        timeStamp =round(timeStamp ,2)
        time.sleep(0.2)
t = threading.Thread(target=getTimeStamp)
t.start()

def click_img(url, d=0):
    # print(datetime.datetime.now())
    target = Image.open(url)
    img_size = target.size
    target = cv2.cvtColor(np.array(target, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
    screen = ImageGrab.grab((begin_x, begin_y, 1400, 800))
    screen = cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
    res = cv2.matchTemplate(screen, target, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if d:
        pyautogui.doubleClick(x=(begin_x + max_loc[0] + img_size[0] // 2), y=(begin_y + max_loc[1] + img_size[1] // 2),
                              button='left')
    else:
        pyautogui.click(x=(begin_x + max_loc[0] + img_size[0] // 2), y=(begin_y + max_loc[1] + img_size[1] // 2),
                        button='left')
        # print(datetime.datetime.now())

def check_img(url):
    target = Image.open(url)
    target = cv2.cvtColor(np.array(target, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
    screen = ImageGrab.grab((begin_x, begin_y, 1400, 800))
    screen = cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
    res = cv2.matchTemplate(screen, target, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val > 0.9:
        return max_loc
    else:
        return 0


def getDamatu(theCodeDict):
    dmt = td.DamatuApi("slientcraft", "inwcwizard")
    theCode = dmt.decode(code_url, 200)
    # print(theCode)
    lock.acquire()
    try:
        # global theCodeDict
        if theCode in theCodeDict:
            theCodeDict[theCode] += 1
        else:
            theCodeDict[theCode] = 1
    finally:
        lock.release()


def deCode(theCodeDict, t_Time):
    # global theCodeDict
    global timeStamp
    for i in range(10):
        t = threading.Thread(target=getDamatu, args=(theCodeDict,))
        t.start()
    print(t_Time - timeStamp)
    time.sleep(t_Time - timeStamp)

    ret = 0
    lock.acquire()
    try:
        print(theCodeDict)
        if 'ERROR' in theCodeDict:
            theCodeDict.pop('ERROR')
        if 'IERROR' in theCodeDict:
            theCodeDict.pop('IERROR')
        if -304 in theCodeDict:
            theCodeDict.pop(-304)
        if len(theCodeDict) == 0:
            lock.release()
            return '0'
        theCodeDict = sorted(theCodeDict.items(), key=lambda dic: dic[1])
        print(theCodeDict[-1][0])
        ret = theCodeDict[-1][0]
    finally:
        lock.release()
    return ret

def grabCodeNew():
    print(datetime.datetime.now())
    code = ImageGrab.grab(s_grabCode)
    print(datetime.datetime.now())
    code.save(code_url, "PNG")
    print(datetime.datetime.now())


def beginWork():
    pyautogui.click(c_deltaPrice[0], c_deltaPrice[1], button='left')
    pyautogui.typewrite(first_dPrice)


def firstWork():
    pyautogui.click(c_deltaPrice[0], c_deltaPrice[1], button='left')
    pyautogui.typewrite(first_dPrice)
    time.sleep(0.1)
    pyautogui.click(c_addPrice[0], c_addPrice[1], button='left')
    time.sleep(0.1)
    pyautogui.click(c_confirmPrice[0], c_confirmPrice[1], button='left')
    time.sleep(0.1)
    while 1:
        if check_img(r"C:\Users\guo\Desktop\thePrj\51\tip_begin.png"):
            time.sleep(0.5)
            if check_img(r"C:\Users\guo\Desktop\thePrj\51\refresh_code_button.png"):
                click_img(r"C:\Users\guo\Desktop\thePrj\51\refresh_code_button.png")
            else:
                # print(datetime.datetime.now())
                print(timeStamp)
                grabCodeNew()
                pyautogui.click(c_typeCode[0], c_typeCode[1], button='left')
                theCode = deCode(firstCodeDict, first_eTime)
                pyautogui.typewrite(theCode)
                click_img(r"C:\Users\guo\Desktop\thePrj\51\confirm_code_button.png")
                time.sleep(0.3)
                while 1:
                    if check_img(r"C:\Users\guo\Desktop\thePrj\51\confirm_code_button.png"):
                        click_img(r"C:\Users\guo\Desktop\thePrj\51\confirm_code_button.png")
                        return


def secondWork():
    pyautogui.doubleClick(c_deltaPrice[0], c_deltaPrice[1], button='left')
    pyautogui.typewrite(second_dPrice)
    time.sleep(0.1)
    pyautogui.click(c_addPrice[0], c_addPrice[1], button='left')
    time.sleep(0.1)
    pyautogui.click(c_confirmPrice[0], c_confirmPrice[1], button='left')
    while 1:
        if check_img(r"C:\Users\guo\Desktop\thePrj\51\tip_begin.png"):
            time.sleep(0.5)
            if check_img(r"C:\Users\guo\Desktop\thePrj\51\refresh_code_button.png"):
                click_img(r"C:\Users\guo\Desktop\thePrj\51\refresh_code_button.png")
            else:
                # print(timeStamp)
                # grabCodeNew()
                code = ImageGrab.grab(s_grabCode)
                catch =StringIO()
                code.save(catch ,'PNG')
                pyautogui.click(c_typeCode[0], c_typeCode[1], button='left')
                # theCode = deCode(secondCodeDict, second_eTime)
                payload = {'idt': '0001'}
                files = {'file': catch.getvalue()}
                requests.post(servUrl +'uploadPic', files=files ,data=payload)
                print(datetime.datetime.now())
                time.sleep(second_eTime -timeStamp)
                theCode =requests.get(servUrl +'getCode' ,payload)
                pyautogui.typewrite(theCode.text)
                click_img(r"C:\Users\guo\Desktop\thePrj\51\confirm_code_button.png")
                break


# main
pyautogui.click(x=260, y=1060, button='left')
pyautogui.click(x=630, y=640, button='left')
pyautogui.click(x=1148, y=42, button='left')
time.sleep(100)
# beginWork()

while 1:
    # 检查有没被T出
    # ...
    # 到策略点干活
    if timeStamp > second_bTime:
        # firstWork()
        secondWork()
        break
    time.sleep(0.1)
