#CST205 Lab 13
#Team 1
#Craig Calvert, Samuel Pearce

# The Room class keeps track of the state of each room as well as references to nearby rooms
class Room:
    def __init__(self,name,description):
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
    return showInformation("*** Welcome to Northwestern Technology\'s Adventure Game *** "
                           "In this game you start in the backyard of a mysterious house. Your "
                           "goal is to find the riches and not die in the process. "
                           "Part of the game is to find what commands you can use. Try to "
                           "figure out what commands work using natural language. "
                           "\nHere are some commands to get you started. \n"
                           "Look, Go North, Go South, Inventory")
#Returns the name of the player 
def getPlayerName():
    showInformation("Thank you for playing our game. Before we begin may we please have your name?")
    name = requestString("Please enter your name.")
    showInformation("Thank you " + name + ". Please enjoy the game!")
    return name
    
# This is the main game entry point that loops while the game is being played.
def play():
    validDirections = ["north","n","south","s","east","e","west","w","up","u","down","d"]
    livingRoom = Room("Living Room", "There is an old TV with a cracked screen and a bookshelf with a collection of books. There is one book missing from the collection.")
    kitchen = Room("Kitchen","There is a table and chair, refridgerator and a stove here. There is a panel with a door on the wall.")
    backYard = Room("Back Yard", "There is a fence here with no gate and an old, rusty swingset.")# There is an open hatch with a ladder leading down.")
    bedroom = Room("Bedroom", "There is a bed with a stained mattress.")
    entryway = Room("Entry", "There is a chandelier and a door that is boarded shut.")
    basement = Room("Basement","It is dark here.")
    deathRoom = Room("Death Room","You have died.")
    garage = Room("Garage","There is an oil stain on the floor.")
    attic = Room("Attic", "This is the secret attic!")
    attic.addRoom("Down",garage)
    attic.items.append("Huge Diamond")
    kitchen.addRoom("North",backYard)
    kitchen.addRoom("South",livingRoom)
    kitchen.addRoom("East",garage)
    kitchen.items.append("sandwich")
    kitchen.allowedActions.append("sit")
    kitchen.allowedActions.append("open")

    garage.addRoom("West",kitchen)
    garage.items.append("Hammer")
    #garage.items.append("Key")

    backYard.addRoom("South",kitchen)
    backYard.allowedActions.append("unlock")
    backYard.allowedActions.append("open")

    livingRoom.addRoom("North",kitchen)
    livingRoom.addRoom("South",entryway)
    livingRoom.addRoom("West",bedroom)
    

    bedroom.addRoom("East",livingRoom)
    bedroom.allowedActions.append("sit")
    bedroom.items.append("Piggy Bank")
    bedroom.items.append("Book")

    entryway.addRoom("North",livingRoom)

    basement.addRoom("Up",backYard)
    basement.addRoom("North",deathRoom)
    basement.addRoom("South",deathRoom)
    basement.addRoom("East",deathRoom)
    basement.addRoom("West",deathRoom)
    
    currentRoom = backYard
    playerInventory = []
    #calls the getInstructions function with the new popup box
    getInstructions()
    #Assigns name the value entered in getPlayername
    name = getPlayerName()
    #print(getInstructions())
    # The panel exposes the switch
    kitchenPanelOpen = False
    # The switch turns on the basement light
    kitchenSwitchOn = False

    # The skeleton key unlocks the hatch in the back yard
    backYardHatchUnlocked = False
    
    # Once unlocked, the hatch can be opened
    backYardHatchOpen = False
    
    #This is a nested function since there are a couple
    #ways to break the piggy bank   
    def breakPiggyBank():
        #The piggy bank will be destroyed and a key will appear
        currentRoom.items.append("Broken Piggy Bank")
        currentRoom.items.append("Key")
        if("Piggy Bank" in playerInventory):
            playerInventory.remove("Piggy Bank")
        if("Piggy Bank" in bedroom.items):
            bedroom.items.remove("Piggy Bank")
        showInformation("You break the Piggy Bank with the hammer. A key falls out of it onto the floor.")

    # If the light is off in the basement and the user moves anywhere except
    # up, the user is eaten by a grue (game over -- lose)
    # If the basement light is on there is a bar of gold. If they take the gold game over/win

    # Game loop, exits on the following conditions:
    #   Game over (lost or won)
    #   User typed exit
    while(True):

        if(currentRoom.name=="Death Room"):
            showInformation(''' As you move in that direction the growls get louder. The last sensation you feel is yourself being eaten by a grue. \n
            You are dead. \n
            You have lost the game. ''')
            break
        if("Gold Bar" in playerInventory):
            if ("Huge Diamond" in playerInventory):
                showInformation("Congratulations! You have found the gold bar and won the game! \n You found the bonus item!")
            else:
                showInformation("Congratulations! You have found the gold bar and won the game! \n Next time, try to find the bonus item!!")
        #    print("Congratulations! You have found the gold bar and won the game!")
        #    if("Huge Diamond" in playerInventory):
        #        print("You found the bonus item!")
        #    else:
        #        print("Next time, try to find the bonus item!")
            break
        #showInformation('You are in the ' + currentRoom.name + ".")
        #input = requestString("\nWhat do you do?")
        input = requestString('Your are in the ' + currentRoom.name + '.\nWhat do you do?')
        #input = raw_input("\nWhat do you do? ")
        if(input==None):
            continue
        # All of the words will be split by space characters for parsing.        
        commands = input.split(" ")
        if(len(commands)==0):
            continue
        # Initially we just are concerned with the first command
        command = commands[0]
        if(command.lower()=="exit" or command.lower()=="quit"):
            break
        if(command.lower()=="help"):
            showInformation(getInstructions())
            continue
        # If the room allows it, let the user sit down.
        if(command.lower()=="sit"):
          if("sit" in currentRoom.allowedActions):
              showInformation("You are sitting down.")
          else:
              showInformation("There is nothing to sit on here!")
          continue
        if(command.lower()=="eat" and len(commands)>1):
            if(commands[1].lower()=="sandwich" and "sandwich" in playerInventory):
                showInformation("You take a bite out of the sandwich and just as you recognize the taste of cyanide, everything goes black. You are dead. You have lost the game.")
                break
        if(command.lower()=="read" and len(commands)>1):
            if(commands[1].lower()=="book" and "Book" in playerInventory):
                showInformation("The book is titled 'Climb Your Way to Riches' Written by: " + name + ". All the pages are blank.")
                continue
            else:
                showInformation("I can't read that.")
                continue

        if(command.lower()=="break" or command.lower()=="smash"):
            if("Hammer" in playerInventory and 
             (("Piggy Bank" in playerInventory) or ("Piggy Bank" in currentRoom.items)) and
             (len(commands)>4 and commands[1].lower()=="piggy" and commands[2].lower()=="bank" and commands[3].lower()=="with" and commands[4]=="hammer")):
                 breakPiggyBank()
                 continue
            if(len(commands)==3 and commands[1].lower()=="piggy" and commands[2].lower()=="bank"):
              showInformation("You need to use something to break it.")
              continue
            showInformation("I can't break that.")
            continue
        if(command.lower()=="open"):
          if(len(commands)==1):
              showInformation("What do you want me to open?")
              continue
          #Allow the piggy bank to be 'opened' with the hammer
          if((len(commands)==5) and ("Hammer" in playerInventory) and 
             (("Piggy Bank" in playerInventory) or ("Piggy Bank" in currentRoom.items)) and
             (commands[1].lower()=="piggy" and commands[2].lower()=="bank" and commands[3].lower()=="with" and commands[4]=="hammer")):
                 breakPiggyBank()
                 continue
          if(len(commands)==3 and commands[1].lower()=="piggy" and commands[2].lower()=="bank"):
            showInformation("You need to use something to open it.")
            continue
          if("open" in currentRoom.allowedActions):
              if(currentRoom.name == 'Kitchen' and commands[1].lower()=="panel"):
                if(not kitchenPanelOpen):
                    kitchenPanelOpen = True
                    showInformation("You opened the panel. There is a switch behind the panel.")
                    continue
                else:
                    showInformation("The panel is already open!")
                    continue
              elif(currentRoom.name == 'Back Yard' and commands[1].lower()=="hatch"):
                  if(not backYardHatchUnlocked):
                      showInformation("The hatch is locked.")
                      continue
                  if(not backYardHatchOpen):
                      backYardHatchOpen = True
                      showInformation("The hatch is now open.")
                      continue
                  else:
                      showInformation("The hatch is already open.")
                      continue
              showInformation("I don't know how to open that!")
              continue
        if(len(commands)>1 and commands[0]=="turn" and commands[1]=="on"):
           if(len(commands)==2):
               showInformation("What do you want to turn on?")
               continue
           elif(commands[2]=='switch' and
           currentRoom.name=="Kitchen"and 
           kitchenPanelOpen and kitchenSwitchOn == False):
               kitchenSwitchOn = True
               showInformation("The switch is on.")
               basement.items.append("Gold Bar")
               basement.description = "There pungent smell in the air"
               # Remove all the other deadly directions.
               basement.exits.clear()
               #Add the up direction back in.
               basement.addRoom("Up",backYard)
               continue
           else:
               showInformation("I don't know how to turn that on.")
               continue
        # Print information to the user about the current Room
        if(command.lower()=="look"):
            showInformation(currentRoom.description)
            if(currentRoom.name == "Basement"):
                if(kitchenSwitchOn):
                    showInformation("There is a gold bar on the floor.")
                else:
                    showInformation("It is very dark in here. You hear growling nearby.")
            elif(currentRoom.name == 'Back Yard'):
                if(backYardHatchOpen):
                    showInformation("There is an open hatch with a ladder leading down.")
                else:
                    showInformation("There is a closed hatch on the side of the house.")
            elif(currentRoom.name=="Kitchen" and kitchenPanelOpen):
                showInformation("The panel is open.")
            elif(currentRoom.name=="Kitchen" and kitchenSwitchOn):
                showInformation("The switch is in the on position.")
            if(len(currentRoom.items)):
                showInformation("You see the following items in this room:")
                for roomItem in currentRoom.items:
                    showInformation("\t" + roomItem)
            if(len(currentRoom.exits)>0):
                showInformation("You can go in the following directions:")
            for direction in currentRoom.exits.keys():
                if(len(direction)>1):
                    showInformation("\t" + direction)
            continue
        # Show the user which items they currently have.
        if(command.lower()=="inventory" or command.lower()=="i"):
            if(len(playerInventory)==0):
                showInformation("You do not have any items in your inventory.")
                continue
            showInformation("You have the following items:")
            for item in playerInventory:
                showInformation("\t" + item)
            continue
        if(command.lower()=="drop"):
            droppedSomething = False
            if(len(commands)>1):
                for item in playerInventory:
                    if(item.lower()==commands[1].lower()):
                        playerInventory.remove(item)
                        currentRoom.items.append(item)
                        showInformation("You have dropped " + item)
                        droppedSomething = True
                        break
                if(not droppedSomething):
                    showInformation("You don't have that.")
            else:
                showInformation("You need to tell me what to drop!")
            continue
        
        itemIndex = 0
        if(command.lower()=="put"):
            if(currentRoom.name=="Living Room" and
               len(commands)==4 and 
               commands[1].lower()=="book" and
               commands[2].lower()=="on" and
               (commands[3].lower()=="bookshelf" or commands[3].lower()=="shelf")):
               if ("Book" in playerInventory):
                 showInformation("You hear a clunking sound in a nearby room.")
                 garage.addRoom("Up",attic)
                 playerInventory.remove("Book")
                 garage.description + "\nA ladder hangs down from an open hatch above."
                 livingRoom.description = "There is an old TV with a cracked screen and a bookshelf with a collection of books."
                 continue
               else:
                 showInformation("You don't have a book")
                 continue
            showInformation("I can't put that there!")
            continue
        #Alias take and grab to get        
        if(command.lower()=="take"):
            command = "get"
        if(command.lower()=="grab"):
            command = "get"
        #Support the command 'get' and 'pick up'. Either works the same
        if((len(commands) > 1) and command.lower()=="get"):
            itemIndex = 1
        elif((len(commands)>2) and (commands[0].lower()=="pick") and (commands[1].lower()=="up")):
            itemIndex = 2
        if(itemIndex!=0):
            pickedSomethingUp = False
            for roomItem in currentRoom.items:
                #Handle single or multi-word item name (e.g. flashlight or 'baseball bat')
                getItem = ""
                for i in range(itemIndex,len(commands)):
                    if(len(getItem)>0):
                        getItem = getItem + " " + commands[i]
                    else:
                        getItem = commands[i]
                
                if(getItem.lower()==roomItem.lower()):
                    # Remove item from the room and add it to the inventorylook
                    playerInventory.append(roomItem)
                    currentRoom.items.remove(roomItem)
                    pickedSomethingUp = True
                    showInformation("You now have the " + roomItem + " in your inventory.")
                    break
            if(not pickedSomethingUp):
                showInformation("I can't find that to pick up.")
            continue
        if(currentRoom.name=="Back Yard" and (len(commands)>1) and command.lower()=="unlock" and commands[1].lower()=="hatch"):
            if(not "Key" in playerInventory):
                showInformation("You have nothing to unlock it with.")
                continue
            if(backYardHatchUnlocked):
                showInformation("The hatch is already unlocked.")
                continue
            else:
                backYardHatchUnlocked = True
                showInformation("You unlocked the hatch with the Key.")
                backYard.addRoom("Down",basement)
                continue
        # The old Zork Easter Egg
        if(command.lower()=="xyzzy"):
            showInformation("A hollow voice says 'fool'")
            continue
        # Shortcut so go north works
        if(command.lower()=="go" and len(commands)>1):
            command = commands[1]
        if(command.lower() in validDirections):
            newRoom = currentRoom.move(command)
            if(newRoom):
                currentRoom = newRoom
            else:
                showInformation("You can't go that way!")
        else:
            showInformation("I don't know how to do that. (Try 'look')")

        

play()
                                                                                                                                                                                                                                                