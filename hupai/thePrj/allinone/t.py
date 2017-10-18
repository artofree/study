# # import damatu as td
import myLib ,damatu
from PIL import ImageGrab, Image
import numpy as np
import cv2 ,pyautogui, datetime, time, threading, requests
from io import BytesIO as StringIO
import configparser ,json ,zipfile ,os ,sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#用于前期自动登陆打码
code_url = os.path.join(os.path.join(BASE_DIR, 'rsc'), 'code.png')
jpg_url = os.path.join(os.path.join(BASE_DIR, 'rsc'), 'code.jpg')

img1 =Image.open(r'rsc\price\90900.png')
# img1 =Image.open(code_url)
img1 = cv2.cvtColor(np.array(img1, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
img2 =Image.open(r'rsc\price\90000.png')
img2 = cv2.cvtColor(np.array(img2, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
res = cv2.matchTemplate(img1,img2,myLib.method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print(max_val)


# imgPriceArea =(600 ,450 ,750 ,500)
# imgPrice1 ,imgPrice2 =0 ,0
# imgPriceTime1 ,imgPriceTime2 =50.5 ,53.5
# priceImageLst =[]
# priceList =list(range(85000 ,93000 ,100))
# for index in range(len(priceList)):
#     priceUrl ='rsc\\price\\' +str(priceList[index]) +'.png'
#     priceImage = Image.open(priceUrl)
#     priceImage = cv2.cvtColor(np.array(priceImage, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
#     priceImageLst.append(priceImage)
# #截图取价函数
# def getImgPrice():
#     global  imgPriceArea ,priceList ,priceImageLst
#     thePrice =0
#     screen =ImageGrab.grab(imgPriceArea)
#     screen =cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
#     for priceIndex in range(len(priceList)):
#         res = cv2.matchTemplate(screen,priceImageLst[priceIndex],myLib.method)
#         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#         if max_val >0.99:
#             thePrice =priceList[priceIndex]
#     if thePrice ==0:
#         print('----------------------------------------------')
#         time.sleep(0.2)
#         screen = ImageGrab.grab(imgPriceArea)
#         screen = cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
#         for priceIndex in range(len(priceList)):
#             res = cv2.matchTemplate(screen, priceImageLst[priceIndex], myLib.method)
#             min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#             if max_val > 0.99:
#                 thePrice = priceList[priceIndex]
#     return thePrice
#
# time.sleep(8)
# while 1:
#     print(getImgPrice())
#     time.sleep(0.5)


# import pytesseract
# from PIL import ImageGrab, Image ,ImageFilter
# time.sleep(8)
# oldTime =time.time()
# codeList =[]
# while 1:
#     img =ImageGrab.grab((600, 468, 720, 484))
#     img =img.convert('L')
#     img =img.resize((1200, 160),Image.ANTIALIAS)
#     # img =img.filter(ImageFilter.EDGE_ENHANCE_MORE)
#     vcode = pytesseract.image_to_string(img ,config='digits -psm 8')
#     ncode =vcode.replace(' ' ,'')
#     ncode =ncode.replace(':' ,'')[-5:]
#     ret ='1'
#     if len(ncode) >0:
#         if int(ncode) <80000 :
#             ret ='0'
#     else:
#         ret ='0'
#     print(vcode +'--' +ncode +'--' +ret)
#     time.sleep(0.5)
    # theCode =''
    # for theChar in vcode:
    #     if theChar in ['0','1','2','3','4','5','6','7','8','9']:
    #         theCode +=theChar

# code ='dsfadsf12432ui3up9rq0h5fj 6 {78}:}'
# nCode =''
# for theC in code:
#     if theC in ['0','1','2','3','4','5','6','7','8','9']:
#         nCode +=theC
# print(nCode)

# image =Image.open(os.path.join(os.path.join(BASE_DIR, 'rsc'), '2.JPG'))
# time.sleep(8)
# screen = ImageGrab.grab((664, 468, 706, 484))
# screen.save(jpg_url)
# screen = screen.convert('L')
# screen =screen.resize((420, 160),Image.ANTIALIAS)
# # screen =screen.filter(ImageFilter.EDGE_ENHANCE_MORE)
# screen.show()
# vcode = pytesseract.image_to_string(screen ,config='digits -psm 7')
# print(vcode)

# from pyocr import pyocr
# tools = pyocr.get_available_tools()[:]
# print("Using '%s'" % (tools[0].get_name()))
# tools[0].SetVariable("tessedit_char_whitelist", "0123456789")
# print(tools[0].image_to_string(Image.open(jpg_url),lang='eng'))

# screen.save(jpg_url)
# screen.save(code_url, "PNG")
# img =Image.open(jpg_url)
# img =img.convert('1')
# vcode = pytesseract.image_to_string(img ,config='digits -psm 7')
# vcode = pytesseract.image_to_string(screen)
# print(vcode)





#关于价格匹配
# time.sleep(5)
# priceImageLst =[]
# priceList =list(range(90000 ,92401 ,100))
# # print(priceList)
# for index in range(len(priceList)):
#     priceUrl ='rsc\\price\\' +str(priceList[index]) +'.png'
#     priceImage = Image.open(priceUrl)
#     priceImage = cv2.cvtColor(np.array(priceImage, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
#     priceImageLst.append(priceImage)
#
# time.sleep(10)
#
# print(datetime.datetime.now())
# screen = ImageGrab.grab((600, 450, 750, 500))
# screen = cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
# for index in range(len(priceList)):
#     res = cv2.matchTemplate(screen,priceImageLst[index],myLib.method)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#     if max_val > 0.99:
#         print(priceList[index])
# print(datetime.datetime.now())

# screen =ImageGrab.grab((600 ,450 ,750 ,500))
# screen.save(code_url, "PNG")
# screen.show()
# valList =[]
# while 1:
#     screen = ImageGrab.grab((600, 450, 750, 500))
#     screen = cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
#     for index in range(len(priceList)):
#         res = cv2.matchTemplate(screen,priceImageLst[index],myLib.method)
#         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#         # valList.append(max_val)
#         if max_val > 0.99:
#             print(priceList[index])
#     time.sleep(0.5)

    # print(valList)
    # valList =[]
    # time.sleep(0.5)
    # if max_val >0.99:
    #     i =0
# print(datetime.datetime.now())


# code = ImageGrab.grab([960, 410, 1190, 545])
# catch = StringIO()
# code.save(catch, 'PNG')
#
# payload = {'idt': "000000000000000001" ,'times' :'0'}
# files = {'file': catch.getvalue()}
#
# count =0
#
# while 1:
#     # thetime =time.time()
#     # requests.get('http://139.219.238.37:8000/' + 'getVersion')
#     requests.get('http://139.219.238.37:8000/static/exp/1.png')
#     count +=1
#     if count %100 ==0:
#         print(datetime.datetime.now())
    # if time.time() -thetime >1:
        # print(time.time() -thetime)
    # time.sleep(1)

    # requests.post('http://58.33.101.128:8000/' + 'uploadPic', files=files, data=payload)
    # requests.post('http://192.168.0.100:8000/' + 'uploadPic', files=files, data=payload)
    # requests.get('http://139.219.238.37:8000/' + 'getVersion')
    # requests.post('http://139.219.238.37:8000/' + 'uploadPic', files=files, data=payload)


# print(type(int('1')))


# time.sleep(5)
# s_checkTime = (0, 0, 1920, 1080)
# timeTarget = Image.open(r'rsc\29_23.png')
# timeTarget = cv2.cvtColor(np.array(timeTarget, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
# screen = ImageGrab.grab(s_checkTime)
# screen = cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
# res = cv2.matchTemplate(screen, timeTarget, myLib.method)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# if max_val > 0.99:
#     print(1)

# def test():
#     print(100)
#     time.sleep(20)
#     python = sys.executable
#     os.execl(python, python, *sys.argv)
#
# if __name__=='__main__':
#     test()

# lock = threading.Lock()
#
# def Thread1():
#     time.sleep(5)
#     print('thread1')
#
# def Thread2():
#     lock.acquire()
#     try:
#         print('thread2')
#     finally:
#         lock.release()
#
#
# t1 = threading.Thread(target=Thread1)
# t1.start()
# time.sleep(1)
# myLib.stop_thread(t1)
# t2 = threading.Thread(target=Thread2)
# t2.start()

# import myThread
#
# myThread.beginWork()
# time.sleep(10)
# myThread.clearWork()

# theConf =myLib.myConf()
# time.sleep(5)
# myLib.click_img(theConf.check_main_confirm)

# cmd = 'taskkill /F /IM iexplore.exe'
# os.system(cmd)

# time.sleep(5)
# theConf =myLib.myConf()
# pyautogui.click(theConf.coor_login_closefirstpage)
# print(myLib.check_img(theConf.check_login_against))
# cf = configparser.ConfigParser()
# cf.read(r"C:\Users\guo\Desktop\step")
# cf.set('main' ,'step' ,'1')
# cf.write(open(r"C:\Users\guo\Desktop\step", "w"))
# step =cf.get('main' ,'step')
# print(step)
# if step =='0':
#     print(1)
# scns =cf.sections()
# print(scns)
# print(cf.options('login'))
# print(cf.items('login'))
# theTuple =cf.get('login' ,'thread')
# theTuple =json.loads(theTuple)
# print(type(theTuple))
