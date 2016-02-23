from PIL import Image ,ImageDraw

circle = Image.new('RGBA', (100 * 2, 100 * 2), (127,32,150,255))
circle.save('/Users/guo/Documents/5.png' ,'PNG' ,quality = 100)
# draw =ImageDraw.Draw(circle)
# draw.ellipse(circle.getbbox() ,(0 ,0 ,0 ,1))
# draw.chord(circle.getbbox() ,0 ,270 ,(0 ,0 , 0, 0))
# circle.save('/Users/guo/Documents/5.png' ,'PNG' ,quality = 100)
