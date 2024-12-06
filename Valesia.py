#Imports
import console
import userManagement
from userManagement import CheckAuthorization

# Login Config
PermitEmptyPassword = False
MinPasswordLength = 6
MaxRetries = 3

LoginConfig = userManagement.getConfig()
PermitEmptyPassword = LoginConfig.PermitEmptyPassword
MinPasswordLength = LoginConfig.MinPasswordLength
MaxRetries = LoginConfig.MaxRetries

Retries = 0
loginSucessful = False
userDetailsUpdate = False

while (not loginSucessful) and (Retries < MaxRetries):
    username = input("Enter your username: ")
    password = input("Please enter your password: ")
    if (password == "") and not PermitEmptyPassword:
        print("Empty Passwords are not permitted!")
    elif len(password) < MinPasswordLength:
        print("User Credentials do not meet requirements")
        loginSucessful = CheckAuthorization(username, password)
        if loginSucessful:
            userDetailsUpdate = True
    elif password != "":
        loginSucessful = CheckAuthorization(username, password)
    if (loginSucessful):
        print("Login Sucessful!")
        print("Welcome to Valesia Client")
        if (userDetailsUpdate):
            print("Some details for this account do not meet requirements")
            print("Please contact your system adminstrator to fix this")
        console.consoleExecute()
    else:
        print("User Credentials are incorrect")
        Retries += 1

if (Retries >= MaxRetries) and not loginSucessful:
    print("System Locked Down")
    print("Contact your system adminstrator inorder to regain access")