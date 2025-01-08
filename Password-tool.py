
def intNumbers():
    "Ask for positive integer numbers"
    try:
        users = int(input(f"Enter a positive integer number : "))
        if type(users) == int and users > 0:
            #print(f'Numero ingresado {users}')
            return users
    except:
        print("Please, enter an integer positive number...")
        return intNumbers()

def validPositiveIntNumbers(users):
    "Valid a positive integer number"
    try:
        users = int(users)
        if type(users) == int and users > 0:  #print(f'Numero ingresado {users}')
            return users
        else:
            print("Please, enter an integer positive number higher than 0..")
            users = input(f"Enter a positive integer number : ")
            return validPositiveIntNumbers(users)
    except:
        print("Please, enter an integer positive number higher than 0....")
        users = input(f"Enter a positive integer number : ")
        return validPositiveIntNumbers(users)

def yesNo(message):
    "Get a message to print on terminal, y/n answer"
    try:
        option = input(f'{message} (y/n): ')
        option=option.lower()
        if type(option) == str and (option=="y" or option=="n"):
            print(f'{message} --> {option}')
            return option
        else:
            print("Please enter y/n option...")
            return yesNo(message)
    except:
        print("Please enter y/n option....")
        message = input(f"Enter y/n: ")
        return yesNo(message)

# Number of users (optional)
passwordQty = input(f'How many password: ')
passwordQty = validPositiveIntNumbers(passwordQty)
print(passwordQty)

# Load user data by file
userDataLoadByFile = yesNo("Load user data by file")
print(userDataLoadByFile)

# Save passwords to file
savePasswordToFile = yesNo("Save passwords to file")
print(savePasswordToFile)

# Send passwords by email
sendPasswordEmail = yesNo("Send password by email")
print(sendPasswordEmail)

# Print passwords on terminal
printPasswordToTerminal = yesNo("Print passwords to terminal")
print(printPasswordToTerminal)



userData = {'name':'','email':'','password': ''}
print
