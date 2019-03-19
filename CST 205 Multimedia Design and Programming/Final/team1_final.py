#CST205 Final Project
#Team 1
#Brian Sheridan, Kevin Bentley, Craig Calvert, Samuel Pearce

import os

'''
Media resources:

Icons: https://icomoon.io/
Sounds: http://soundbible.com

Photos: https://www.flickr.com/photos/shantideva/2580811889/in/photostream/

'''
# The root path for all of the media files.
rootFilePathName = os.path.dirname(__file__)
# The main picture for the app. This will never be reassigned 
mainWindow = makeEmptyPicture(480,560,makeColor(255,255,255))
show(mainWindow)

def pyCopy(source, target, targetX, targetY):
    copyInto(source, target, targetX, targetY)
    
# Build Inventory list      
def inventoryIcons(inventory,picture):
  for x in range(0,480):
    for y in range(481,560):
     pixel = getPixel(picture,x,y)
     setColor(pixel,white)
  t = 0
  addText(picture,120, 490,'---------------------- Inventory ----------------------')
  for item in inventory:
    if((item).iconPicture != None):
        greenScreen(picture,(item).iconPicture,t*60,500)
        t+=1
  return picture
  
# Greenscreen rendering  
def greenScreen(backGround, foreGround, targetX, targetY):
  greenScreen = makeColor(0,255,0)
  shadow = makeColor(33,29,22)
  for x in range(0, getWidth(foreGround)-1):
    for y in range(0, getHeight(foreGround)-1):
      picPixel = getPixel(foreGround,x, y)
      newPixel = getPixel(backGround,targetX + x ,targetY + y)
      color = getColor(picPixel)
      if distance(color,greenScreen) > 140:
        setColor(newPixel,color)
  return backGround
# All game states will be stored here
class GameState:
  def __init__(self):
    self.bottleOnScale = False
    self.playerWon = False
    self.playerDied = False
    self.bottleOpen = False
    self.drawerOpen = False

class Player:
  def __init__(self,name):
    self.inventory = []
    self.name = name
  def getItem(self, itemName):
      for item in self.inventory:
        if(item.name.lower()==itemName.lower()):
          return item
      return None

class InventoryItem:
  def __init__(self,name,iconFile, description):
    global rootFilePathName;
    # The name to display
    self.name = name
    # This will show when the user picks it up
    self.description = description
    # The file name for the icon
    self.iconFile = iconFile
    if(iconFile != None):
      # JES Picture object
      self.iconPicture = makePicture(os.path.join(rootFilePathName,"inventory_icons",iconFile))
    else:
      self.iconPicture = None
    self.actionFunction = None
# The Room class keeps track of the state of each room as well as references to nearby rooms
class Room:

    def __init__(self,name,description, pictureFileName):
        global rootFilePathName;
        # The name of the room that is displayed automatically with each command
        self.name = name
        # The description you see when you type look
        self.description = description
        # A dictionary where the key is the direction and the value is another Room object
        self.exits = {}
        # A list of objects currently in the room. The objects are just strings
        self.items = []
        # Actions (strings) that are allowed in this room, such as sit, turn on light, etc.
        self.allowedActions = []
        # File name with the picture for the room
        self.pictureFileName = pictureFileName
        if(pictureFileName != None):
          # JES Picture Object
          self.picture = makePicture(os.path.join(rootFilePathName,"room_pictures",pictureFileName))
        else:
          self.picture = None
        self.roomActionFunction = None

    def getItem(self, itemName):
      for item in self.items:
        if(item.name.lower()==itemName.lower()):
          return item
      return None

    # A direction string and a room object it goes to.
    # Each direction will also add a shortcut (E.g. North will add a shortcut of N)
    # Directions are case insensitive
    def addRoom(self, direction, room):
        self.exits[direction.lower()] = room
        #Add shortcut
        self.exits[direction[0:1].lower()] = room

    # Attempt to move in a direction. If there is a valid room in that direction
    # return a Room object. If it isn't a valid direction, return None, meaning
    # The player cannot go that way.
    def move(self,direction):
        direction = direction.lower()
        if(direction in self.exits.keys()):
            return self.exits[direction]
        else:
            return None
# Returns the instructions to print at the start or when 'help' is typed.
def getInstructions():
  return ("Part of the game is to figure out what commands you can use. Try to "
         "figure out what commands work using natural language. Here are some "
         "commands to get you started:\n"
         "Look\n"
         "North\n"
         "South\n"
         "Inventory\n")

#import console
def getGameInput(msg):
    inputStr = requestString(msg)
    #input = raw_input(msg)
    #inputStr = input()
    return inputStr

def displayGameText(msg):
    #print(msg)
    showInformation(msg)

def getName():
  inputStr = requestString("What is your name?")
  return inputStr

def clip(source,start,end):
  newSound = makeEmptySound(end-start,int(getSamplingRate(source)))
  newPosition = 0
  for i in range(start,end):
    sample = getSampleObjectAt(source,i)
    newSample = getSampleObjectAt(newSound,newPosition)
    sampleValue = getSampleValue(sample)
    setSampleValue(newSample,sampleValue)
    newPosition = newPosition + 1
  return newSound

def getFoolSound():
    theSound = makeSound(os.path.join(rootFilePathName,"sounds","LOTR Fool.wav"))
    clippedSound = clip(theSound,2679256,2703500)
    clippedSound.play()

def officeActions(room, gameState, player, commands):
  def showDeskDescription():
    displayGameText("You see that one of the drawers is ajar. The typewriter on the desk is an "
                      "old 'Smith Corona.' You notice that the keys for 'A', 'C', 'E', 'L', and 'S' are all missing.")

  if(len(commands)>1):
    if((commands[0]=='examine' or commands[0]=='view') and commands[1]=='desk'):
      showDeskDescription()
      return True
    if(commands[0]=='open' and (commands[1]=='desk' or commands[1]=='drawer') and gameState.drawerOpen == False):
      gun = InventoryItem("Gun","Gun.jpg","Locked and loaded!")
      room.items.append(gun)
      displayGameText("You open the desk drawer and find an old revolver. Upon closer inspection you find that it only has two bullets.")
      return True
  if(len(commands)>1):
    if(commands[0]=='look' and commands[1]=='at' and commands[2]=='desk'):
      showDeskDescription()
      return True
  return None

def foyerActions(room, gameState, player, commands):
  if(len(commands)>1):
    if(commands[0]=='open' and commands[1]=='door'):
      if(gameState.bottleOnScale):
        displayGameText("The door opens and you feel a cool refreshing breeze. As you step outside you feel a sense of relief at escaping.\n"
                         "Congratulations, you have won the game!")
        gameState.playerWon = True
        return True
      else:
        displayGameText("The door appears to be locked, but you don't see any keyhole or lock mechanism on the door.")
        return True
  return None

def basementActions(room, gameState, player, commands):
  # Assume that the commands are all lower case
  if( (len(commands) > 2 and commands[0] == 'look' and (commands[1] == 'in' or commands[1] == 'at') and commands[2] == 'crypt') or
    (len(commands) > 1 and commands[0] == 'examine' and commands[1] == 'crypt')):
      displayGameText("You see what appears to be, by his clothing, a young male lying on "
                      "his back in the crypt. From the looks of it he has been dead for "
                      "quite some time now. The material from his shirt is missing over "
                      "his left breast...matching the size and style of the fabric you "
                      "woke up with in your right hand.")
      return True
  return None

def storageActions(room, gameState, player, commands):
    if(len(commands)>1):
        if(commands[0]=='open' and commands[1]=='window'):
            displayGameText("With great difficulty you manage to slide the window open."
                            " As it opens, thousands of large spiders stream in, and swarm over your body."
                            " You don't know which is worse, the pain of a thousands of spider bites, or the sudden "
                            " realization that you have a phobia of spiders.")
            gameState.playerDied = True
            deathSound = makeSound(os.path.join(rootFilePathName,"sounds","DeathSound.wav"))
            if(deathSound!=None):
                deathSound.play()            
            return True
    return None


def scaleActions(room, gameState, player, commands):
    if(len(commands)>3):
        if((commands[0]=='put' or commands[0]=='place') and commands[1]=='bottle' and commands[2]=='on' and commands[3]=='scale'):
            bottleItem = player.getItem("bottle")
            if(bottleItem==None):
                displayGameText("You don't have a bottle.")
                return True
            else:
                gameState.bottleOnScale = True
                player.inventory.remove(bottleItem)
                deathSound = makeSound(os.path.join(rootFilePathName,"sounds","SqueakingSound.wav"))
                deathSound.play()
                inventoryIcons(player.inventory,mainWindow)
                repaint(mainWindow)
                displayGameText("You place the bottle on the scale. The scale moves down slightly and you hear a distant creaking sound.")
                return True
    return None

def bedroom1Actions(room, gameState, player, commands):
    if(len(commands)>1):
        if(commands[0]=='open' and commands[1]=='window'):
            displayGameText("The window won't budge.")
    return None

def parseGet(room, gameState, player, commands):
  itemIndex = 0
  command = commands[0]
  #Alias take and grab to get 
  #Support the command 'get' and 'pick up'. Either works the same       
  if(command.lower()=="take"):
      command = "get"
  if(command.lower()=="grab"):
      command = "get"
  if(len(commands)<2):
    return None
  if(command != "get"):
    return None
  itemIndex = 1
  if(len(commands)>2 and commands[0]=='pick' and commands[1]=='up'):
    itemIndex = 2
  itemName = reassembleCommand(commands,itemIndex)
  
  item = room.getItem(itemName)
  if(item==None):
    displayGameText("I can't find that to pick up.")
    return True
  else:
    # Remove item from the room and add it to the inventorylook
    player.inventory.append(item)
    room.items.remove(item)
    inventoryIcons(player.inventory,mainWindow)
    repaint(mainWindow)
    if(item.description != None):
      displayGameText(item.description)
    else:
      displayGameText("You now have the " + item.name + " in your inventory.")
    return True
  return None

# This function builds a single string from the previously parsed commands.
# This allows us to parse, for example, the first two words as commands, and
# then treat the rest of the text as a single 'object'. E.g. take Typewriter 
# Keys vs pick up Typewriter Keys
def reassembleCommand(commands,index):
  command = ""
  for i in range(index,len(commands)):
    if(i!=index):
      command += " "
    command += commands[i]
  return command

# This is the main game entry point that loops while the game is being played.
def play():
    global rootFilePathName;
    validDirections = ["north","n","south","s","east","e","west","w","up","u","down","d","u","under"]
    
    basement = Room("Basement",
                    "The room is long and narrow with a doorway located at the north end. "
                    "To your right the wall looks like something from an old mausoleum. "
                    "One of the doors has been pried off and you see a pair of feet "
                    "sticking out of where the door once was.",
                    "basement.jpg")
    basement.roomActionFunction = basementActions

    lowerStairway = Room("Stairway",
                     "There is a stairway leading up. To the east is a doorway leading to an outdoor courtyard.",
                     "stairway_courtyard.JPG")

    courtyard = Room("Courtyard",
                     "As you step through the doorway to the courtyard you fail to see the man step out of "
                     "the second courtyard doorway to your right. The ground rushes up toward your face "
                     "shortly after the sharp pain in your back. The ground ends up being the last thing you see...ever.",
                     "death_stairway_courtyard.png")
    foyer = Room("Foyer",
                 "Straight ahead of you is what appears to be the front door to the house. To the left and to "
                 "the right of you are doorways to other rooms.",
                 "foyer.JPG")
    foyer.roomActionFunction = foyerActions

    office = Room("Office",
                  "You are standing in what looks like it used to be a personal office. Pushed against one of "
                  "the walls is a desk with an old typewriter on it.",
                  "Office.JPG")
    office.roomActionFunction = officeActions
                                         
    stairway = Room("Stairway",
                    "Before you is a stairway leading upstairs. You also notice a little farther down, just "
                    "underneath the stairs, is another doorway.",
                    "stairway.JPG")

    storage = Room("Storage Room",
                   "This room appears to be a storage room full of bottles and jars. Two items stand out to you. "
                   "A bottle sitting on a chair in the middle of the room and a jar that is precariously balanced "
                   "on a piece of wood to your right.",
                   "storage.JPG")
    storage.roomActionFunction = storageActions

    bottle = InventoryItem("Bottle","Bottle.jpg","The label says 'Smith Corona' and, rather oddly, "
                                         "the bottle is corked and has what looks to be five typewriter keys in it.")
    jar = InventoryItem("Jar","Jar.jpg","Through the liquid inside you can see what looks like a "
                                   "house key lying on the bottom of the jar.")
    storage.items.append(bottle)
    storage.items.append(jar)

    scale = Room("Scale Room",
                 "At the top of the stairs you find yourself standing in a room with a doorway to your left and "
                 "a doorway to your right. In the middle of the room is a scale that appears to many, many years old.",
                 "scale_room.JPG")
    scale.roomActionFunction = scaleActions
    bedroom1 = Room("Bedroom #1",
                    "You are standing in someone's bedroom. Yesterday's clothes appear to be laid on a chair next to "
                    "the bed. On the bed is a newspaper next to a bottle of whiskey.",
                    "bedroom_1.JPG")
    whiskey = InventoryItem("Whiskey","Whiskey.jpg","It looks like whiskey all right.")
    newspaper = InventoryItem("Newspaper","Newspaper.jpg","The newspaper is from The Harrodsburg Herald, which you have never heard "
                              "of and have never been to. Dated January of this year, an article just below the fold on "
                              "the front page catches your eye. In it the article tells the story of Brandon Lawson and "
                              "how he disappeared without a trace five years ago.")
    bedroom1.items.append(whiskey)
    bedroom1.items.append(newspaper)


    bedroom2 = Room("Bedroom #2",
                    "You are standing in what is a bedroom, but it doesn't seem that anybody is using it anymore. "
                    "Other than a rancid odor, you notice a book lying on the floor and a tie running from the top "
                    "of a blood stained mattress to the floor.",
                    "bedroom_2.JPG")
    tie = InventoryItem("Tie","Tie.jpg","This really doesn't go with what you are wearing.")
    book = InventoryItem("Book","Book.jpg","There is a bookmark marking a place in the book.")
    bedroom2.items.append(tie)
    bedroom2.items.append(book)

    basement.addRoom("North",lowerStairway)
    lowerStairway.addRoom("South",basement)
    lowerStairway.addRoom("East",courtyard)# This is a 1 way journey

    lowerStairway.addRoom("Up",foyer)
    foyer.addRoom("Down",lowerStairway)

    foyer.addRoom("West",office)
    office.addRoom("East",foyer)

    foyer.addRoom("East",stairway)
    stairway.addRoom("West",foyer)

    stairway.addRoom("Down",storage)
    stairway.addRoom("Under",storage)
    storage.addRoom("Up",stairway)

    stairway.addRoom("Up", scale)
    scale.addRoom("Down",stairway)

    scale.addRoom("West",bedroom1)
    bedroom1.addRoom("East",scale)

    scale.addRoom("East",bedroom2)
    bedroom2.addRoom("West",scale)

    currentRoom = basement
    
    displayGameText(getInstructions())

    playerName = getName()
    player = Player(playerName)
    nameTag = InventoryItem("Name Tag","NameTag.jpg","This is a light blue fabric with a name tag pinned to it. The name tag says 'Brandon.'")#"nametag.png")    
    player.inventory.append(nameTag)
    if(currentRoom.picture!=None):
      pyCopy(currentRoom.picture,mainWindow,0,0)
      inventoryIcons(player.inventory,mainWindow)
      repaint(mainWindow)

    gameState = GameState()
    
    displayGameText("You wake up in a room lying on your back. Your head is pounding "
                     "and you have no idea where you are or how you got here. In your right"
                     " hand you are clutching a piece of light blue fabric with a name tag"
                     " pinned to it. The name tag says 'Brandon'.")

    storageDeathPicture = makePicture(os.path.join(rootFilePathName,"room_pictures","death_storage.jpg"))
    # Game loop, exits on the following conditions:
    #   Game over (lost or won)
    #   User typed exit
    while(True):
        if(currentRoom == storage and gameState.playerDied == True):
            deathSound = makeSound(os.path.join(rootFilePathName,"sounds","deathSound.wav"))
            deathSound.play()
            pyCopy(storageDeathPicture,mainWindow,0,0)
            repaint(mainWindow)
            displayGameText(courtyard.description + "\nYou have died.")
        if(currentRoom == courtyard):            
            deathSound = makeSound(os.path.join(rootFilePathName,"sounds","deathSound.wav"))
            deathSound.play()
            displayGameText(courtyard.description + "\nYou have died.")
            break
        if(gameState.playerDied):
          displayGameText("You lost the game.")
          break
        # Check for win condition
        if(gameState.playerWon):
          displayGameText("You won the game!")
          break
        print('You are in the ' + currentRoom.name + ".")
        input = getGameInput("\nWhat do you do? ")
        print(input)
        if(input==None):
          continue
        input = input.lower()
        # All of the words will be split by space characters for parsing.        
        commands = input.split(" ")
        if(len(commands)==0):
            continue

        #Execute room specific commands
        if(currentRoom.roomActionFunction != None):
          results = currentRoom.roomActionFunction(currentRoom, gameState, player, commands)
          if(results == True):
            continue
          if(results == False):
            break # You are dead
          #If none, continue parsing.

        # Initially we just are concerned with the first command
        command = commands[0]
        if(command.lower()=="exit" or command.lower()=="quit"):
            break
        if(command.lower()=="help"):
            print(getInstructions())
            continue
        
        if(len(commands) > 1 and (command=="shoot" or command=='fire') and commands[1]=='gun'):            
            gunClick = makeSound(os.path.join(rootFilePathName,"sounds","GunJam.wav"))
            gunClick.play()
            displayGameText("The gun jams!")
            continue
        # Print information to the user about the current Room
        if(command.lower()=="look"):
          if((len(commands)==1) or 
            (len(commands)==3 and commands[1]=="at" and commands[2]=="room")):
              lookString = currentRoom.description + "\n"
              
              if(len(currentRoom.items)):
                  lookString += "You see the following items in this room:\n"
                  for roomItem in currentRoom.items:
                      lookString += "\t" + roomItem.name + "\n"
              lookString += "\n"
              if(len(currentRoom.exits)>0):
                  lookString += "You can go in the following directions:\n"
              for direction in currentRoom.exits.keys():
                  if(len(direction)>1):
                      lookString += ("\t" + direction) + "\n"
              displayGameText(lookString)
              continue
          if(len(commands)>2 and commands[1]=="at"):
            itemName = reassembleCommand(commands,2)
            item = currentRoom.getItem(itemName)
            if(item==None):
              item = player.getItem(itemName)
            if(item!=None):
              displayGameText(item.description)
              continue
            else:
              displayGameText("You don't see that.")

        # Show the user which items they currently have.
        if(command.lower()=="inventory" or command.lower()=="i"):
            if(len(player.inventory)==0):
                displayGameText("You do not have any items in your inventory.")
                continue
            inventoryString = "You have the following items:"
            for item in player.inventory:
                inventoryString = inventoryString + "\t" + item.name + "\n"
            displayGameText(inventoryString)
            continue
        if(len(commands)>3):
            if((commands[0]=='put' or commands[0]=='place') and commands[1]=='bottle' and commands[2]=='on' and commands[3]=='scale'):
                if(currentRoom!=scale):
                    displayGameText("There isn't a scale here!")
                    continue
        if(len(commands)>1):
          if(commands[0]=='drink' and commands[1]=='whiskey'):
            if(whiskey in player.inventory):                
                player.inventory.remove(whiskey)
                whiskeySound = makeSound(os.path.join(rootFilePathName,"sounds","DrinkingWhiskey.wav"))
                whiskeySound.play()
                displayGameText("That seems to help your stress level go down.")
                inventoryIcons(player.inventory,mainWindow)
                repaint(mainWindow)
            else:
                displayGameText("Sadly, you don't have any.")
            continue
          if(commands[0]=='open' and commands[1]=='jar'):
            if(jar in player.inventory):
              displayGameText("You pick up the jar and unscrew the lid. You smell a strange odor as the room begins to spin. "
                              "You eventually wake up to find yourself in complete darkness, your new roommate is Brandon. "
                              "Other than the owner of the house, nobody ever hears your screams.")
              gameState.playerDied = True;
              deathSound = makeSound(os.path.join(rootFilePathName,"sounds","DeathSound.wav"))
              deathSound.play()
              pyCopy(storageDeathPicture,mainWindow,0,0)
              repaint(mainWindow)
              break;
          if(commands[0]=='open' and commands[1]=='bottle'):
            if(bottle in player.inventory):
              if(gameState.bottleOpen):
                displayGameText("The bottle is already open.")
                continue
              theSound = makeSound(os.path.join(rootFilePathName,"sounds","TyperWriterKeys.wav"))
              theSound.play()
              displayGameText("You open the bottle and five 'Typewriter Keys' fall to the floor,"
                              " crumbling to dust instantly.")
              typewriterKeys = InventoryItem("Typewriter Keys",None,"Five Typewriter Keys")
              currentRoom.items.append(typewriterKeys)              
              bottle.description = "The label says 'Smith Corona.' The bottle is open and empty."
              gameState.bottleOpen = True
              continue;
            else:
              displayGameText("You don't have that.")
              continue

        if(len(commands)>1 and command.lower()=="read" and commands[1]=="book"):
          if(book in player.inventory):
            displayGameText("You open the book where the bookmark is marking the place of whoever was "
                            "last reading it. There are three columns of text. The first column of "
                            "text contains names of people, while the second and third columns contain "
                            "dates. At the bottom of the first column you are surprised to see the name " + player.name +
                            " with today's date next to it. It's only then that you notice that "
                            "the first column is labeled 'guest', and the second and third columns "
                            "are labeled 'date abducted', and 'date interred' respectively.")
          else:
            displayGameText("You don't have a book to read.")
          continue          
        if(command.lower()=="drop"):
            droppedSomething = False
            if(len(commands)>1):
                for item in player.inventory:
                    if(item.name.lower()==reassembleCommand(commands,1).lower()):
                        player.inventory.remove(item)
                        currentRoom.items.append(item)
                        inventoryIcons(player.inventory,mainWindow)
                        repaint(mainWindow)
                        displayGameText("You have dropped " + item.name)
                        droppedSomething = True
                        break
                if(not droppedSomething):
                    displayGameText("You don't have that.")
            else:
                displayGameText("You need to tell me what to drop!")
            continue
                
        if(parseGet(currentRoom, gameState, player, commands)==True):
          continue

        # The old Zork Easter Egg
        if(command.lower()=="xyzzy"):
            getFoolSound()
            displayGameText("A hollow voice says 'fool'")
            continue
        if(command.lower()=="die"):            
            gameState.playerDied = True
            deathSound = makeSound(os.path.join(rootFilePathName,"sounds","DeathSound.wav"))
            if(deathSound!=None):
                deathSound.play()
            pyCopy(storageDeathPicture,mainWindow,0,0)
            repaint(mainWindow)
            displayGameText("ok.")
            continue
        # Shortcut so go north works
        if(command.lower()=="go" and len(commands)>1):
            command = commands[1]
        if(command.lower() in validDirections):
            newRoom = currentRoom.move(command)
            if(newRoom):
                currentRoom = newRoom
                # Copy pixels over for this room to mainWindow
                if(currentRoom.picture!=None):
                  pyCopy(currentRoom.picture,mainWindow,0,0)
                  repaint(mainWindow)

            else:
                displayGameText("You can't go that way!")
        else:
            displayGameText("I don't know how to do that. (Try 'look')")

splashscreen = makePicture(os.path.join(rootFilePathName,"room_pictures","splashscreen.png"))

pyCopy(splashscreen,mainWindow,0,0)
repaint(mainWindow)
play()