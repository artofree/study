import cv2
from PIL import ImageGrab ,Image
import numpy as np
import pyautogui,datetime,time ,threading
import theLib.damatu as td

method = eval('cv2.TM_CCOEFF_NORMED')
begin_x =800
begin_y =100
timeTarget =Image.open(r'C:\Users\guo\Desktop\thePrj\51\29_21.png')
timeTarget =cv2.cvtColor(np.array(timeTarget, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
timeStamp =0
theCodeDict ={}
lock = threading.Lock()
code_url =r'C:\Users\guo\Desktop\thePrj\51\code.png'

def addTime():
    global timeStamp
    while 1:
        time.sleep(1)
        timeStamp +=1

def checkTime():
    global timeTarget
    global timeStamp
    screen =ImageGrab.grab((500 ,200 ,900 ,600))
    screen =cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
    res = cv2.matchTemplate(screen,timeTarget,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val >0.99:
        timeStamp =21
        t =threading.Thread(target=addTime)
        t.start()

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

def getCode():
    dmt=td.DamatuApi("slientcraft","inwcwizard")
    theCode =dmt.decode(code_url,200)
    lock.acquire()
    try:
        global theCodeDict
        if theCode in theCodeDict:
            theCodeDict[theCode] +=1
        else:
            theCodeDict[theCode] =1
    finally:
        lock.release()

def grabCode():
    target =Image.open(r'C:\Users\guo\Desktop\thePrj\51\tip_end.png')
    tip_loc =check_img(r'C:\Users\guo\Desktop\thePrj\51\tip_begin.png')
    left ,top=begin_x +tip_loc[0] ,begin_y +tip_loc[1]
    tip_loc =check_img(r'C:\Users\guo\Desktop\thePrj\51\tip_end.png')
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

def deCode():
    global theCodeDict
    global timeStamp
    for i in range(20):
        t =threading.Thread(target=getCode)
        t.start()
    print(55-timeStamp)
    time.sleep(55 -timeStamp)
    print(theCodeDict)
    if 'ERROR' in theCodeDict:
        theCodeDict.pop('ERROR')
    if 'IERROR' in theCodeDict:
        theCodeDict.pop('IERROR')
    theCodeDict = sorted(theCodeDict.items(), key=lambda dic: dic[1])
    theCodeDict ={}
    print(theCodeDict[-1][0])
    return theCodeDict[-1][0]

def beginWork():
    click_img(r"C:\Users\guo\Desktop\thePrj\51\add_price.png" ,1)
    pyautogui.typewrite('800')

def mainWork():
    click_img(r"C:\Users\guo\Desktop\thePrj\51\add_price_button.png")
    click_img(r"C:\Users\guo\Desktop\thePrj\51\confirm_price_button.png")
    while 1:
        if check_img(r"C:\Users\guo\Desktop\thePrj\51\tip_begin.png"):
            if check_img(r"C:\Users\guo\Desktop\thePrj\51\refresh_code_button.png"):
                click_img(r"C:\Users\guo\Desktop\thePrj\51\refresh_code_button.png")
            else:
                # print(datetime.datetime.now())
                print(timeStamp)
                grabCode()
                click_img(r"C:\Users\guo\Desktop\thePrj\51\type_code.png")
                print(timeStamp)
                pyautogui.typewrite(deCode())
                click_img(r"C:\Users\guo\Desktop\thePrj\51\confirm_code_button.png")
                break

#main
pyautogui.click(x=260 ,y=1060 ,button='left')
beginWork()

while 1:
    #找点对齐时间
    if not timeStamp:
        checkTime()
    #检查有没被T出
    #...
    #到策略点干活
    if timeStamp ==45:
        mainWork()
        break
    time.sleep(0.3)



