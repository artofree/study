import myLib, damatu, sys
from PIL import ImageGrab, Image
import numpy as np
import cv2, pyautogui, datetime, time, threading, requests
from io import BytesIO as StringIO
import configparser,os

pyautogui.FAILSAFE =False

decodeThreadList = []
theCodeDict = {}
servUrl = 'http://139.219.234.120:8000/'
# servUrl = 'http://139.219.238.37:8000/'
# servUrl = 'http://192.168.8.102:8020/'
# servUrl = 'http://116.237.16.180:8000/'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#用于前期自动登陆打码
code_url = os.path.join(os.path.join(BASE_DIR, 'rsc'), 'code.png')
theConf = myLib.myConf()
lock = threading.Lock()

timeStamp ,stampDlt=0 ,0
baseH ,baseM ,baseS1 ,baseS2=11 ,29 ,12 ,23
baseTime =baseH *3600 +baseM *60
s_checkTime = (500, 200, 900, 600)
timeTarget1 = Image.open(r'rsc\29_12.png')
timeTarget1 = cv2.cvtColor(np.array(timeTarget1, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
timeTarget2 = Image.open(r'rsc\29_23.png')
timeTarget2 = cv2.cvtColor(np.array(timeTarget2, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
cf = configparser.ConfigParser()
cf.read(r"C:\Users\guo\Desktop\mainConf")

###第一常量，版本号信息
curVersion = 0

###第二常量，用hostname获得拍牌人信息和出价策略
hostName =cf.get('main', 'hostname')
infoList =requests.get(servUrl + 'getOrderInfo', {'hostname':hostName}).text.split('~')
print(infoList)
identy ,orderid, orderpass, firstPrice ,secondPrice= infoList[0] ,infoList[1] ,infoList[2] ,infoList[3] ,infoList[4]
firstPrice =firstPrice.split('-')
first_bTime, first_eTime, first_dPrice =float(firstPrice[0]) ,float(firstPrice[1]) ,firstPrice[2]
secondPrice =secondPrice.split('-')
second_bTime, second_eTime, second_dPrice =float(secondPrice[0]) ,float(secondPrice[1]) ,secondPrice[2]

###第三常量，取自mainConf
curStep =cf.get('main', 'step')
isMainClient =cf.get('main', 'mainclient')
handMade =cf.get('main', 'handmade')
secondCheck =int(cf.get('main', 'secondCheck'))


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

    for t in decodeThreadList:
        myLib.stop_thread(t)
    decodeThreadList = []

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
    theCode = theCodeDict[-1][0]
    theCodeDict = {}
    return theCode

def checkVersion():
    while 1:
        if int(requests.get(servUrl + 'getVersion').text) > curVersion:
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

def makeTimeStamp():
    global timeStamp ,stampDlt ,baseTime
    while 1:
        now =datetime.datetime.now()
        theH =int(now.strftime('%H'))
        theM =int(now.strftime('%M'))
        theS =int(now.strftime('%S'))
        theStamp =theH *3600 +theM *60 +theS -baseTime +int(now.strftime('%f')[:2]) /100 -stampDlt
        # theStamp =round(theStamp ,2)
        # print(theStamp)
        if 0 <theStamp <60:
            timeStamp =theStamp
        time.sleep(0.1)

isFirstTimeChecked =False
def checkTime():
    global timeTarget1 ,timeTarget2 ,stampDlt ,isFirstTimeChecked
    while 1:
        try:
            screen = ImageGrab.grab(s_checkTime)
        except OSError:
            continue
        screen = cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
        res1 = cv2.matchTemplate(screen, timeTarget1, myLib.method)
        min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res1)
        res2 = cv2.matchTemplate(screen, timeTarget2, myLib.method)
        min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(res2)
        if not isFirstTimeChecked and max_val1 >0.99:
            isFirstTimeChecked =True
            now =datetime.datetime.now()
            stampDlt =int(now.strftime('%H')) *3600 +int(now.strftime('%M')) *60 +int(now.strftime('%S')) +int(now.strftime('%f')[:2]) /100 -baseTime -baseS1
            stampDlt =round(stampDlt ,2)
            print('time_12_check')
            if isMainClient =='1':
                payload = {'times' :'1'}
                requests.get(url=servUrl +'setTimeStamp' ,params=payload)
        if max_val2 >0.99:
            now =datetime.datetime.now()
            stampDlt =int(now.strftime('%H')) *3600 +int(now.strftime('%M')) *60 +int(now.strftime('%S')) +int(now.strftime('%f')[:2]) /100 -baseTime -baseS2
            stampDlt =round(stampDlt ,2)
            print('time_23_check')
            if isMainClient =='1':
                payload = {'times' :'2'}
                requests.get(url=servUrl +'setTimeStamp' ,params=payload)
            return
        time.sleep(0.1)

def against():
    while 1:
        if myLib.check_img(theConf.check_main_kick):
            pyautogui.click([1150,550])
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
    pyautogui.doubleClick(theConf.coor_login_orderid)
    time.sleep(1)
    pyautogui.typewrite(orderid)
    time.sleep(1)
    pyautogui.doubleClick(theConf.coor_login_orderpass)
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
    pyautogui.doubleClick(theConf.coor_main_firststep1)
    time.sleep(1)
    pyautogui.typewrite(price)
    time.sleep(1)
    pyautogui.doubleClick(theConf.coor_main_firststep2)
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

###获取预览图
def secondStepGetTestImg():
    pyautogui.click(theConf.coor_main_secondtestaddprice)
    time.sleep(1)
    pyautogui.click(theConf.coor_main_secondconfirmprice)
    time.sleep(1)
    while 1:
        if myLib.check_img(theConf.check_main_refreshcode):
            myLib.click_img(theConf.check_main_refreshcode)
        elif myLib.check_img(theConf.check_main_secondcodehere):
            if not secondCheck:
                code = ImageGrab.grab(theConf.area_main_secondstepcode)
                catch = StringIO()
                code.save(catch, 'PNG')
                pyautogui.click(theConf.coor_main_secondstepcode)
                payload = {'idt': identy ,'times' :'0'}
                files = {'file': catch.getvalue()}
                requests.post(servUrl + 'uploadPic', files=files, data=payload)
            pyautogui.click(theConf.coor_main_secondetestcancel)
            break


###第二阶段出价函数
def secondStepPrice(dPrice ,eTime ,times):
    pyautogui.doubleClick(theConf.coor_main_seconddeltaprice)
    pyautogui.doubleClick(theConf.coor_main_seconddeltaprice)
    pyautogui.typewrite(dPrice)
    time.sleep(0.1)
    pyautogui.click(theConf.coor_main_secondaddprice)
    time.sleep(0.3)
    pyautogui.click(theConf.coor_main_secondconfirmprice)
    time.sleep(0.1)
    while 1:
        if myLib.check_img(theConf.check_main_refreshcode):
            myLib.click_img(theConf.check_main_refreshcode)
        elif myLib.check_img(theConf.check_main_secondcodehere):
            time.sleep(0.3)
            code = ImageGrab.grab(theConf.area_main_secondstepcode)
            payload = {'idt': identy ,'times' :times}
            if secondCheck:
                code.save(code_url, "PNG")
            else:
                catch = StringIO()
                code.save(catch, 'PNG')
                pyautogui.click(theConf.coor_main_secondstepcode)
                files = {'file': catch.getvalue()}
                requests.post(servUrl + 'uploadPic', files=files, data=payload)
            # print(datetime.datetime.now())
            if eTime >timeStamp:
                time.sleep(eTime - timeStamp -0.5)
            if not secondCheck:
                theCode = requests.get(servUrl + 'getTrueCode', payload)
                pyautogui.typewrite(theCode.text)
                time.sleep(0.5)
            pyautogui.click(theConf.coor_main_secondstepcodeconfirm)
            break

isGetTestImg =1
isFirstPrice =1
def secondStep():
    global isGetTestImg
    global isFirstPrice
    while 1:
        if timeStamp >27:
            if isGetTestImg:
                secondStepGetTestImg()
                isGetTestImg =0
        if timeStamp >first_bTime:
            if isFirstPrice:
                secondStepPrice(first_dPrice ,first_eTime ,'1')
                time.sleep(1)
                myLib.click_img(theConf.check_main_confirm)
                isFirstPrice =0
        if timeStamp > second_bTime:
            secondStepPrice(second_dPrice ,second_eTime ,'2')
            break
        time.sleep(0.1)


####################################################################################
###主线程

def mainWork():
    ###无论是否主终端都启动对时线程：
    makeTimeTrhead = threading.Thread(target=makeTimeStamp)
    makeTimeTrhead.start()
    if not secondCheck:
        checkTimeTrhead = threading.Thread(target=checkTime)
        checkTimeTrhead.start()
    ###线程0-检查版本改变
    # checkVersionThread = threading.Thread(target=checkVersion)
    # checkVersionThread.start()
    ###线程1-常规终端只开获得时间戳
    # timeStampThread = threading.Thread(target=getTimeStamp)
    # timeStampThread.start()
    ###线程2-防t
    againstThread = threading.Thread(target=against)
    againstThread.start()
    ###主线程非手动版么自动登陆：
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
    if secondCheck:
        now =datetime.datetime.now()
        theH =int(now.strftime('%H'))
        theM =int(now.strftime('%M'))
        theS =int(now.strftime('%S'))
        #减10意味着当前为11：29：10，测试状态下不做对时
        baseTime =theH *3600 +theM *60 +theS -10
    mainWork()
