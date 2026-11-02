from calculator import add, check_employee


def test_add():
    assert add(2,3)==5

def test_junior_employee():
    assert check_employee({"experience": 1}) == "Junior level"

def test_experienced_employee():
    assert check_employee({"experience": 2}) == "Eligible for experienced role"

def test_missing_experience():
    assert check_employee({}) == "Experience missing"

def test_negative_experience():
    assert check_employee({"experience": -1}) == "Invalid experience"




# name=input("enter the name:")
# if name =="":
#    print("you didnt enter anything")
# else:
#    print("welcome",name)

# num= int(input("enter the number:"))
# if num % 2 == 0:
#     print(num,"is even")
# else:
#     print(num,"is odd")

# import random
# while True:
#  secret = random.randint(1, 10)
#  score=10
#  attempts=0
#  while True:
#             guess=int(input("Guess the number (1-10): "))
#             attempts+=1
#             if guess==secret:
#                 print("Correct! 🎉 Your score is:",score)
#                 break
#             elif guess>secret:
#                 print("Too high!")
#                 score-=1
#             else:
#                 print("Too low!")
#                 score-=1
#             print("Current score:",score)

#             if score==0:
#                 print("Game over! The secret number was:", secret)
#                 break

#  play_again = input("Do you want to play again? (yes/no): ")
#  if play_again.lower() != "yes":
#         print("Thanks for playing! Goodbye!")
#         break
            
# username="admin"
# password="pass123"

# attempts=0
# while attempts<3:
#     entered_user=input("Enter username:")
#     entered_pass=input("Enter password:")

#     if entered_user==username and entered_pass==password:
#         print("Login successful! Welcome,", entered_user)
#         break
#     else:
#         print("Login failed! Invalid username or password.")
#         attempts+=1

# if attempts==3:
#     print("Too many failed attempts. Please try again later.")
# else:
#     print("Login failed! Invalid username or password.")

# attempts=3
# while attempts>0:
#     entered_user=input("Enter username:")
#     entered_pass=input("Enter password:")

#     if entered_user==username and entered_pass==password:
#         print("Login successful! Welcome,", entered_user)
#         break
#     else:
#         attempts-=1
#         print("Login failed! Invalid username or password.")
#         print("Attempts remaining:", attempts)

# if attempts==0:
#     print("Account locked due to too many failed attempts. Please try again later.")

# users = {
#     "admin": "1234",
#     "john": "pass",
#     "alice": "qwerty"
# }

# attempts = 3

# while attempts > 0:
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     if username in users and users[username] == password:
#         print("Login successful ✅")
#         break
#     else:
#         attempts -= 1
#         print("Invalid credentials ❌")
#         print("Attempts left:", attempts)

# if attempts == 0:
#     print("Account locked 🔒")

# users={}

# while True:
#     choice= input("Do you want to (1) Register or (2) Login? (Enter 1 or 2): ")
#     if choice=="1":
#         username=input("Enter a username: ")
#         if username in users:
#             print("Username already exists. Please choose a different one.")
#             continue
#         password=input("Enter a password: ")
#         users[username]=password
#         print("Registration successful! You can now log in.")
#     elif choice=="2":
#         username=input("Enter your username: ")
#         password=input("Enter your password: ")
#         if username in users and users[username]==password:
#             print("Login successful! Welcome,", username)
#             break
#         else:
#             print("Invalid credentials. Please try again.")
#     else:
#         print("Invalid choice. Please enter 1 or 2.")

# print(users)
# import json

# # Load users if file exists
# try:
#     with open("users.json", "r") as file:
#         users = json.load(file)
# except:
#     users = {}
    
# print(users)

# while True:
#     choice = input("1.Register  2.Login : ")

#     if choice == "1":
#         username = input("Create username: ")
#         password = input("Create password: ")

#         if username in users:
#             print("User already exists ❌")
#         else:
#             users[username] = password

#             with open("users.json", "w") as file:
#                 json.dump(users, file)

#             print("Registered successfully ✅")

#     elif choice == "2":
#         username = input("Enter username: ")
#         password = input("Enter password: ")

#         if username in users and users[username] == password:
#             print("Login successful ✅")
#         else:
#             print("Invalid credentials ❌")

#     else:
#         print("Invalid option")

#     cont = input("Continue? (yes/no): ")
#     if cont.lower() != "yes":
#         break

# import json

# try:
#     with open("users.json", "r") as file:
#         users = json.load(file)
# except:
#     users = {}

# while True:
#     choice = input("1.Register  2.Login : ")

#     if choice == "1":
#         username = input("Create username: ")
#         password = input("Create password: ")

#         if username in users:
#             print("User already exists ❌")

#         elif len(password) < 4:
#             print("Password must be at least 4 characters ❌")

#         else:
#             users[username] = password

#             with open("users.json", "w") as file:
#                 json.dump(users, file)

#             print("Registered successfully ✅")

#     elif choice == "2":
#         username = input("Enter username: ")
#         password = input("Enter password: ")

#         if username not in users:
#             print("User not found ❌")

#         elif users[username] != password:
#             print("Wrong password ❌")

#         elif username=="" or password=="":
#             print("Please enter both username and password ❌")

#         else:
#             print("Login successful ✅")

#     else:
#         print("Invalid option")

#     cont = input("Continue? (yes/no): ")
#     if cont.lower() != "yes":
#         break


# import json

# def load_users():
#     try:
#         with open("users.json", "r") as file:
#             return json.load(file)
#     except:
#         return {}

# def save_users(users):
#     with open("users.json", "w") as file:
#         json.dump(users, file)

# def register(users):
#     username = input("Create username: ")
#     password = input("Create password: ")

#     if username in users:
#         print("User already exists ❌")

#     elif len(password) < 4:
#         print("Password too short ❌")

#     else:
#         users[username] = password
#         save_users(users)
#         print("Registered successfully ✅")

# def login(users):
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     if username not in users:
#         print("User not found ❌")

#     elif users[username] != password:
#         print("Wrong password ❌")

#     else:
#         print("Login successful ✅")

# users = load_users()

# while True:
#     choice = input("1.Register  2.Login : ")

#     if choice == "1":
#         register(users)

#     elif choice == "2":
#         login(users)

#     else:
#         print("Invalid option")

#     cont = input("Continue? (yes/no): ")
#     if cont.lower() != "yes":
#         break

# print(users)
# import json

# def load_users():
#     try:
#         with open("users.json", "r") as file:
#             return json.load(file)
#     except:
#         return {}

# def save_users(users):
#     with open("users.json", "w") as file:
#         json.dump(users, file)

# def register(users):
#     username = input("Create username: ")
#     password = input("Create password: ")
#     age = input("Enter age: ")

#     if username in users:
#         print("User already exists ❌")

#     elif len(password) < 4:
#         print("Password too short ❌")

#     else:
#         users[username] = {
#             "password": password,
#             "age": age
#         }
#         save_users(users)
#         print("Registered successfully ✅")

# def login(users):
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     if username not in users:
#         print("User not found ❌")

#     elif users[username]["password"] != password:
#         print("Wrong password ❌")

#     else:
#         print("Login successful ✅")
#         print("User age:", users[username]["age"])


# def update_user(users):
#     username = input("Enter username to update: ")

#     if username not in users:
#         print("User not found ❌")
#         return

#     new_age = input("Enter new age: ")
#     users[username]["age"] = new_age
#     print("User updated ✅")

# def delete_user(users):
#     username = input("Enter username to delete: ")

#     if username in users:
#         del users[username]
#         print("User deleted ✅")
#     else:
#         print("User not found ❌")

# def view_users(users):
#     if not users:
#         print("No users found ❌")
#         return

#     print("\n--- All Users ---")
#     for username, data in users.items():
#         print(f"Username: {username}, Age: {data['age']}")

# users = load_users()
# print(users)

# while True:
#     choice = input("1.Register 2.Login 3.Update 4.Delete 5.List all users : ")

#     if choice == "1":
#         register(users)
#     elif choice == "2":
#             login(users)
            
#     if choice == "3":
#         update_user(users)
#         save_users(users)

#     elif choice == "4":
#         delete_user(users)
#         save_users(users)


#     elif choice == "5":
#          view_users(users)

        

#     else:
#         print("Invalid option")

#     cont = input("Continue? (yes/no): ")
#     if cont.lower() != "yes":
#         break

# numbers = [10, 25, 30, 45, 50, 60]
# total=sum(numbers)
# average=total/len(numbers)
# print("Total:",total)
# print("Average:",average)

# highest=[]

# for num in numbers:
#     if num>30:
#         highest.append(num)
# print("Numbers greater than 30:",highest)

# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     print("Excellent ⭐")
# elif marks >= 75:
#     print("Good 👍")
# elif marks >= 50:
#     print("Average 🙂")
# else:
#     print("Needs Improvement ⚠️")

# numbers=[1,2,1,2,1,1,1,1,2,3,2,3,2,5,6,5,4,4,5,5,6]

# count={}
# for num in numbers:
#     count[num] = count.get(num, 0) + 1

# print("Number of occurrences of each element:", count)
# for num in numbers:
#     if num in count:
#         count[num]+=1
#     else:
#         count[num]=1
# print("Number of occurrences of each element:", count)
# most_common=max(count,key=count.get)
# print("Most common element:", most_common)


import pandas as pd
print(pd.__version__)

# data = {
#     "name": ["A", "B", "C"],
#     "age": [20, 30, 25]
# }

# df = pd.DataFrame(data)

# print(df)
# print(df["age"].mean())
