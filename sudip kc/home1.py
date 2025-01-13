#Check if a number is positive, negative, or zero
#Check if a number is even or odd:
#num=int(input("enter a number"))
#if num/2==0:
#    print("the number is even")
#else:
#    print("the num id odd")    
    

#num = 9

#if num % 2 == 0:
#    print(f"{num} is even!")
#else:
#    print(f"{num} is odd!")

#check if the number is posiyive ,negative or zero
#n=int(input("enter a num"))
#if n>0:
#    print("the num is positive")
#elif n<0:
#    print("the num is negative")
#else:
#    print("the num is zero")

#Write a program that takes a student's score (0–100) as input and prints the corresponding grade:

#Score Range	Grade
#90–100	A
#80–89	B
#70–79	C
#60–69	D
#Below 60	F
 
#score=int(input("enter a score"))
#if 90<=score<=100:
#     print("The grade is A")
#elif 80<=score<=89:
#    print("the gread is B")
#elif 70<=score<=79:
#    print("the gread is C")    
#elif 60<=score<=69:
#    print("the gread is D")
#else:
#    print("the gread is F")        

#check the program is leap yrs 

#year = int(input("Enter a year: "))
#if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#    print("It's a leap year.")
#else:
#    print("It's not a leap year.")
 # while True:
  #  number = int(input("Enter a number (or -1 to exit): "))
   # if number == -1:
    #    print("Exiting...")
    #    break
    #if number % 2 == 0:
    #    print("The number is even.")
    #else:
    #    print("The number is odd."
    
    #Basic User Management:
#Extend the program you wrote to:

#Allow users to update their password.
#Implement a feature to delete their account.
    
import json

def load_users(filename="users.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users, filename="users.json"):
    with open(filename, "w") as file:
        json.dump(users, file, indent=4)

def update_password(username, new_password):
    users = load_users()
    if username in users:
        users[username]['password'] = new_password
        save_users(users)
        print("Password updated successfully.")
    else:
        print("User not found.")

def delete_account(username):
    users = load_users()
    if username in users:
        del users[username]
        save_users(users)
        print("Account deleted successfully.")
    else:
        print("User not found.")

