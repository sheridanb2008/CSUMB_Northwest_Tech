# CST205
# Midterm Project
# Clearly Instagram Filter
# Craig Calvert
# Samuel Pearce

# Set the path to the graphics directory
root = os.path.join(os.path.dirname(os.path.realpath(__file__)),"images")

# Determines the areas that the filters do not need to be applied to.
def coordinates(height):
  # X values for all image sizes
  leftLenseX = [182, 381, 138, 425]
  rightLenseX = [700, 899, 657, 944]
  # Y values for area not to apply blur manipulation for 1080 x 566 image
  lenses566y = [140, 181, 180, 386, 385, 426]
  # Y values for area not to apply blur manipulation for 1080 x 1080 image
  lenses1080y = [397, 438, 437, 643, 642, 683]
  # Y values for area not to apply blur manipulation for 1080 x 1350 image
  lenses1350y = [532, 573, 572, 778, 777, 818]
  # X and Y values to pass on
  lx1 = leftLenseX[0]
  lx2 = leftLenseX[1]
  lx3 = leftLenseX[2]
  lx4 = leftLenseX[3]
  rx1 = rightLenseX[0]
  rx2 = rightLenseX[1]
  rx3 = rightLenseX[2]
  rx4 = rightLenseX[3]
  y1 = eval('lenses' + str(height) + 'y[0]')
  y2 = eval('lenses' + str(height) + 'y[1]')
  y3 = eval('lenses' + str(height) + 'y[2]')
  y4 = eval('lenses' + str(height) + 'y[3]')
  y5 = eval('lenses' + str(height) + 'y[4]')
  y6 = eval('lenses' + str(height) + 'y[5]')
  return lx1, lx2, lx3, lx4, rx1, rx2, rx3, rx4, y1, y2, y3, y4, y5, y6

# Takes the submitted image and blurs it
def blur(picture):
  width = getWidth(picture)
  height = getHeight(picture)
  # Retrieve the x,y coordinates for the areas not to apply the blur manipulation
  lx1, lx2, lx3, lx4, rx1, rx2, rx3, rx4, y1, y2, y3, y4, y5, y6 = coordinates(height)
  for x in range(1, width - 1):
    for y in range(1, height - 1):
      if ((x >= lx1 and x <= lx2) and ((y >= y1 and y <= y2) or (y >= y5 and y <= y6)) or
        (x >= lx3 and x <= lx4) and (y >= y3 and y <= y4)):
        pass
      elif ((x >= rx1 and x <= rx2) and ((y >= y1 and y <= y2) or (y >= y5 and y <= y6)) or
        (x >= rx3 and x <= rx4) and (y >= y3 and y <= y4)):
        pass
      else:
        pixel = getPixel(picture, x, y)
        right = getPixel(picture, x + 1, y)
        left = getPixel(picture, x - 1, y)
        topLeft = getPixel(picture, x - 1, y - 1)
        top = getPixel(picture, x, y - 1)
        topRight = getPixel(picture, x + 1, y - 1)
        bottomLeft = getPixel(picture, x - 1, y + 1)
        bottom = getPixel(picture, x, y + 1)
        bottomRight = getPixel(picture, x + 1, y + 1)
        # The line of code below was viewed in a video found at
        # https://www.youtube.com/watch?v=8iIPlNNUWfc. However, we did make some slight 
        # alterations to it.
        colorAverage = (lambda function: sum(map(function, [right, left, topLeft, top, 
        topRight, bottomLeft, bottom, bottomRight])) / 8)
        redAverage = colorAverage(getRed)
        greenAverage = colorAverage(getGreen)
        blueAverage = colorAverage(getBlue)
        blurColor = makeColor(redAverage, greenAverage, blueAverage)
        setColor(pixel, blurColor)
  return picture
  
# Converts image to grayscale
def betterBnW(picture):
  width = getWidth(picture)
  height = getHeight(picture)
  # Retrieve the x,y coordinates for the areas not to apply the blur manipulation
  lx1, lx2, lx3, lx4, rx1, rx2, rx3, rx4, y1, y2, y3, y4, y5, y6 = coordinates(height)
  for x in range(1, width - 1):
    for y in range(1, height - 1):
      if ((x >= lx1 and x <= lx2) and ((y >= y1 and y <= y2) or (y >= y5 and y <= y6)) or
        (x >= lx3 and x <= lx4) and (y >= y3 and y <= y4)):
        pass
      elif ((x >= rx1 and x <= rx2) and ((y >= y1 and y <= y2) or (y >= y5 and y <= y6)) or
        (x >= rx3 and x <= rx4) and (y >= y3 and y <= y4)):
        pass
      else:
        pixel = getPixel(picture, x, y)
        r = getRed(pixel)
        g = getGreen(pixel)
        b = getBlue(pixel)
        luminance = r*0.299 + g*0.587 + b*0.114
        setRed(pixel,luminance)
        setGreen(pixel,luminance)
        setBlue(pixel,luminance)
  return picture
  
# Chromakey method to combine eyeglasses with submitted image
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
        if(dist < 200):
          backgroundPixel = getPixel(backgroundPic,col,row)
          backgroundColor = getColor(backgroundPixel)
          setColor(foregroundPixel,backgroundColor)
  return foregroundPic
  
# Clearly Instagram filter
def clearly(picture):
  picWidth = getWidth(picture)
  picHeight = getHeight(picture)
  # Checks if picture being entered is a standard Instagram size
  if (picWidth == 1080 and picHeight == 566 or
    picHeight == 1080 or picHeight == 1350):
    pass
  else:
    print('Picture is the incorrect size. All pictures need to be:\n1080 x 566, 1080 x 1080, or 1080 x 1350.')
  # If picture is correct size call method to blur the picture
  # and then call the method to convert it to gray-scale
  blur(picture)
  betterBnW(picture)
  # Select correct eyeglass image for picture size
  if picHeight == 566:
    foregroundPic = makePicture(os.path.join(root,"glasses_1080x566.png"))
  elif picHeight == 1080:
    foregroundPic = makePicture(os.path.join(root,"glasses_1080x1080.png"))
  else:
    foregroundPic = makePicture(os.path.join(root,"glasses_1080x1350.png"))
  picture = chromakey(foregroundPic,picture)
  return picture

# Method tests

def clearlyTest():
  picture = makePicture(pickAFile())
  newPic = clearly(picture)
  show(newPic)

