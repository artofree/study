from PIL import Image ,ImageDraw

#圆角矩形
def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    circle.show()
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

# im = Image.open("/Users/guo/Documents/1.jpg")
# im =im.resize((640 ,640) ,Image.ANTIALIAS)
# im =add_corners(im ,100)
# im =im.resize((48 ,48) ,Image.ANTIALIAS)
# im.save('/Users/guo/Documents/2.png' ,'PNG' ,quality = 100)

#圆环
def huan(iLen ,width ,r ,g ,b):
    im =Image.new('RGBA' ,(2 *(iLen +width) ,2 *(iLen +width)) ,(r ,g ,b ,0))
    alpha =Image.new('L' ,(2 *(iLen +width) ,2 *(iLen +width)) ,0)
    draw =ImageDraw.Draw(alpha)
    draw.ellipse((0 ,0 ,2 *(iLen +width) ,2 *(iLen +width)) ,fill=255)
    draw.ellipse((width ,width ,2*iLen +width ,2*iLen +width) ,fill=0)
    im.putalpha(alpha)
    return im

# im =huan(200 ,50 ,255 ,0 ,0)
# im.save('/Users/guo/Documents/3.png' ,'PNG' ,quality = 100)

#掩码使用
png=Image.open("/Users/guo/Documents/I2uNe.png")
background=Image.new("RGBA",png.size,(255,255,255,0))
r,g,b,a=png.split()
r.show()
background.paste(png,mask=r)
background.save('/Users/guo/Documents/4.png' ,'PNG' ,quality = 100)