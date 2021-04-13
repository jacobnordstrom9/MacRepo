

# phonebook_dic = open("phonebook.txt","r")
# contents = phonebook_dic.read()
2
phonebook_dic = {
    "Alice": "703-493-1834",
    "Bob" : "857-384-1234",
    "Elizabeth": "484-584-2923"
}


# def userQuestion(userInput):

#     userInput = int(input("""Electronic Phone Book
# =====================

# 1. Look up an entry
# 2. Add a new entry
# 3. Delete an entry
# 4. Listing all the entries
# 5. Quit phonebook    
# """))
#     return choice

# choice = int(userInput)

# # menu

# Functions Start Here

def UserQuestion():
    userInput = int(input(f""" What would you like to do?
1. Look up an entry
2. Add a new entry
3. Delete an entry
4. Listing all the entries
5. Quit phonebook    
"""))
    return userInput   
    # Without "return userInput" we would give the userInput a numer of 1 but that 1 would not "exit" the userInput ever again. We were baking a cake but never taking it out of the oven. With return = userInput, we are able to give the userInput a new variable/integer to run the code again

def setEntry():
    lookup_name = input("Who do you want to look up? >> ")
    result = phonebook_dic[lookup_name]
    print(result)

def addEntry():
    new_user = input("so you want to add a new name to the phone book? who do you want to add? >> ")
    new_number = input("what is their phone number? >> ")
    phonebook_dic [f"{new_user}"] = f"{new_number}" 
    print(phonebook_dic)

def deleteEntry():
    delete_entry = input("Who do you want to delete from the phone book? >> ")
    del phonebook_dic[f"{delete_entry}"]
    print(phonebook_dic)
    print(f"You have no deleted {delete_entry} from the phonebook")

def listAllEntry():
    print("You can find all the entries currently in the phone book below")
    print(phonebook_dic)

# Main Code

userInput = input(f""" What would you like to do? ******
1. Look up an entry
2. Add a new entry
3. Delete an entry
4. Listing all the entries
5. Quit phonebook    
""")

choice = int(userInput)

while True:
    if choice == 1 :
        setEntry()
        choice = UserQuestion()
    elif choice == 2:
        addEntry()
        choice = UserQuestion()
    elif choice ==3:
        deleteEntry()
        choice = UserQuestion()
    elif choice == 4:
        listAllEntry()
        choice = UserQuestion()
    elif choice == 5 :
        print("You have now exited the phonebook")
        break







# # 1. Look up an entry
# def lookUp(lookup_name):
# while 
#     lookup_name = input("who do you want to look up? >> ")
#     result = phonebook_dic[lookup_name]
#     print(result)

#2. Setting an entry

def setEntry():
    pass


# phonebook_dict ["Kareem"] = "938-489-1234"

# print(phonebook_dict)  #{'Alice': '703-493-1834', 'Bob': '857-384-1234', 'Elizabeth': '484-584-2923', 'Kareem': '938-489-1234'}


#3 Deleting Entry
def deleteEntry():
    pass

#4 List all Entries
def listEntry():
    pass

# For Loops, While Loops, If statements
# While Loops prompting users for input
#Within the while loop, we need to check for when the users want to quit
# if users want to quit, we need to exit the whole loop
#if, elif blocks
#call function within these blocks


#breaks
#false




