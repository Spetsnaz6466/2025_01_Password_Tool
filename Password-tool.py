
"""
# Password creation tool
# input number of: Special chars(specialSym), capital letters (capsLetter), numbers (number) and lover case letters(lower)
# Password length = specialSym + capsLetter + number + lower
"""
import string, csv, random, os,sys

def intNumber():
    """
    # Ask for positive integer number until get it
    """
    try:
        users = int(input(f"Enter a positive integer number : "))
        if type(users) == int and users > 0:
            return users
    except:
        print("Please, enter an positive integer number...")
        return intNumber()

def validatePositiveIntNumbers(users):
    """
    # Valid if a given number is integer and positive
    """
    try:
        users = int(users)
        if type(users) == int and users > 0:  #print(f'Numero ingresado {users}')
            return users
        else:
            print("Please, enter an integer positive number ")
            users = input(f"Enter a positive integer number : ")
            return validatePositiveIntNumbers(users)
    except:
        print("Please, enter an integer positive number higher than 0....")
        users = input(f"Enter a positive integer number : ")
        return validatePositiveIntNumbers(users)

def yesNo(message):
    """
    # Get a message to print on terminal asking for a y/n answer
    """
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

def passwordConfiguration():
    print("\n/* Password security requirements */")
    specialSym = int(input("1. Qty of Special Symbols: "))
    capsLetter = int(input("2. Qty of Capital letters: "))
    number     = int(input("3. Qty of numbers: "))
    lower      = int(input("4. Qty of lower case letters: "))
    return specialSym,capsLetter,number,lower

def passwordGenerate(specialSym,capsLetter,number,lower):
    """
    # Password creation tool
    # input number of: Special chars(specialSym), capital letters (capsLetter), numbers (number) and lover case letters(lower)
    # Password length = specialSym + capsLetter + number + lower
    """
    password = ""
    lowercase = list(string.ascii_lowercase)
    caps = list(string.ascii_uppercase)
    digits = list(string.digits)
    special = list(string.punctuation)
    matrix = [special,caps,digits,lowercase]

    specs = [specialSym,capsLetter,number,lower]
    orden = 0
    for i in specs:
        while i > 0:
            password += matrix[orden][random.randint(0,len(matrix[orden])-1) ]
            i -= 1
        orden += 1
    #print("PASSWORD ---> ",password)
    return password

def _loadCSV_UserData(file)-> dict:
    """
    This function opens a file returning user information as dictionary
    """
    _buffer = {}
    with open(file) as file0:
        file1 = csv.DictReader(file0)
        a=0
        for i in file1:
            _buffer[a] = {'User': i['User'],'Email' :i['Email']}
            a += 1
    return _buffer

def savePasswordsOnFile(_dict, outputFile,_keyNames,usersInformation):
    with open(outputFile,"w") as salida0:
        salida1 = csv.DictWriter(salida0, fieldnames= _keyNames)
        salida1.writeheader()
        for i in usersInformation:
            salida1.writerow(usersInformation[i])

def noFileChoice():
    """
    Print passwords on terminal
    """
    passwordQty = input(f'How many password: ')
    passwordQty = validatePositiveIntNumbers(passwordQty)
    print(passwordQty)
    specialSym,capsLetter,number,lower = passwordConfiguration()
    while(passwordQty > 0):
        _passwordNoFile= passwordGenerate(specialSym,capsLetter,number,lower)
        print(f'Password {passwordQty}:  {_passwordNoFile}')
        passwordQty -=1

def yesFileChoice(file):
    """
    Print passwords on terminal and file
    """
    specialSym,capsLetter,number,lower = passwordConfiguration()
    os.system("clear")
    usersInformation = _loadCSV_UserData(file)
    for i in usersInformation:
        _keyNames = usersInformation[0].keys()
        _password = passwordGenerate(specialSym,capsLetter,number,lower)
        usersInformation[i]["Password"] = _password
        print(usersInformation[i])
    #print(_keyNames); print("Users Information"); print(usersInformation)
    outputFile = input("\nInput Output CSV file name: ")
    outputFile = "Output_" + outputFile + ".csv"
    savePasswordsOnFile(usersInformation, outputFile,_keyNames,usersInformation)
    print(f'Information saved on: {outputFile}')

if __name__ == "__main__":
    if len(sys.argv) >1:
        os.system("clear")
        file = sys.argv[1]
        print("\nDirectory files:")
        os.system("ls")
        yesFileChoice(file)
    else:
        os.system("clear")
        userDataLoadByFile = yesNo("\nLoad user data by CSV file")
        if userDataLoadByFile == 'n':
            noFileChoice()
        else:
            os.system("clear")
            print("Files on the curren working directory:\n")
            os.system("ls -lsa")
            file = input("\nIngrese file con user data: ")
            yesFileChoice(file)
