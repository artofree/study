import myLib, damatu, sys
from PIL import ImageGrab, Image
import numpy as np
import cv2, pyautogui, datetime, time, threading, requests
from io import BytesIO as StringIO
import configparser,os

pyautogui.FAILSAFE =False

decodeThreadList = []
theCodeDict = {}
servUrl = 'http://52.80.83.187:8020/'
# servUrl = 'http://192.168.0.100:8020/'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#用于前期自动登陆打码
code_url = os.path.join(os.path.join(BASE_DIR, 'rsc'), 'code.png')
theConf = myLib.myConf()
lock = threading.Lock()

timeStamp ,stampDlt =0 ,0
baseH ,baseM ,baseS1 ,baseS2=11 ,29 ,12 ,23
baseTime =baseH *3600 +baseM *60
s_checkTime = (580, 430, 720, 480)
timeTarget1 = Image.open(r'rsc\29_12.png')
timeTarget1 = cv2.cvtColor(np.array(timeTarget1, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
timeTarget2 = Image.open(r'rsc\29_23.png')
timeTarget2 = cv2.cvtColor(np.array(timeTarget2, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
cf = configparser.ConfigParser()
cf.read(r"C:\Users\guo\Desktop\mainConf")

#初始化码区图片：
codeAreaPic = ImageGrab.grab(theConf.area_main_secondstepcode)
codeAreaPic =cv2.cvtColor(np.array(codeAreaPic, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
#初始化价格比对图列表
# imgPriceArea =(600 ,450 ,750 ,500)
imgPriceArea =(600 ,450 ,750 ,500)
imgPrice1 ,imgPrice2 =0 ,0
imgPriceTime1 ,imgPriceTime2 ,isImgPrice1Check=47.3 ,53.3 ,1
priceImageLst =[]
priceList =list(range(86000 ,90000 ,100))
for index in range(len(priceList)):
    priceUrl ='rsc\\price\\' +str(priceList[index]) +'.png'
    priceImage = Image.open(priceUrl)
    priceImage = cv2.cvtColor(np.array(priceImage, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
    priceImageLst.append(priceImage)
#截图取价函数
def getImgPrice():
    global  imgPriceArea ,priceList ,priceImageLst
    thePrice =0
    screen =ImageGrab.grab(imgPriceArea)
    screen =cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
    for priceIndex in range(len(priceList)):
        res = cv2.matchTemplate(screen,priceImageLst[priceIndex],myLib.method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val >0.98:
            thePrice =priceList[priceIndex]
    if thePrice ==0:
        time.sleep(0.1)
        screen = ImageGrab.grab(imgPriceArea)
        screen = cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
        for priceIndex in range(len(priceList)):
            res = cv2.matchTemplate(screen, priceImageLst[priceIndex], myLib.method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if max_val > 0.98:
                thePrice = priceList[priceIndex]
    return thePrice


###第一常量，版本号信息，时间信息
curVersion = 0
testBeginTime ,firstBeginTime=20 ,33

###第二常量，用hostname获得拍牌人信息和出价策略
hostName =cf.get('main', 'hostname')
infoList =requests.get(servUrl + 'getOrderInfo', {'hostname':hostName}).text.split('~')
print(infoList)
identy ,orderid, orderpass, firstPrice ,secondPrice ,isPriceOffset= infoList[0] ,infoList[1] ,infoList[2] ,infoList[3] ,infoList[4] ,int(infoList[5])
firstPrice =firstPrice.split('-')
first_bTime, first_eTime, first_dPrice =float(firstPrice[0]) ,float(firstPrice[1]) ,firstPrice[2]
secondPrice =secondPrice.split('-')
second_bTime, second_eTime, second_dPrice =float(secondPrice[0]) ,float(secondPrice[1]) ,secondPrice[2]
finTime =second_eTime

###第三常量，取自mainConf
curStep =cf.get('main', 'step')
isMainClient =cf.get('main', 'mainclient')
handMade =cf.get('main', 'handmade')
secondCheck =int(cf.get('main', 'secondCheck'))
#最终出价时间的人数变量：
nn =int(cf.get('main', 'nn'))
basePrice =int(cf.get('main', 'basePrice'))
#出价时间计算常量：
#计算式为：tb +(nb -nn) *nw +(pb -(53秒价-basePrice))/100 *pw +(cb -(53秒价-50秒价))/100 *cw
# nb ,pb ,cb ,tb ,nw ,pw ,cw =22, 1700, 200, 55, 0.1, 0.1, 0.5
nb ,pb ,cb ,tb ,nw ,pw ,cw =18, 10, 2, 56, 0, 0.1, 0.3




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
    if myLib.check_img(theConf.check_main_refreshcode):
        myLib.click_img(theConf.check_main_refreshcode)
        time.sleep(3)
        if myLib.check_img(theConf.check_main_refreshcode):
            myLib.click_img(theConf.check_main_refreshcode)
            time.sleep(3)
    code = ImageGrab.grab(area_code)
    code.save(code_url, "PNG")
    time.sleep(1)
    for i in range(10):
        t = threading.Thread(target=getCode)
        t.start()
        decodeThreadList.append(t)
    time.sleep(12)

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
    global timeStamp ,stampDlt ,baseTime ,imgPrice1 ,isImgPrice1Check ,imgPriceTime1 ,isPriceOffset
    while 1:
        now =datetime.datetime.now()
        theH =int(now.strftime('%H'))
        theM =int(now.strftime('%M'))
        theS =int(now.strftime('%S'))
        theStamp =theH *3600 +theM *60 +theS -baseTime +int(now.strftime('%f')[:2]) /100 -stampDlt
        theStamp =round(theStamp ,2)
        # print(theStamp)
        if 0 <theStamp <60:
            timeStamp =theStamp
            if isPriceOffset:
                if isImgPrice1Check:
                    if imgPriceTime1 < timeStamp:
                        imgPrice1 = getImgPrice()
                        print('imgPrice1---' + str(imgPrice1) + '---:' + str(imgPrice1 - basePrice))
                        isImgPrice1Check =0
        time.sleep(0.1)

isFirstTimeChecked =False
def checkTime():
    global timeTarget1 ,timeTarget2 ,stampDlt ,isFirstTimeChecked
    while 1:
        # try:
        #     screen = ImageGrab.grab(s_checkTime)
        # # except (OSError, MemoryError):
        # except OSError:
        #     continue
        screen = ImageGrab.grab(s_checkTime)
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
            print('time_12_check--' +str(stampDlt))
            if isMainClient =='1':
                payload = {'times' :'1'}
                requests.get(url=servUrl +'setTimeStamp' ,params=payload)
        if max_val2 >0.99:
            now =datetime.datetime.now()
            stampDltNew =int(now.strftime('%H')) *3600 +int(now.strftime('%M')) *60 +int(now.strftime('%S')) +int(now.strftime('%f')[:2]) /100 -baseTime -baseS2
            stampDltNew =round(stampDltNew ,2)
            # stampDlt =round((stampDlt +stampDltNew) /2 ,2)
            if stampDlt ==0:
                stampDlt =stampDltNew
            else:
                stampDlt =min(stampDlt ,stampDltNew)
            print('time_23_check--' +str(stampDltNew) +'--' +str(stampDlt))
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
    pyautogui.click([360 ,40])
    time.sleep(1)
    pyautogui.typewrite('https://paimai.alltobid.com/')
    # pyautogui.typewrite('www.163.com')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(8)
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
    time.sleep(5)
    pyautogui.doubleClick(theConf.coor_main_firststep1)
    time.sleep(1)
    pyautogui.typewrite(price)
    time.sleep(1)
    pyautogui.doubleClick(theConf.coor_main_firststep2)
    time.sleep(1)
    pyautogui.typewrite(price)
    time.sleep(1)
    pyautogui.click(theConf.coor_main_firststepconfirm)
    time.sleep(5)
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
    pyautogui.doubleClick(theConf.coor_main_secondtestaddprice)
    time.sleep(0.1)
    pyautogui.click(theConf.coor_main_secondtestaddprice)
    time.sleep(0.1)
    pyautogui.click(theConf.coor_main_secondconfirmprice)
    time.sleep(1.5)
    if not secondCheck:
        code = ImageGrab.grab(theConf.area_main_secondstepcode)
        catch = StringIO()
        code.save(catch, 'PNG')
        pyautogui.click(theConf.coor_main_secondstepcode)
        payload = {'idt': identy, 'times': '0', 'hostName': hostName}
        files = {'file': catch.getvalue()}
        print(str(timeStamp) + "_testimgsendbegin")
        requests.post(servUrl + 'uploadPic', files=files, data=payload)
        print(str(timeStamp) + "_testimgsendend")
    pyautogui.click(theConf.coor_main_secondetestcancel)

###二阶段第一次出价函数
def secondStepPrice1(dPrice ,eTime):
    pyautogui.doubleClick(theConf.coor_main_seconddeltaprice)
    pyautogui.typewrite(dPrice)
    time.sleep(0.05)
    pyautogui.click(theConf.coor_main_secondaddprice)
    time.sleep(0.05)
    ###继续出价
    pyautogui.click(theConf.coor_main_secondconfirmprice)
    time.sleep(1)
    code = ImageGrab.grab(theConf.area_main_secondstepcode)
    payload = {'idt': identy ,'times' :'1' ,'hostName':hostName}
    if secondCheck:
        code.save(code_url, "PNG")
    else:
        catch = StringIO()
        code.save(catch, 'PNG')
        pyautogui.click(theConf.coor_main_secondstepcode)
        files = {'file': catch.getvalue()}
        print(str(timeStamp) + "_1_imgsendbegin")
        requests.post(servUrl + 'uploadPic', files=files, data=payload)
        print(str(timeStamp) + "_1_imgsendend")
    #第一价，睡到出价前0.5秒取吗然后再睡到出价时间，睡两次
    if eTime >timeStamp +0.5:
        time.sleep(eTime -timeStamp -0.5)
    #然后取回并输入验证码：
    if not secondCheck:
        print(str(timeStamp) + "_1_codegetbegin")
        theCode = requests.get(servUrl + 'getTrueCode', payload)
        print(str(timeStamp) + "_1_codegetend")
        pyautogui.typewrite(theCode.text)
    #睡到出价时间
    if eTime >timeStamp:
        time.sleep(eTime -timeStamp)
    print(str(timeStamp) + "_1_confirmPrice")
    pyautogui.click(theConf.coor_main_secondstepcodeconfirm)

def getCodePic():
    global codeAreaPic ,finTime
    oldTime =timeStamp
    print(str(timeStamp) + "_2_codebegin")
    payload = {'idt': identy, 'times': '2', 'hostName': hostName}
    while 1:
        time.sleep(0.1)
        if timeStamp -oldTime >5 or finTime -timeStamp <2:
            print(timeStamp ,oldTime ,finTime ,timeStamp)
            break
        if myLib.check_img(theConf.check_main_refreshcode):
            myLib.click_img(theConf.check_main_refreshcode)
            continue
        #获取码区图片并于老内容比较
        code = ImageGrab.grab(theConf.area_main_secondstepcode)
        newAreaPic =cv2.cvtColor(np.array(code, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
        res = cv2.matchTemplate(codeAreaPic, newAreaPic, myLib.method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val < 0.99:
            codeAreaPic =newAreaPic
            if secondCheck:
                code.save(code_url, "PNG")
            else:
                catch = StringIO()
                code.save(catch, 'PNG')
                pyautogui.click(theConf.coor_main_secondstepcode)
                files = {'file': catch.getvalue()}
                requests.post(servUrl + 'uploadPic', files=files, data=payload)
                print(str(timeStamp) + "_2_code_upload")



###二阶段第二次出价函数
def secondStepPrice2(bTime ,dPrice ,eTime):
    global imgPrice1 ,imgPrice2 ,finTime
    #特殊化短策略出价前的等待时间
    restTime = 0.6
    if bTime >48.5:
        restTime =0.4
    if bTime >49.5:
        restTime =0.2
# pyautogui.doubleClick(theConf.coor_main_seconddeltaprice)
    pyautogui.typewrite(dPrice)
    time.sleep(0.05)
    pyautogui.click(theConf.coor_main_secondaddprice)
    time.sleep(0.05)
    ###继续出价
    pyautogui.click(theConf.coor_main_secondconfirmprice)
    print(str(timeStamp) + "_2_imgbegin")
    time.sleep(0.2)
    #启动取码线程
    getCodePicThread = threading.Thread(target=getCodePic)
    getCodePicThread.start()
    # 第二价，可能睡三次，先睡到53.5,看是否计算etime
    # 无论是否计算etime，此时如果etime大于当前时间加0.5，就再睡到0.5时间取吗，之后再睡到出价时间
    if isPriceOffset:
        # 睡到第1次检查价格：
        # if imgPriceTime1 > timeStamp:
        #     time.sleep(imgPriceTime1 - timeStamp)
        # imgPrice1 =getImgPrice()
        # print('imgPrice1---' +str(imgPrice1) +'---' +str(imgPrice1 -basePrice))
        # 睡到第2次检查价格：
        if imgPriceTime2 > timeStamp:
            time.sleep(imgPriceTime2 - timeStamp)
        imgPrice2 = getImgPrice()
        print('imgPrice2---' + str(imgPrice2) +'---:' +str(imgPrice2 -basePrice))
        #计算出价时间
        if imgPrice1 !=0 and imgPrice2 !=0:
            print('nb ,pb ,cb , tb ,nw ,pw ,cw =18, 10, 2, 56, 0, 0.1, 0.3')
            calTime =tb +(nb -nn) *nw +(pb -(imgPrice2-basePrice)/100) *pw +(cb -(imgPrice2-imgPrice1)/100) *cw
            print("calTime :" + str(calTime))
            if isPriceOffset ==1:
                eTime =calTime
            if isPriceOffset ==2:
                eTime =calTime -0.5
            if isPriceOffset ==3:
                eTime =calTime +0.5
            finTime =eTime
            print("etime :" +str(eTime))
    if eTime >timeStamp +restTime:
        time.sleep(eTime -timeStamp -restTime)
    #然后取回并输入验证码：
    if not secondCheck:
        print(str(timeStamp) + "_2_codegetbegin")
        payload = {'idt': identy ,'times' :'2' ,'hostName':hostName}
        theCode = requests.get(servUrl + 'getTrueCode', payload)
        print(str(timeStamp) + "_2_codegetend")
        pyautogui.typewrite(theCode.text)
    #睡到出价时间
    pyautogui.moveTo(theConf.coor_main_secondstepcodeconfirm)
    if eTime >timeStamp:
        time.sleep(eTime -timeStamp)
    print(str(timeStamp) + "_2_confirmPrice")
    pyautogui.click()

isGetTestImg =1
isFirstPrice =1
def secondStep():
    global isGetTestImg
    global isFirstPrice
    while 1:
        if timeStamp >testBeginTime:
            if isGetTestImg:
                secondStepGetTestImg()
                isGetTestImg =0
        if timeStamp >firstBeginTime:
            if isFirstPrice:
                secondStepPrice1(first_dPrice ,first_eTime)
                time.sleep(1)
                myLib.click_img(theConf.check_main_confirm)
                isFirstPrice =0
                time.sleep(0.5)

                pyautogui.doubleClick(theConf.coor_main_seconddeltaprice)
                pyautogui.press('backspace')
                pyautogui.doubleClick(theConf.coor_main_seconddeltaprice)
        #第二次出价统一基准时间
        if timeStamp > second_bTime:
            secondStepPrice2(second_bTime ,second_dPrice ,second_eTime)
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
    # againstThread = threading.Thread(target=against)
    # againstThread.start()
    ###主线程非手动版么自动登陆：
    if handMade =='0':
        pyautogui.click(1800, 800)
        ###未登陆：
        if curStep == '0':
            preLogin()
            login()
        ###第一次出价
        if curStep == '1':
            firstStep(str(basePrice))
            # cf.set('main', 'step', '2')
            # cf.write(open(r"C:\Users\guo\Desktop\step", "w"))
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
