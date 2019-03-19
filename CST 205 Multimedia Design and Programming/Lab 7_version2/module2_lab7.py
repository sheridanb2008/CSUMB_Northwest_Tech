#CST205
#Module 2: Lab 7
#Kevin Bentley
#Samuel Pearce

#Warm Up

def snowman(pic):
  #Snowman's body
  addOvalFilled(pic, 184, 213, 60, 60, white)
  addOvalFilled(pic, 162, 273, 104, 104, white)
  addRectFilled(pic, 196, 270, 36, 7, green)
  #Snowman's left arm
  addLine(pic, 143, 264, 175, 291, black)
  addLine(pic, 149, 260, 151, 271, black)
  addLine(pic, 140, 268, 148, 269, black)
  #Snowman's hat
  addRectFilled(pic, 191, 198, 46, 25, black)
  addRectFilled(pic, 177, 223, 71, 3, black)
  addRectFilled(pic, 191, 218, 46, 5, red)
  #Snowman's face
  addOvalFilled(pic, 202, 237, 6, 6, black)
  addOvalFilled(pic, 220, 237, 6, 6, black)
  addOvalFilled(pic, 211, 243, 6, 6, orange)
  addArc(pic, 201, 242, 25, 19, 180, 180, black)
  #Snowman's buttons
  addOvalFilled(pic, 210, 293, 8, 8, black)
  addOvalFilled(pic, 210, 311, 8, 8, black)
  addOvalFilled(pic, 210, 329, 8, 8, black)
  #Sign
  addRectFilled(pic, 286,239, 100, 70, yellow)
  addRect(pic, 286,239, 100, 70, black)
  #Sign text
  s = makeStyle(sansSerif, bold, 15)
  addTextWithStyle(pic, 295, 260, "North Pole", s, black)
  addTextWithStyle(pic, 330, 280, "or", s, black)
  addTextWithStyle(pic, 317, 300, "BUST", s, red) 
  #Snowman's right arm
  addLine(pic, 254, 292, 286, 284, black)
  addLine(pic, 285, 285, 293, 278, black)
  addLine(pic, 285, 285, 293, 288, black)
  return pic

#Problem 1

#Sepia method from lab 6, problem #1
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

#Chroma-key method from lab 6, problem #3
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

def thanksgivingCard(foregroundPic, backgroundPic, subject):
  backgroundPic = makeSepia(backgroundPic)
  backgroundPic = chromakey(subject, backgroundPic)
  pic = chromakey(foregroundPic, backgroundPic)
  style1 = makeStyle(mono, bold, 255)
  style2 = makeStyle(mono, bold, 155)
  addTextWithStyle(pic, 371, 350, "Happy", style1, white)
  addTextWithStyle(pic, 161, 1846, "Thanksgiving!", style2, white)
  return pic

#Method tests

def testWarmup():
  rootPath = r'/Users/craigcalvert/Documents/GitHub/csumb_nwtech/Lab 7_version2/warmup_pictures'
  originalPath = os.path.join(rootPath, "desert.jpg")
  originalPic = makePicture(originalPath)
  originalPic = snowman(originalPic)
  writePictureTo(originalPic, '/Users/craigcalvert/Documents/GitHub/csumb_nwtech/Lab 7_version2/warmup_pictures/snowman_output.jpg')
  show(originalPic)
  
def problem1():
  rootPath = r'/Users/craigcalvert/Documents/GitHub/csumb_nwtech/Lab 7_version2/problem1_pictures'
  foregroundPath = os.path.join(rootPath, "cardFrame.png")
  backgroundPath = os.path.join(rootPath, "background.png")
  subjectPath = os.path.join(rootPath, "turkey.png")
  foregroundPic = makePicture(foregroundPath)
  backgroundPic = makePicture(backgroundPath)
  turkey = makePicture(subjectPath)
  newPic = thanksgivingCard(foregroundPic, backgroundPic, turkey)
  writePictureTo(newPic, '/Users/craigcalvert/Documents/GitHub/csumb_nwtech/Lab 7_version2/problem1_pictures/thanksgivingCard.png')
  show(newPic)
