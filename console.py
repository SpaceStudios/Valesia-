import userManagement
import time

#Global Variables
LoggedIn = False
CurrentUser = ""

class Command:
    def __init__(self, commandName, commandDescription, commandFunction, PermissionLevel): 
        self.commandName = commandName
        self.commandDescription = commandDescription
        self.commandFunction = commandFunction
        self.PermissionLevel = PermissionLevel

def logout(flags):
    LoggedIn = False
    return LoggedIn

def helpCommands(flags):
    for x in CommandList:
        print(x.commandName + " - " + x.commandDescription)
        
def registerUser(flags):
    userName = flags[0]
    userPassword = flags[1]
    userManagement.addUser(userName, userPassword)

def removeUser(flags):
    commandFlags = [
        "-rg" #Removes User Groups
    ]

def group(flags):
    if len(flags) > 0:
        possibleFlags = [
            "create",
            "add",
            "-c",
            "-a",
            "list",
            "-l"
        ]
        if flags[0] == possibleFlags[0] or flags[0] == possibleFlags[2]:
            if len(flags) > 2:
                flags.remove(flags[0])
                userManagement.createGroup(flags)
            else:
                print("Not enough data was provided inorder to create a group")
        elif flags[0] == possibleFlags[1] or flags[0] == possibleFlags[3]:
            if len(flags) > 1:
                print("Add User")
            else:
                print("Not enough data was provided inorder to create a user")
        elif flags[0] == possibleFlags[4] or flags[0] == possibleFlags[5]:
            flags.remove(flags[0])
            userManagement.listGroups(flags)
    else:
        print("Not enough flags provided")

CommandList = [
    Command("adduser", "adds a user to the system", registerUser, 1),
    Command("deluser", "removes a user from the system", userManagement.delUser, 1),
    Command("logout", "Logout from the system", logout, 20),
    Command("help", "shows commands", helpCommands, 20),
    Command("listusers", "list all users on the system", userManagement.listUsers, 10),
    Command("group", "creates and modifies groups", group, 1)
]

def RegisterCommand(commandName, commandDescription, commandFunction, commandPermissionLevel):
    CommandList.append(Command(commandName, commandDescription, commandFunction, commandPermissionLevel))
    
def checkCommand(command):
    commandExists = False
    for x in CommandList:
        if commandExists == False:
            if command == x.commandName:
                commandExists = True
    return commandExists

def getCommand(command):
    for x in CommandList:
        if command == x.commandName:
            return x

def consoleExecute():
    LoggedIn = True
    while LoggedIn:
        commandInput = input()
        commandTable = commandInput.split()
        commandExists = checkCommand(commandTable[0])
        if commandExists:
            command = getCommand(commandTable[0])
            commandName = commandTable[0]
            commandTable.remove(commandTable[0])
            result = command.commandFunction(commandTable)
            if commandName == "logout":
                LoggedIn = result
        time.sleep(1/60)