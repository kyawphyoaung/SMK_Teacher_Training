import sys

print("1. Register")
print("2. Login")
print("3. Forgot Password")
print("4. Exit.")

user_choice = int(input("Please enter a menu option"))

while user_choice != 4:
    if user_choice == 1:
        print("Register")
    elif user_choice == 2:
        print("Login")
    elif user_choice == 3:
        print("Forgot Password")

    print("==================")
    print("1. Register")
    print("2. Login")
    print("3. Forgot Password")
    print("4. Exit.")

    user_choice = int(input("Please enter a menu option"))

def newUser():
    print("New User Registration")
    

sys.exit(0)