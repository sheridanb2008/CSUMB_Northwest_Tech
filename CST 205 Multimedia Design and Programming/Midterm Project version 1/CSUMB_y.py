# Brian Sheridan And Kevin Bentley
# CST 205 
# Midterm Project CSUMB-y

# Main 
def csumb(source):
# FIND THE PATH TO THE CURRENT DIRECTORY AND ADD THE CLIPART FOLDER 
  root = os.path.join(os.path.dirname(os.path.realpath(__file__)),"Clipart")
# IMPORT THE PICTURES THAT WILL BE USED  
  pic1 = makePicture(source)
  pic2 = makePicture(os.path.join(root,"2.jpg"))
  pic3 = makePicture(os.path.join(root,"3.jpg"))  
  pic4 = makePicture(os.path.join(root,"4.jpg"))  
# COLLECT USER INPUT FOR BANNER
  text = requestString("Type input for your banner.")
# MANIPULATE IMAGES VIA FUNCTIONS  
  greenScreen(pic1,pic2,0,0)
  startX = getWidth(pic1) - 251
  greenScreen(pic1,pic3,startX,0)  
  bannerFill(pic1,text)
  startX = getWidth(pic1) - getWidth(pic4)
  startY = getHeight(pic1) - getHeight(pic4)
  greenScreen(pic1,pic4,startX,startY)
  show(pic1)

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

# FUNCTION BANNERFILL
#- BUILD A BANNER ACROSS THE PICTURE AND FILLS IT WITH TEXT
def bannerFill(source,text):
# BUILDS TEHE COLOR OF THE BANNER
  nColor = makeColor(20,34,159)
# CYCLES THROUGH THE SOURCE PICTURE AND FILLS IN PIXELS WITH THE BANNER COLOR  
  for x in range(249, getWidth(source) - 251):
    for y in range(46,106):
      setColor(getPixel(source,x,y),nColor)
# PRINT TEXT IN THE BANNER      
  style = makeStyle(mono,italic + bold,54)
  offset = (len(text) / 2) * 30
  addTextWithStyle(source,(getWidth(source)/ 2) - offset,96,text,style,white)
  return source