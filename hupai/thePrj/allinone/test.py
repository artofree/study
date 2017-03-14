# # import damatu as td
import myLib ,damatu
from PIL import ImageGrab, Image
import numpy as np
import cv2 ,pyautogui, datetime, time, threading, requests
from io import BytesIO as StringIO
import configparser ,json ,zipfile ,os ,sys

time.sleep(5)
priceImageLst =[]
priceList =list(range(86000 ,88201 ,100))
print(priceList)
for index in range(len(priceList)):
    priceUrl ='rsc\\price\\' +str(priceList[index]) +'.png'
    print(priceUrl)
    priceImage = Image.open(priceUrl)
    priceImage = cv2.cvtColor(np.array(priceImage, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
    priceImageLst.append(priceImage)
print(len(priceImageLst))

print(datetime.datetime.now())
screen =ImageGrab.grab((600 ,450 ,750 ,500))
# screen.show()
screen =cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
for index in range(len(priceList)):
    res = cv2.matchTemplate(screen,priceImageLst[index],myLib.method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val >0.99:
        i =0
print(datetime.datetime.now())


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
