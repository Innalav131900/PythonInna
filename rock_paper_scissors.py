import random

user_select = input("Enter 'rock' or 'paper' or 'scissors':")
print(user_select)

list_of_selection = ["rock", "paper", "scissors"]
if user_select not in list_of_selection:
    print("incorrect value")
    exit()

random_select = random.choice(list_of_selection)
print(random_select)


if user_select == random_select:
    print("game draw, sorry")
if user_select == "rock" and random_select == "paper":
    print("you lost, sorry")
if user_select == "scissors" and random_select == "paper":
    print("you win, congratulations!")
if user_select == "paper" and random_select == "rock":
    print("you win, congratulations!")
if user_select == "scissors" and random_select == "rock":
    print("you lost, sorry")
if user_select == "paper" and random_select == "scissors":
    print("you lost, sorry")
if user_select == "rock" and random_select == "scissors":
    print("you win, congratulations!")