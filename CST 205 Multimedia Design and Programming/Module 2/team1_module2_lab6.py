#Team 1: Northwestern Technology
#Brian Sheridan
#Craig Calvert
#Kevin Bentley
#Samuel Pearce

#Warm Up
def copyPic(pic):
  width = pic.getWidth()
  height = pic.getHeight()
  sourcePixels = getPixels(pic)
  newPic = makeEmptyPicture(width,height)
  for row in range(height):
    for col in range(width):
      sourcePixel = getPixel(pic,col,row)
      sourceColor = getColor(sourcePixel)
      destPixel = getPixel(newPic,col,row)
      setColor(destPixel,sourceColor)
  return newPic

#red eye red color: 223,68,84
def removeRedEye(pic):
  redEyeColor = makeColor(223,68,84)
  pixels = getPixels(pic)
  for p in pixels:
    pixelColor = getColor(p)
    dist = distance(pixelColor,redEyeColor)
    if(dist < 62):
      #desaturate the color if it's too close to redeye
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      luminance = r*0.299 + g*0.587 + b*0.114
      newColor = makeColor(luminance,luminance,luminance)
      setColor(p,newColor)

def crazyRedEye(pic):
  redEyeColor = makeColor(223,68,84)
  pixels = getPixels(pic)
  for p in pixels:
    pixelColor = getColor(p)
    dist = distance(pixelColor,redEyeColor)
    if(dist < 100):
      newColor = makeColor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
      setColor(p,newColor)

def testRedEye():
  # Set this path to where your module 2 github repository is
  rootPath = r'C:\dev\csumb_nwtech\Module 2'
  redEyePath = os.path.join(rootPath,"redeye.jpg")
  redEyePic = makePicture(redEyePath)
  noRedEyePic = copyPic(redEyePic)
  show(redEyePic)
  removeRedEye(noRedEyePic)
  repaint(noRedEyePic)

#Problem 1:
def makeSepia(pic):
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    luminance = r*0.299 + g*0.587 + b*0.114
    redMult = 1
    blueMult = 1
    if(r < 63):
      redMult = 1.1
      blueMult = 0.9
    elif(62 < r and r < 192):
      redMult = 1.15
      blueMult = 0.85
    else:
      redMult = 1.08
      blueMult = 0.93    
    r = redMult * luminance
    r = min(r,255)
    b = blueMult * luminance
    setRed(p,r)
    setGreen(p,luminance)
    setBlue(p,b)
  return pic


#Problem 2
def getArtifiedPixel(p):
  #This is an ordered list of tuples. The first value is the 
  #upper range value to compare against. The second value is
  #the value to replace the original pixel with.
  colorSubstitutionTable = [(64,31),(128,95),(192,159),(256,223)]
  for tuple in colorSubstitutionTable:
    #If this pixel's value is less than the first value
    #in the tuple, return the second value
    if(p < tuple[0]):
      return tuple[1]
  return p
  
def Artify(pic):
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    setRed(p,getArtifiedPixel(r))
    setGreen(p,getArtifiedPixel(g))
    setBlue(p,getArtifiedPixel(b))
  return pic
    
#Problem 3
def chromakey(foregroundPic,backgroundPic):
  if(foregroundPic.getWidth() != backgroundPic.getWidth() or
    foregroundPic.getHeight() != backgroundPic.getHeight()):
    print("Foreground and background pictures must be the same size.")
  greenScreenColor = makeColor(0,255,0)
  foregroundPixels = getPixels(foregroundPic)
  for row in range(foregroundPic.getHeight()):
      for col in range(foregroundPic.getWidth()):
        foregroundPixel = getPixel(foregroundPic,col,row)
        pixelColor = getColor(foregroundPixel)
        dist = distance(pixelColor,greenScreenColor)
        if(dist < 185):
          backgroundPixel = getPixel(backgroundPic,col,row)
          backgroundColor = getColor(backgroundPixel)
          setColor(foregroundPixel,backgroundColor)
  return foregroundPic        


def testProblem1():
  rootPath = r'C:\dev\cs205\csumb_nwtech\Module 2'
  originalPath = os.path.join(rootPath,"1.jpg")
  originalPic = makePicture(originalPath)
  originalPic = makeSepia(originalPic)
  writePictureTo(originalPic,os.path.join(rootPath,"sepia.png"))
  show(originalPic)

def testProblem2():
  rootPath = r'C:\dev\cs205\csumb_nwtech\Module 2'
  originalPath = os.path.join(rootPath,"1.jpg")
  originalPic = makePicture(originalPath)
  originalPic = Artify(originalPic)
  writePictureTo(originalPic,os.path.join(rootPath,"artify.png"))
  show(originalPic)

def testProblem3():
  rootPath = ''
  rootPath = r'C:\dev\cs205\csumb_nwtech\Module 2\Green Screens'

  foregroundPath = os.path.join(rootPath,"eagle.png")
  backgroundPath = os.path.join(rootPath,"outdoors.jpg")
  backgroundPic = makePicture(backgroundPath)
  foregroundPic = makePicture(foregroundPath)
  foregroundPic0 = chromakey(foregroundPic,backgroundPic)
  #show(foregroundPic0)
  writePictureTo(foregroundPic0,os.path.join(rootPath,"eagle_outdoors.png"))
  foregroundPath = os.path.join(rootPath,"Richie Still 3.png")
  backgroundPath = os.path.join(rootPath,"fall.jpg")
  backgroundPic = makePicture(backgroundPath)
  foregroundPic = makePicture(foregroundPath)
  foregroundPic1 = chromakey(foregroundPic,backgroundPic)
  #show(foregroundPic1)
  writePictureTo(foregroundPic1,os.path.join(rootPath,"richie_still_fall.png"))
  foregroundPath = os.path.join(rootPath,"curtains.png")
  backgroundPath = os.path.join(rootPath,"opera_singer.jpg")
  backgroundPic = makePicture(backgroundPath)
  foregroundPic = makePicture(foregroundPath)
  foregroundPic2 = chromakey(foregroundPic,backgroundPic)
  #show(foregroundPic)
  writePictureTo(foregroundPic2,os.path.join(rootPath,"opera_singer_curtains.png"))
  return
  