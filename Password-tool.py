
import string
import random
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

def passwordGenerate(length,specialSym,capsLetter,number,lower):
    """Password creation
    EDA List, random, randint """
    password = ""
    special = list(string.punctuation)
    caps = list(string.ascii_uppercase)
    digits = list(string.digits)
    lowercase = list(string.ascii_lowercase)
    matrix = [special,caps,digits,lowercase]
    specs = [specialSym,capsLetter,number,lower]
    print(specs)
    orden = 0
    for i in specs:
        while i > 0:
            password += matrix[orden][random.randint(0,len(matrix[orden]) )]
            print(password)
            i -= 1
        orden += 1
    print(password)

passwordGenerate(2,1,1,2,4)

#EDA: List of dictionaries & random selection
usersInformation =[]

# Load user data by file
userDataLoadByFile = yesNo("Load user data by file")
if userDataLoadByFile == 'n':
    # Number of users (optional)
    passwordQty = input(f'How many password: ')
    passwordQty = validPositiveIntNumbers(passwordQty)
    print(passwordQty)

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






"""special = list(string.punctuation)
    while specialSym > 0:
        password += special[random.randint(0,len(special))]
        specialSym -= 1

    caps = list(string.ascii_uppercase)
    while capsLetter > 0:
        password += caps[random.randint(0,len(caps))]
        capsLetter -= 1

    digits = list(string.digits)
    while number > 0:
        password += digits[random.randint(0,len(digits))]
        number -= 1

    lowercase = list(string.ascii_lowercase)
    while lower > 0:
        password += lowercase[random.randint(0,len(lowercase))]
        lower -= 1"""
