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
imgPriceTime45 ,imgPriceTime48 , imgPriceTime49 ,imgPriceTime54 ,isImgPriceCheck45 ,isImgPriceCheck48 ,isImgPriceCheck49 ,imgPrice45 ,imgPrice48 ,imgPrice49=45.2 ,48.2 ,49.3 ,54.3 ,1 ,1 ,1 ,0 ,0 ,0
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
identy ,orderid, orderpass, firstPrice ,secondPrice ,subPrice ,pFlag= infoList[0] ,infoList[1] ,infoList[2] ,infoList[3] ,infoList[4] ,infoList[5] ,int(infoList[6])
firstPrice =firstPrice.split('-')
first_bTime, first_eTime, first_dPrice =float(firstPrice[0]) ,float(firstPrice[1]) ,firstPrice[2]
secondPrice =secondPrice.split('-')
second_bTime, second_eTime, second_dPrice =float(secondPrice[0]) ,float(secondPrice[1]) ,secondPrice[2]
sub_bTime, sub_eTime, sub_dPrice =0 ,0 ,0
if pFlag ==1:
    subPrice =int(subPrice)
else:
    subPrice =subPrice.split('-')
    sub_bTime, sub_eTime, sub_dPrice =float(subPrice[0]) ,float(subPrice[1]) ,subPrice[2]

###第三常量，取自mainConf
curStep =cf.get('main', 'step')
isMainClient =cf.get('main', 'mainclient')
handMade =cf.get('main', 'handmade')
secondCheck =int(cf.get('main', 'secondCheck'))
#最终出价时间的人数变量：
# tag =int(cf.get('main', 'tag'))
basePrice =int(cf.get('main', 'basePrice'))
#出价时间计算常量：
#计算式为：tb +(nb -nn) *nw +(pb -(53秒价-basePrice))/100 *pw +(cb -(53秒价-50秒价))/100 *cw
#pb ,cb ,tb ,tagw ,pw ,cw =12, 2, 55.5, 0.5, 0.1, 0.2
#计算式为：tb +(cb -(54秒价-49秒价)/100) *cw
tb ,cb ,cw =55.0 ,3.0 ,0.25


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

def makeTimeStamp():
    global timeStamp ,stampDlt ,baseTime ,isImgPriceCheck45 ,imgPrice45 ,isImgPriceCheck48 ,imgPrice48 ,isImgPriceCheck49 ,imgPrice49 ,second_bTime, second_eTime, second_dPrice
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
            # 45秒一定检查价格，取价格失败执行原策略。随即对pFlag2检查，pFlag3也需要用到该价格。满足pFlag2执行子策略，否则执行原策略
            if timeStamp > imgPriceTime45 and isImgPriceCheck45 == 1 and (pFlag ==2 or pFlag ==3):
                isImgPriceCheck45 = 0
                imgPrice45 = getImgPrice()
                print('imgPrice45.2---' + str(imgPrice45) + '---:' + str(imgPrice45 - basePrice))
                if (imgPrice45 - basePrice) >= 900 and pFlag == 2:
                    print('change stage45...!')
                    second_bTime, second_dPrice ,second_eTime =sub_bTime ,sub_dPrice ,sub_eTime
            #48秒一定检查价格，取价失败执行原策略。随即对pFlag3检查，满足pFlag3执行子策略，不满足执行48-45策略
            if timeStamp > imgPriceTime48 and isImgPriceCheck48 == 1 and (pFlag ==3 or pFlag ==4):
                imgPrice48 = getImgPrice()
                print('imgPrice48.2---' + str(imgPrice48) + '---:' + str(imgPrice48 - basePrice))
                if pFlag == 3 and imgPrice48 != 0 and imgPrice45 != 0:
                    if (imgPrice48 - basePrice) < 700 or ((imgPrice48 - basePrice) == 700 and (imgPrice45 - basePrice) == 700):
                        print('change stage48...!')
                        second_bTime, second_dPrice, second_eTime = sub_bTime, sub_dPrice, sub_eTime
                    else:
                        second_dPrice = str(int(second_dPrice) - (imgPrice48 - imgPrice45))
                isImgPriceCheck48 = 0

            if timeStamp > imgPriceTime49 and isImgPriceCheck49 == 1 and pFlag ==1:
                isImgPriceCheck49 = 0
                imgPrice49 = getImgPrice()
                print('imgPrice49.3---' + str(imgPrice49) + '---:' + str(imgPrice49 - basePrice))
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
    # time.sleep(1)
    # pyautogui.typewrite(deCode(theConf.area_login_code))
    # time.sleep(1)
    # pyautogui.click(theConf.coor_login_longin)
    # time.sleep(5)
    # if myLib.check_img(theConf.check_login_against):
    #     pyautogui.click(theConf.coor_login_confirmagainst)
    #     time.sleep(1)
    #     againstLogin()


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
    # time.sleep(1)
    # pyautogui.typewrite(deCode(theConf.area_main_firststepcode, 4))
    # time.sleep(15)
    # pyautogui.click(theConf.coor_main_firststepcodeconfirm)
    # time.sleep(5)
    # myLib.click_img(theConf.check_main_confirm)
    # time.sleep(1)

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
    global codeAreaPic
    oldTime =timeStamp
    print(str(timeStamp) + "_2_codebegin")
    payload = {'idt': identy, 'times': '2', 'hostName': hostName}
    while 1:
        time.sleep(0.1)
        #考虑到总会给码工4.5秒以上打码时间，所以，5不大再有变了
        if timeStamp -oldTime >5:
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
def secondStepPrice2(dPrice ,eTime):
    #特殊化短策略出价前的等待时间
    restTime = 0.3
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

    if pFlag ==4:
        time.sleep(54.1 - timeStamp)
        if secondCheck ==0:
            print(str(timeStamp) + "_2_54codegetbegin")
            payload = {'idt': identy ,'times' :'2' ,'hostName':hostName}
            theCode = requests.get(servUrl + 'getTrueCode', payload)
            print(str(timeStamp) + "_2_54codegetend")
            pyautogui.typewrite(theCode.text)
        print(datetime.datetime.now())
        imgPrice540 = getImgPrice()
        print('imgPrice54.0---' + str(imgPrice540) + '---:' + str(imgPrice540 - basePrice))
        if imgPrice540 !=0 and imgPrice48 !=0:
            if (imgPrice540 -imgPrice48) >=500:
                print(str(timeStamp) + "_2_54confirmPrice")
                pyautogui.doubleClick(theConf.coor_main_secondstepcodeconfirm)
                return

    # 仅仅在pFlag ==1的时候取54.2价格，并计算出价时间
    if pFlag ==1:
        time.sleep(imgPriceTime54 - timeStamp)
        imgPrice543 = getImgPrice()
        print('imgPrice54.3---' + str(imgPrice543) +'---:' +str(imgPrice543 -basePrice))
        #计算出价时间
        if imgPrice49 !=0 and imgPrice543 !=0:
            print('tb ,cb ,cw =55.0 ,3.0 ,0.25')
            calTime =tb +(cb -(imgPrice543-imgPrice49)/100) *cw
            print("calTime :" + str(calTime))
            if subPrice ==1:
                eTime =calTime
            if subPrice ==2:
                eTime =calTime -0.5
            if subPrice ==3:
                eTime =calTime +0.5
            print("etime :" +str(eTime))
    if eTime >timeStamp +restTime:
        time.sleep(eTime -timeStamp -restTime)
    #然后取回并输入验证码：
    if secondCheck ==0 and pFlag !=4:
        print(str(timeStamp) + "_2_codegetbegin")
        payload = {'idt': identy ,'times' :'2' ,'hostName':hostName}
        theCode = requests.get(servUrl + 'getTrueCode', payload)
        print(str(timeStamp) + "_2_codegetend")
        pyautogui.typewrite(theCode.text)
    #睡到出价时间
    if eTime >timeStamp:
        time.sleep(eTime -timeStamp)
    print(str(timeStamp) + "_2_confirmPrice")
    pyautogui.doubleClick(theConf.coor_main_secondstepcodeconfirm)

isGetTestImg =1
isFirstPrice =1
def secondStep():
    global isGetTestImg ,isFirstPrice ,second_bTime, second_dPrice, second_eTime
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

        #确保pFlag3情况下，48秒的原始策略不先于48秒价格检查执行
        if pFlag !=3 or isImgPriceCheck48 !=1:
            if timeStamp > second_bTime:
                secondStepPrice2(second_dPrice ,second_eTime)
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
    ###线程3-第二阶段是个线程
    secondStepThread =threading.Thread(target=secondStep)
    secondStepThread.start()



if __name__=='__main__':
    if secondCheck:
        now1 =datetime.datetime.now()
        theH1 =int(now1.strftime('%H'))
        theM1 =int(now1.strftime('%M'))
        theS1 =int(now1.strftime('%S'))
        #减10意味着当前为11：29：10，测试状态下不做对时
        baseTime =theH1 *3600 +theM1 *60 +theS1 -10
    mainWork()
