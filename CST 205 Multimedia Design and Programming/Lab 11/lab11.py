#CST205 Lab 11
#Team 1
#Brian Sheridan, Craig Calvert, Samuel Pearce, Kevin Bentley

class Room:

    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []
        self.allowedActions = []
    # A direction string and a room object it goes to.
    def addRoom(self, direction, room):
        self.exits[direction.lower()] = room
        #Add shortcut
        self.exits[direction[0:1].lower()] = room

    def move(self,direction):
        direction = direction.lower()
        if(direction in self.exits.keys()):
            return self.exits[direction]
        else:
            return None

def getInstructions():
    return '''
              Welcome to Northwestern Technology's Adventure Game (CST205 Lab 11)
              In this game you start in the back yard of a mysterious house. Your 
              goal is to find riches and not die in the process.
              Part of the game is to figure out what commands you can use. Try to
              figure out what commands work using natural language.Here are some 
              commands to get you started:
                Look
                Go North
                Go South
                Inventory
            '''


def play():
    livingRoom = Room("Living Room", "There is an old TV with a cracked screen.")
    kitchen = Room("Kitchen","There is a table and chair, refridgerator and a stove here.")
    backYard = Room("Back Yard", "There is a fence here with no gate and an old, rusty swingset. There is an open hatch with a ladder leading down.")
    bedroom = Room("Bedroom", "There is a bed with a stained mattress.")
    entryway = Room("Entry", "There is a chandelier and a door that is boarded shut.")
    basement = Room("Basement","It is dark here.")
    garage = Room("Garage","There is an oil stain on the floor.")
    kitchen.addRoom("North",backYard)
    kitchen.addRoom("South",livingRoom)
    kitchen.addRoom("Down",basement)
    kitchen.addRoom("East",garage)
    kitchen.items.append("sandwich")
    kitchen.allowedActions.append("sit")

    garage.addRoom("North",backYard)
    garage.addRoom("West",kitchen)
    garage.items.append("flashlight")

    backYard.addRoom("South",kitchen)
    backYard.addRoom("Down",basement)

    livingRoom.addRoom("North",kitchen)
    livingRoom.addRoom("South",entryway)
    livingRoom.addRoom("West",bedroom)

    bedroom.addRoom("East",livingRoom)
    bedroom.allowedActions.append("sit")

    entryway.addRoom("North",livingRoom)

    basement.addRoom("Up",backYard)

    currentRoom = backYard
    playerInventory = []
    print(getInstructions())
    while(True):
        print('You are in the ' + currentRoom.name + ".")
        input = requestString("\nWhat do you do?")
        if(input==None):
            continue
        commands = input.split(" ")
        if(len(commands)==0):
            continue
        command = commands[0]
        if(command.lower()=="exit"):
            break
        if(command.lower()=="help"):
            print(getInstructions())
            continue
        if(command.lower()=="sit"):
          if("sit" in currentRoom.allowedActions):
              print("You are sitting down")
          else:
              print("There is nothing to sit on here!")
          continue
        if(command.lower()=="look"):
            print(currentRoom.description)
            if(len(currentRoom.items)):
                print("You see the following items in this room:")
                for roomItem in currentRoom.items:
                    print("\t" + roomItem)
            if(len(currentRoom.exits)>0):
                print("You can go in the following directions:")
            for direction in currentRoom.exits.keys():
                if(len(direction)>1):
                    print("\t" + direction)
            print("")
            continue
        if(command.lower()=="inventory" or command.lower()=="i"):
            if(len(playerInventory)==0):
                print("You do not have any items in your inventory.")
                continue
            print("You have the following items:")
            for item in playerInventory:
                print("\t" + item)
            continue
        itemIndex = 0
        if((len(commands) > 1) and command.lower()=="get"):
            itemIndex = 1
        elif((len(commands)>2) and (commands[0].lower()=="pick") and (commands[1].lower()=="up")):
            itemIndex = 2
        if(itemIndex!=0):
            for roomItem in currentRoom.items:
                #Handle single or multi-word item name
                nameMatches = True
                for i in range(itemIndex,len(commands)):
                    if(roomItem.lower()!=commands[i].lower()):
                        nameMatches = False
                        break
                if(nameMatches):
                    #Remove item from the room and add it to the inventory
                    playerInventory.append(roomItem)
                    currentRoom.items.remove(roomItem)
                    print("You now have the " + roomItem + " in your inventory.")
                    break
            continue
        if(command.lower()=="xyzzy"):
            print("A hollow voice says 'fool'")
            continue
        newRoom = currentRoom.move(command)
        if(newRoom):
            currentRoom = newRoom
        else:
            print("You can't go that way!")
        

play()