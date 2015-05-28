from PIL import Image, ImageDraw

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

def round_corner(radius):
    """Draw a round corner"""
    corner = Image.new('RGBA', (radius, radius), (0, 0, 0, 0))
    draw = ImageDraw.Draw(corner)
    draw.pieslice((0, 0, radius * 2, radius * 2), 180, 270, fill="blue")
    return corner

def blank_roundrect(length ,rad):
    circle = Image.new('RGBA', (rad * 2, rad * 2), (255,255,255,0))
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), "grey")
    alpha = Image.new('RGBA', (length ,length), (127,127,127,1))
    w =length
    h =length
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    return alpha

from PIL import Image
def myPic():
    pic = Image.new("RGB",(64,64))
    for x in range(64):
        for y in range(64):
            pic.putpixel((x,y),(64 +x +y,64 +x +y,64 +x +y))
    pic =pic.rotate(90)
    pic =pic.resize((560,560),Image.ANTIALIAS)
    pic.save('/Users/guopeng/Documents/panoramio/blank.jpg' ,'JPEG' ,quality = 100)

myPic()

# im1=round_corner(100)
# im1.save('/Users/guopeng/Documents/panoramio/74363.png' ,'PNG' ,quality = 100)

im1 =Image.open('/Users/guopeng/Documents/panoramio/photos/74363.jpg')
im1 =im1.resize((500,500),Image.ANTIALIAS)
im1 =add_corners(im1 ,40)
im1.load()
background = Image.new("RGB", im1.size, (160, 160, 160))
background.paste(im1, mask=im1.split()[3]) # 3 is the alpha channel
#background.save('/Users/guopeng/Documents/panoramio/74363.jpg' ,'JPEG' ,quality = 100)
# im1.convert('RGB').save('/Users/guopeng/Documents/panoramio/74363.jpg' ,'JPEG' ,quality = 100)
# im1 =Image.open('/Users/guopeng/Documents/panoramio/74363.png')

im2 =Image.new('RGBA', (560,560) ,(160 ,160 ,160))
im2.paste(background,(30 ,30 ,530 ,530))
im2 =add_corners(im2 ,70)
im2 =im2.resize((64,64) ,Image.ANTIALIAS)
im2.save('/Users/guopeng/Documents/panoramio/74363.jpg' ,'PNG' ,quality = 100)











circle = Image.new('RGBA', (100 * 2, 100 * 2))
draw = ImageDraw.Draw(circle)
draw.ellipse((0, 0, 100 * 2, 100 * 2), "black")
#im1 =blank_roundrect(100,20)
alpha =Image.new('RGBA', (500,500) ,(0 ,0 ,0 ,0))
w=500
h=500
rad=100
alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
alpha.save('/Users/guopeng/Documents/panoramio/78555.jpg' ,'JPEG' ,quality = 100)


im = Image.open('/Users/guopeng/Documents/panoramio/photos/74363.jpg')
im =im.resize((480,480),Image.ANTIALIAS)
im = add_corners(im, 80)
#im =im.resize((56,56),Image.ANTIALIAS)
alpha.paste(im ,(10,10,490,490))
#alpha =alpha.resize((56,56),Image.ANTIALIAS)
alpha.save('/Users/guopeng/Documents/panoramio/78555.png' ,'PNG' ,quality = 100)
