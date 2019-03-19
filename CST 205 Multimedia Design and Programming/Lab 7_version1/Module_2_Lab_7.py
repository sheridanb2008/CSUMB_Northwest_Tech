# Brian Sheridan
# Craig Calvert
# CST 205 Lab 7

# Warm-up Creat snowman in the desert.
def snowman():
  root = 'Z:\Csumb\CST 205\PY flies\Module_2_Lab_7'
  pic = makePicture(os.path.join(root,"desert.jpg"))
  addArcFilled(pic,229,540,50,50,0,360,white)
  addArcFilled(pic,232,503,40,40,0,360,white)
  addArcFilled(pic,229,477,30,30,0,360,white)  
  addArcFilled(pic,235,485,5,5,0,360,black)
  carrot = makeColor(235,137,33)  
  addArcFilled(pic,215,492,20,5,0,360,carrot)
  writePictureTo(pic, r'Z:\Csumb\CST 205\PY flies\Module_2_Lab_7\snowman.jpg')
  
#  Problem 1
# Make Thanksgiving day card
def makeCard():
  backGround = makePicture(pickAFile())
  pic1 = shrink(makePicture(pickAFile()))
  pic2 = makePicture(pickAFile())
  greenScreen(backGround, pic1, 325, 700)
  greenScreen(backGround, pic2, 500, 550)
  textStyle = makeStyle(sansSerif,bold,80)
  addTextWithStyle(backGround, 900,300, 'Happy',textStyle,blue)
  addTextWithStyle(backGround, 900,400, 'Thanksgiving',textStyle,blue)
  writePictureTo(backGround, r'Z:\Csumb\CST 205\PY flies\Module_2_Lab_7\Thanksgiving_Card.jpg')


#  Shrink the picture
def shrink(source):
  target = makeEmptyPicture(getWidth(source)/2,getHeight(source)/2)
  for x in range(0, getWidth(source), 2):
    for y in range(0, getHeight(source), 2):
      sourcePixel = getPixel(source,x,y)
      targetPixel = getPixel(target,x / 2,y / 2)
      color = getColor(sourcePixel)
      setColor(targetPixel, color)
  return target
      

# Greenscreen rendering  
def greenScreen(backGround, foreGround, targetX, targetY):
  greenScreen = makeColor(0,255,0)
  shadow = makeColor(33,29,22)
  for x in range(0, getWidth(foreGround)):
    for y in range(0, getHeight(foreGround)):
      picPixel = getPixel(foreGround,x, y)
      newPixel = getPixel(backGround,targetX + x ,targetY + y)
      color = getColor(picPixel)
      if distance(color,greenScreen) > 150:
        setColor(newPixel,color)
  return backGround