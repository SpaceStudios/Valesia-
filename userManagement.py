class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.PermissionLevel = 20
        self.GroupTable = []
    def addGroup(group):
        self.GroupTable.append(group)
        print(self.GroupTable)
        
class LoginConfig:
    def __init__(self, PermitEmptyPassword, MinPasswordLength, MaxRetries):
        self.PermitEmptyPassword = PermitEmptyPassword
        self.MinPasswordLength = MinPasswordLength
        self.MaxRetries = MaxRetries
        
class Group:
    def __init__(self, GroupName, PermissionLevel, userList):
        self.GroupName = GroupName
        self.PermissionLevel = PermissionLevel
        self.userList = userList
    def addUser(self, userExecuted):
        self.userList.append(userExecuted)
        userExecuted.GroupTable.append(self)

# Login Config
PermitEmptyPassword = False
MinPasswordLength = 6
MaxRetries = 3

def getConfig():
    return LoginConfig(PermitEmptyPassword, MinPasswordLength, MaxRetries)


authorizedUsers = [
    User("Admin101", "Test12345"),
    User("User01", "12345"),
    User("User02", "12345"),
    User("User03", "12345"),
    User("User04", "12345"),
    User("User05", "12345"),
]

systemGroups = [
    Group("Root", 0, [User("root", "root")]),
    Group("Users", 15, authorizedUsers),
    Group("Administrators", 0,[authorizedUsers[0]])
]

def CheckAuthorization(username, password):
    found = False
    for user in authorizedUsers:
        if found == False:
            found = (username == user.username and password == user.password)
    return found
    
def addUser(username, password):
    usernametaken = False
    for x in authorizedUsers:
        if x.username == username:
            usernametaken = True
    if usernametaken:
        print("Error while trying to create user, "+username+" is already in use!")
    else:
        authorizedUsers.append(User(username, password))
        print(username+" has sucessfully been created!")

def delUser(flags):
    if len(flags) > 0:
        username = flags[0]
        usersremoved = 0
        for x in authorizedUsers:
            if x.username == username:
                authorizedUsers.remove(x)
                usersremoved += 1
        print("Sucessfully removed "+str(usersremoved)+" users")
    else:
        print("You failed to provide enough arguements to execute this command")

def createGroup(flags):
    if len(flags) >= 2:
        groupName = flags[0]
        PermissionLevel = int(flags[1])
        exists = groupExists(groupName)
        if exists:
            print("A group with this name already exists try to name this something else")
        else:
            systemGroups.append(Group(groupName, PermissionLevel, []))
            print("Group "+groupName+" has sucessfully been created!")
    else:
        print("not enough data have been provided")
    
def groupExists(groupName):
    found = False
    for x in systemGroups:
        if x.GroupName == groupName:
            found = True
    return found

def listGroups(flags):
    for x in systemGroups:
        print(x.GroupName)

def CheckUserPermissionLevel(username):
    currentUser = findUser(username)
    if currentUser != None:
        print(currentUser.PermissionLevel)
    
def findUser(username):
    found = False
    for x in authorizedUsers:
        if x.username == username:
            if not found:
                found = True
                return x
    if not found:
        return None
    
def listUsers(flags):
    Errors = []
    PossibleSelectors = []
    Selectors = []
    for x in authorizedUsers:
        print(x.username) 