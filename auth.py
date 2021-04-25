import random
database = {} #dictonary

#Initializing the system
def init():
    print("Welcome to PythonBank")
    haveAccount = int(input("Do you have an account with us: 1 (Yes) 2 (No) \n"))

    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        print(register())
    else:
        print("You have selected invalid option")
        init()

#login
#- account number & password
def login():
    print("****** Login to Your Account ******")

    accountNumberFromUser = int(input("What is Your AccountNumber? \n"))
    password = input("What is your password \n")

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
                

    print("Invalid account or password")
    login()

    
#register
#- first name, last name, password, email
def register():
    print("****** Register ******")
    first_Name = input("What is your First name? \n")
    last_Name = input("What is your Last name? \n")
    email = input("What is your email address? \n")
    password = input("Create your password \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_Name, last_Name, email, password]

    print("Your Account has been Created")
    print(" == ==== ====== ===== ===")
    print("Your account bumer is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print("== ==== ====== ===== ===")

    login()

#bank operations

def bankOperation(user):
    print("Welcome %s %s" % (user[0], user[1]))

    selectedOption = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n"))

    if(selectedOption == 1):
        depositOperation()
    elif(selectedOption == 2):
        withdrawalOperation()
    elif(selectedOption == 3):
        logout()
    elif(selectedOption == 4):
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)

def withdrawalOperation():
    print("withdrawal")

def depositOperation():
    print("Deposit")

#- generate user idaccount
def generationAccountNumber():
    return random.randrange(1111111111, 9999999999)

def logout():
    login()


### ACTUAL BANK SYSTEM ###
init()
