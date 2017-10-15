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
priceList =list(range(90000 ,92401 ,100))
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


#检查价格
time.sleep(8)
print(getImgPrice())


#检查对时区域
# time.sleep(6)
# s_checkTime = (580, 430, 720, 480)
# screen = ImageGrab.grab(s_checkTime)
# screen.show()





# #当前价格的严格区域，注意，缩放比例要严格依此进行！！！
# imgPriceArea =(600, 468, 650, 484)
# #获取当前价格函数：
# def getImgPrice1():
#     img =ImageGrab.grab(imgPriceArea)
#     img =img.convert('L')
#     img =img.resize((500, 160),Image.ANTIALIAS)
#     code =pytesseract.image_to_string(img ,config='digits -psm 7')
#     print('oricode is :' +code)
#     #解决空格问题
#     nCode =''
#     for theC in code:
#         if theC in ['0','1','2','3','4','5','6','7','8','9']:
#             nCode +=theC
#     #长度大于5么取后五位
#     if len(nCode) >5:
#         nCode =nCode[-5:]
#     if len(nCode) >0:
#         if int(nCode) <80000 :
#             return 0
#     else:
#         return 0
#     return int(nCode)
#
# def getImgPrice():
#     vcode =getImgPrice1()
#     if vcode ==0 :
#         vcode =getImgPrice1()
#         if vcode ==0 :
#             return 0
#     return vcode

# while 1:
#     print('fincode is :'+str(getImgPrice()))
#     time.sleep(0.5)


