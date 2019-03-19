# Brian Sheridan And Kevin Bentley
# CST 205 
# Midterm Project Double-y

def doubley(source):
# CREATE TH ROOT PATH
  root = os.path.dirname(os.path.realpath(__file__))
  art = root = os.path.join(os.path.dirname(os.path.realpath(__file__)),"Clipart")
# BRING THE IMAGES INTO THE PROGRAM  
  pic1 = makePicture(source)
  print "Choose another picture to combined with the original." 
  pic2 = makePicture(pickAFile())
# CREATE NEW PICTURE TO ALLOW FOR MULTIPY IMAGAE SIZES
  pic3 = makeEmptyPicture(min(getWidth(pic1),getWidth(pic2)),min(getHeight(pic1),getHeight(pic2)))
  pic4 = makePicture(os.path.join(root,"4.jpg"))  
# FUNCTIONS
  combine(pic3,pic1,pic2)
  greenScreen(pic3,pic4,(getWidth(pic3) - getWidth(pic4)),(getHeight(pic3) - getHeight(pic4)))
  show(pic3)
  
def combine(output, source1, source2):
  x1, x2, y1, y2 = 0, 0, 0, 0
# SET THE STARTING POINT TO OVERLAY IMAGE
# THE SIDES WITH THE LEAST PIXELS WILL BE SELECTED 
   
  if getWidth(source1) > getWidth(source2):
    x1 = getWidth(source1) - getWidth(source2)
  elif getWidth(source1) < getWidth(source2):
    x2 = getWidth(source2) - getWidth(source1)
  if getHeight(source1) > getHeight(source2):
    y1 = getHeight(source1) - getHeight(source2)
  elif getHeight(source1) < getHeight(source2):
    y2 = getHeight(source2) - getHeight(source1)    
# OVERLAY IMAGES AND AVERAGE PIXELS TOGETHER
  for x in range(0, getWidth(output)):
    for y in range(0, getHeight(output)):
      pix1 = getPixel(source1, x + (x1 / 2), y + (y1 / 2))
      pix2 = getPixel(source2, x + (x2 / 2), y + (y2 / 2))
      pix3 = getPixel(output,x, y)
      r = (getRed(pix1) + getRed(pix2)) / 2
      g = (getGreen(pix1) + getGreen(pix2)) / 2
      b = (getBlue(pix1) + getBlue(pix2)) / 2
      color = makeColor(r,g,b)
      setColor(pix3,color)
  return output
  
# FUNCTION GREENSCREEN
# -ADDS TARGET IMAGE OVER SOUCRE PICTURE ND MITIGATES THE COLOR GREEN     
def greenScreen(source,targetP,targetX,targetY):
# MAKE THE COLOR GREEN THAT IS GOING TO BE MITIGATED 
  nColor = makeColor(14,9,69)
# CYCLE THROUGH THE TARGET PICTURE  
  for x in range(0,getWidth(targetP)):
    for y in range(0,getHeight(targetP)):
# PULL IN THE CURRENT COLOR OF THE PIXEL
      color = getColor(getPixel(targetP,x,y))
# COMPARE COLOR TO THE MITIGATED COLOR IF IT IS NOT A MATCH 
# PLACE THE COLOR OF THE PIXEL ON THE SOURCE PICTURE
      if distance(nColor,color) < 125:
        setColor(getPixel(source,targetX + x,targetY + y),color)
  return source
  

