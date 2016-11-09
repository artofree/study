import myLib, damatu, sys, socket
from PIL import ImageGrab, Image
import numpy as np
import cv2, pyautogui, datetime, time, threading, requests
from io import BytesIO as StringIO
import configparser,os

decodeThreadList = []
theCodeDict = {}
second_bTime, second_eTime, second_dPrice = 48, 55, '700'
servUrl = 'http://139.219.238.37:8000/'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
code_url = os.path.join(os.path.join(BASE_DIR, 'rsc'), 'code.png')
theConf = myLib.myConf()
timeStamp = 0
lock = threading.Lock()

s_checkTime = (500, 200, 900, 600)
timeTarget = Image.open(r'rsc\29_23.png')
timeTarget = cv2.cvtColor(np.array(timeTarget, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)

###第一常量，版本号信息
vcf = configparser.ConfigParser()
vcf.read(r"rsc\conf")
curVersion = vcf.get('main', 'version')

###第二常量，用hostname获得拍牌人信息
hostName = socket.gethostname()
orderid, orderpass, identy = requests.get(servUrl + 'getOrderInfo', {'hostname': 'newguo'}).text.split('-')

###第三常量，取自mainConf
cf = configparser.ConfigParser()
cf.read(r"C:\Users\guo\Desktop\mainConf")
curStep =cf.get('main', 'step')
isMainClient =cf.get('main', 'mainclient')
handMade =cf.get('main', 'handmade')


def getCode():
    global theCodeDict
    dmt = damatu.DamatuApi("slientcraft", "inwcwizard")
    theCode = dmt.decode(code_url, 200)
    lock.acquire()
    try:
        if theCode in theCodeDict:
            theCodeDict[theCode] += 1
        else:
            theCodeDict[theCode] = 1
    finally:
        lock.release()
    time.sleep(20)


def deCode(area_code, lim=0):
    global theCodeDict
    global decodeThreadList
    code = ImageGrab.grab(area_code)
    code.save(code_url, "PNG")
    time.sleep(1)
    for i in range(10):
        t = threading.Thread(target=getCode)
        t.start()
        decodeThreadList.append(t)
    time.sleep(10)
    if 'ERROR' in theCodeDict:
        theCodeDict.pop('ERROR')
    if 'IERROR' in theCodeDict:
        theCodeDict.pop('IERROR')

    tmpList = []
    if lim:
        for key in theCodeDict:
            if len(key) != lim:
                tmpList.append(key)
        for key in tmpList:
            theCodeDict.pop(key)

    theCodeDict = sorted(theCodeDict.items(), key=lambda dic: dic[1])
    for t in decodeThreadList:
        myLib.stop_thread(t)
    decodeThreadList = []
    theCode = theCodeDict[-1][0]
    theCodeDict = {}
    return theCode

def checkVersion():
    while 1:
        if requests.get(servUrl + 'getVersion').text != curVersion:
            r = requests.get(servUrl + 'getVersionContent', stream=True)
            with open(r"C:\Users\guo\Desktop\archive.zip", 'wb') as fd:
                for chunk in r.iter_content(10240):
                    fd.write(chunk)
            time.sleep(1)
            myLib.unzip(r"C:\Users\guo\Desktop\archive.zip", '.')
            time.sleep(1)
            cmd = 'taskkill /F /IM iexplore.exe'
            os.system(cmd)
            time.sleep(1)
            python = sys.executable
            os.execl(python, python, *sys.argv)
        time.sleep(10)

def checkTime():
    global timeTarget
    while 1:
        screen = ImageGrab.grab(s_checkTime)
        screen = cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
        res = cv2.matchTemplate(screen, timeTarget, myLib.method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val > 0.99:
            requests.get(url=servUrl +'setTimeStamp')
            return
        time.sleep(0.2)

def getTimeStamp():
    global timeStamp
    while 1:
        timeStamp = float(requests.get(url=servUrl + 'getTimeStamp').text)
        timeStamp = round(timeStamp, 2)
        time.sleep(0.2)


def against():
    while 1:
        if myLib.check_img(theConf.check_main_kick):
            pyautogui.click(theConf.coor_login_orderid)
            time.sleep(1)
            login()
        time.sleep(10)


def preLogin():
    pyautogui.click(x=260, y=1060)
    time.sleep(5)
    pyautogui.click(theConf.coor_login_telcom)
    time.sleep(1)
    pyautogui.click(theConf.coor_login_closefirstpage)
    time.sleep(1)


def againstLogin():
    pyautogui.click(theConf.coor_login_orderid)
    time.sleep(1)
    pyautogui.typewrite(orderid)
    time.sleep(1)
    pyautogui.click(theConf.coor_login_orderpass)
    time.sleep(1)
    pyautogui.typewrite(orderpass)
    time.sleep(1)
    pyautogui.click(theConf.coor_login_identy)
    time.sleep(1)
    pyautogui.typewrite(identy)
    time.sleep(1)
    pyautogui.click(theConf.coor_login_againstcode)
    time.sleep(1)
    pyautogui.typewrite(deCode(theConf.area_login_againstcode))
    time.sleep(1)
    pyautogui.click(theConf.coor_login_againstlongin)
    time.sleep(5)


def login():
    pyautogui.click(theConf.coor_login_checkie)
    time.sleep(3)
    pyautogui.click(theConf.coor_login_agree)
    time.sleep(3)
    pyautogui.click(theConf.coor_login_orderid)
    time.sleep(1)
    pyautogui.typewrite(orderid)
    time.sleep(1)
    pyautogui.click(theConf.coor_login_orderpass)
    time.sleep(1)
    pyautogui.typewrite(orderpass)
    time.sleep(1)
    pyautogui.click(theConf.coor_login_code)
    time.sleep(1)
    pyautogui.typewrite(deCode(theConf.area_login_code))
    time.sleep(1)
    pyautogui.click(theConf.coor_login_longin)
    time.sleep(5)
    if myLib.check_img(theConf.check_login_against):
        pyautogui.click(theConf.coor_login_confirmagainst)
        time.sleep(1)
        againstLogin()


def firstStep(price):
    pyautogui.click(theConf.coor_main_firststep1)
    time.sleep(1)
    pyautogui.typewrite(price)
    time.sleep(1)
    pyautogui.click(theConf.coor_main_firststep2)
    time.sleep(1)
    pyautogui.typewrite(price)
    time.sleep(1)
    pyautogui.click(theConf.coor_main_firststepconfirm)
    time.sleep(3)
    pyautogui.click(theConf.coor_main_firststepcode)
    time.sleep(1)
    pyautogui.typewrite(deCode(theConf.area_main_firststepcode, 4))
    time.sleep(1)
    pyautogui.click(theConf.coor_main_firststepcodeconfirm)
    time.sleep(5)
    myLib.click_img(theConf.check_main_confirm)
    time.sleep(1)


def secondPrice():
    pyautogui.doubleClick(theConf.coor_main_seconddeltaprice)
    pyautogui.typewrite(second_dPrice)
    time.sleep(0.1)
    pyautogui.click(theConf.coor_main_secondaddprice)
    time.sleep(0.1)
    pyautogui.click(theConf.coor_main_secondconfirmprice)
    while 1:
        if myLib.check_img(theConf.check_main_secondcodehere):
            code = ImageGrab.grab(theConf.area_main_secondstepcode)
            catch = StringIO()
            code.save(catch, 'PNG')
            pyautogui.click(theConf.coor_main_secondstepcode)
            payload = {'idt': identy}
            files = {'file': catch.getvalue()}
            requests.post(servUrl + 'uploadPic', files=files, data=payload)
            print(datetime.datetime.now())
            time.sleep(second_eTime - timeStamp)
            theCode = requests.get(servUrl + 'getCode', payload)
            pyautogui.typewrite(theCode.text)
            pyautogui.click(theConf.coor_main_secondstepcodeconfirm)
            break


def secondStep():
    while 1:
        if timeStamp > second_bTime:
            secondPrice()
            break
    time.sleep(0.1)


####################################################################################
###主线程

def mainWork():
    print('everything begin....')
    ###如果主终端，则启动对时线程：
    if isMainClient =='1':
        checkTimeTrhead = threading.Thread(target=checkTime)
        checkTimeTrhead.start()
    ###线程0-检查版本改变
    checkVersionThread = threading.Thread(target=checkVersion)
    checkVersionThread.start()
    ###线程1-常规终端只开获得时间戳
    timeStampThread = threading.Thread(target=getTimeStamp)
    timeStampThread.start()
    ###线程2-防t
    againstThread = threading.Thread(target=against)
    againstThread.start()
    ###非手动版么自动登陆：
    if handMade =='0':
        preLogin()
        login()
        ###若在第一阶段出价并记录已出价
        if curStep == '0':
            firstStep('100')
            firstStep('200')
            cf.set('main', 'step', '1')
            cf.write(open(r"C:\Users\guo\Desktop\step", "w"))
    ###线程3-第二阶段是个线程
    secondStepThread =threading.Thread(target=secondStep)
    secondStepThread.start()


if __name__=='__main__':
    mainWork()

# mainWork()











# def beginWork():
#     t = threading.Thread(target=mainWork)
#     t.start()
#     threadList.append(t)
#
#
# def endWork():
#     for t in threadList:
#         myLib.stop_thread(t)
