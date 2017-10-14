#初始化价格比对图列表
# imgPriceArea =(600 ,450 ,750 ,500)
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
    screen =cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
    for priceIndex in range(len(priceList)):
        res = cv2.matchTemplate(screen,priceImageLst[priceIndex],myLib.method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val >0.99:
            thePrice =priceList[priceIndex]
    if thePrice ==0:
        time.sleep(0.2)
        screen = ImageGrab.grab(imgPriceArea)
        screen = cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
        for priceIndex in range(len(priceList)):
            res = cv2.matchTemplate(screen, priceImageLst[priceIndex], myLib.method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if max_val > 0.99:
                thePrice = priceList[priceIndex]
    return thePrice

###第二阶段出价函数
def secondStepPrice(dPrice ,eTime ,times):
    global imgPrice1 ,imgPrice2
    pyautogui.doubleClick(theConf.coor_main_seconddeltaprice)
    pyautogui.typewrite(dPrice)
    time.sleep(0.05)
    pyautogui.click(theConf.coor_main_secondaddprice)
    time.sleep(0.05)
    ###继续出价
    pyautogui.click(theConf.coor_main_secondconfirmprice)
    print(str(timeStamp) + "_" + times + "_imgbegin")
    time.sleep(0.1)
    while 1:
        if myLib.check_img(theConf.check_main_refreshcode):
            myLib.click_img(theConf.check_main_refreshcode)
        elif myLib.check_img(theConf.check_main_secondcodehere):
            time.sleep(0.8)
            print(str(timeStamp) + "_" + times + "_imgfind")
            code = ImageGrab.grab(theConf.area_main_secondstepcode)
            payload = {'idt': identy ,'times' :times ,'hostName':hostName}
            if secondCheck:
                code.save(code_url, "PNG")
            else:
                catch = StringIO()
                code.save(catch, 'PNG')
                pyautogui.click(theConf.coor_main_secondstepcode)
                files = {'file': catch.getvalue()}
                print(str(timeStamp) + "_" + times + "_imgsendbegin")
                requests.post(servUrl + 'uploadPic', files=files, data=payload)
                print(str(timeStamp) + "_" + times + "_imgsendend")
            # print(datetime.datetime.now())
            #如果第一价，睡到出价前0.6秒取吗然后再睡到出价时间，睡两次
            # 第二价，可能睡三次，先睡到53.5,看是否计算etime
            # 无论是否计算etime，此时如果etime大于当前时间加0.6，就再睡到0.6时间取吗，之后再睡到出价时间
            if times =='2':
                if isPriceOffset:
                    # 睡到第1次检查价格：
                    if imgPriceTime1 > timeStamp:
                        time.sleep(imgPriceTime1 - timeStamp)
                    imgPrice1 =getImgPrice()
                    print('imgPrice1---' +str(imgPrice1) +'---' +str(imgPrice1 -basePrice))
                    # 睡到第2次检查价格：
                    if imgPriceTime2 > timeStamp:
                        time.sleep(imgPriceTime2 - timeStamp)
                    imgPrice2 = getImgPrice()
                    print('imgPrice2---' + str(imgPrice2) +'---' +str(imgPrice2 -basePrice))
                    #计算出价时间
                    if imgPrice1 !=0 and imgPrice2 !=0:
                        print('nb ,pb ,cb , tb ,nw ,pw ,cw =22, 1700, 200, 55, 0.1, 0.1, 0.5')
                        print('tb +(nb -nn) *nw +(pb -(imgPrice2-basePrice))/100 *pw +(cb -(imgPrice2-imgPrice1))/100 *cw +priceOffset')
                        calTime =tb +(nb -nn) *nw +(pb -(imgPrice2-basePrice))/100 *pw +(cb -(imgPrice2-imgPrice1))/100 *cw
                        print("calTime :" + str(calTime))
                        if isPriceOffset ==1:
                            eTime =calTime
                        if isPriceOffset ==2:
                            eTime =calTime -0.5
                        if isPriceOffset ==3:
                            eTime =calTime +0.5
                        print("etime :" +str(eTime))
            if eTime >timeStamp +0.5:
                time.sleep(eTime -timeStamp -0.5)
            #然后取回并输入验证码：
            if not secondCheck:
                print(str(timeStamp) + "_" + times + "_codegetbegin")
                theCode = requests.get(servUrl + 'getTrueCode', payload)
                print(str(timeStamp) + "_" + times + "_codegetend")
                pyautogui.typewrite(theCode.text)
            #睡到出价时间
            if eTime >timeStamp:
                time.sleep(eTime -timeStamp)
            print(str(timeStamp) + "_" + times + "_confirmPrice")
            pyautogui.click(theConf.coor_main_secondstepcodeconfirm)
            break
