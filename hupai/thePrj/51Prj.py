import cv2
from PIL import ImageGrab ,Image
import numpy as np
import pyautogui,datetime,time ,threading
import theLib.damatu as td

method = eval('cv2.TM_CCOEFF_NORMED')
begin_x =800
begin_y =100

def click_img(url):
    print(datetime.datetime.now())
    target =Image.open(url)
    img_size =target.size
    target =cv2.cvtColor(np.array(target, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
    screen =ImageGrab.grab((begin_x ,begin_y ,1400 ,800))
    screen =cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
    res = cv2.matchTemplate(screen,target,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    pyautogui.click(x=(begin_x +max_loc[0] +img_size[0]//2) ,y=(begin_y +max_loc[1] +img_size[1]//2) ,button='left')
    print(datetime.datetime.now())

def check_img(url):
    print(datetime.datetime.now())
    target =Image.open(url)
    target =cv2.cvtColor(np.array(target, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
    screen =ImageGrab.grab((begin_x ,begin_y ,1400 ,800))
    screen =cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
    res = cv2.matchTemplate(screen,target,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(datetime.datetime.now())
    if max_val >0.9:
        return max_loc
    else:
        return 0

theCodeDict ={}
lock = threading.Lock()
code_url =r'C:\Users\guo\Desktop\thePrj\51\code.png'

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

def deCode():
    global theCodeDict
    for i in range(20):
        t =threading.Thread(target=getCode)
        t.start()
    time.sleep(9)
    print(theCodeDict)
    if 'ERROR' in theCodeDict:
        theCodeDict.pop('ERROR')
    if 'IERROR' in theCodeDict:
        theCodeDict.pop('IERROR')
    theCodeDict = sorted(theCodeDict.items(), key=lambda dic: dic[1])
    return theCodeDict[-1][0]
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
    # ret =ImageGrab.grab((0 ,0 ,tip.size[0] +code.size[0] ,tip.size[1]))
    ret.paste(tip ,(0 ,(ret.height -tip.height) //2 ,tip.width ,(ret.height -tip.height) //2 +tip.height))
    ret.paste(code ,(tip.width,0,ret.width,ret.height))
    ret.save(code_url, "PNG")

#main
pyautogui.click(x=260 ,y=1060 ,button='left')
time.sleep(0.1)
click_img(r"C:\Users\guo\Desktop\thePrj\51\add_price.png")
pyautogui.typewrite('800')
time.sleep(0.1)
click_img(r"C:\Users\guo\Desktop\thePrj\51\add_price_button.png")
time.sleep(0.1)
click_img(r"C:\Users\guo\Desktop\thePrj\51\confirm_price_button.png")
time.sleep(0.1)
while 1:
    if check_img(r"C:\Users\guo\Desktop\thePrj\51\get_code.png"):
        if check_img(r"C:\Users\guo\Desktop\thePrj\51\refresh_code_button.png"):
            click_img(r"C:\Users\guo\Desktop\thePrj\51\refresh_code_button.png")
        else:
            # code_pic =ImageGrab.grab((1070 ,420 ,1070 +300 ,420 +130))
            # code_pic.save(code_url, "PNG")
            grabCode()
            click_img(r"C:\Users\guo\Desktop\thePrj\51\type_code.png")
            pyautogui.typewrite(deCode())
            click_img(r"C:\Users\guo\Desktop\thePrj\51\confirm_code_button.png")
            break
    else:
        time.sleep(0.1)


