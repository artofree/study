# # import damatu as td
import myLib ,damatu
from PIL import ImageGrab, Image
import numpy as np
import cv2 ,pyautogui, datetime, time, threading, requests
from io import BytesIO as StringIO
import configparser ,json ,zipfile ,os ,sys ,pytesseract

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#用于前期自动登陆打码
code_url = os.path.join(os.path.join(BASE_DIR, 'rsc'), 'code.png')

imgPriceArea =(600 ,450 ,750 ,500)
imgPrice1 ,imgPrice2 =0 ,0
imgPriceTime1 ,imgPriceTime2 =50.5 ,53.5
priceImageLst =[]
priceList =list(range(88000 ,95000 ,100))
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
    screen.save(code_url)
    screen =cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
    for priceIndex in range(len(priceList)):
        res = cv2.matchTemplate(screen,priceImageLst[priceIndex],myLib.method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val >0.98:
            thePrice =priceList[priceIndex]
    if thePrice ==0:
        time.sleep(0.1)
        screen = ImageGrab.grab(imgPriceArea)
        screen.save(code_url)
        screen = cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
        for priceIndex in range(len(priceList)):
            res = cv2.matchTemplate(screen, priceImageLst[priceIndex], myLib.method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if max_val > 0.98:
                thePrice = priceList[priceIndex]
    return thePrice

# time.sleep(8)
# theConf = myLib.myConf()
# print(myLib.check_img(theConf.check_main_refreshcode))


#检查价格
# time.sleep(6)
# print(datetime.datetime.now())
# print(getImgPrice())
# print(datetime.datetime.now())


# 检查对时区域
time.sleep(6)
s_checkTime = (580, 430, 720, 480)
screen = ImageGrab.grab(s_checkTime)
screen.show()



