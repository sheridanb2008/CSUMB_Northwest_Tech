# CST205
# Midterm Project
# CSUMBy (25th Anniversay) Instagram Filter
# Craig Calvert
# Samuel Pearce

# Set the path to the graphics directory
root = os.path.join(os.path.dirname(os.path.realpath(__file__)),"images")

# Copies the logo over the submitted picture
def copyLogo(picture):
  picHeight = getHeight(picture)
  logo = makePicture(os.path.join(root,"csumb25logo.png"))
  for x in range(0, getWidth(logo)):
    for y in range(0, getHeight(logo)):
      color = getColor(getPixel(logo, x, y))
      setColor(getPixel(picture, x + 290, y + ((picHeight - 354)/2)), color)
  return(picture)

# Takes the submitted picture and fades it
def fade(picture):
  for x in range(0, getWidth(picture)):
    for y in range(0, getHeight(picture)):
      pixel = getPixel(picture, x, y)
      a = getRed(pixel)
      b = a * 0.37 + 98
      setRed(pixel, b)
      a = getGreen(pixel)
      b = a * 0.37 + 98
      setGreen(pixel, b)
      a = getBlue(pixel)
      b = a * 0.37 + 98
      setBlue(pixel, b) 
  return(picture)

# CSUMBy Instagram filter
def csumby(picture):
  picWidth = getWidth(picture)
  picHeight = getHeight(picture)
  csumbBlue = makeColor(0,42,78)
  
  # Checks if picture being entered is a standard Instagram size
  if (picWidth == 1080 and picHeight == 566 or
    picHeight == 1080 or picHeight == 1350):
    pass
  else:
    print('Picture is the incorrect size. All pictures need to be:\n1080 x 566, 1080 x 1080, or 1080 x 1350.')
  # If picture is correct size call method to fade picture
  fade(picture)
  # Generate picture border (top, bottom, left, right)
  addRectFilled(picture, 0, 0, picWidth, 15, csumbBlue)
  addRectFilled(picture, 0, picHeight - 15, picWidth, 15, csumbBlue)
  addRectFilled(picture, 0, 15, 15, picHeight - 30, csumbBlue)
  addRectFilled(picture, picWidth - 15, 15, 15, picHeight - 30, csumbBlue)
  copyLogo(picture)
  return(picture)
  
# Method tests

def csumbyTest():
  pic = makePicture(pickAFile())
  csumby(pic)
  show(pic)

