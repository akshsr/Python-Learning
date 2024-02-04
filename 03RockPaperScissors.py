import random

user_scores = 0
computer_scores = 0

options = ['rock', 'paper', 'scissors'] # with [ ] we created a list 

while True:
    user_input = input("Type Rock/Paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print('You may typed wrong! ')
        continue

    random_number = random.randint(0, 2)
    # rock = 0, paper = 1, scissors = 2
    computer_pick = options[random_number]
    print('Computer picked', computer_pick)

    if user_input == 'rock' and computer_pick == 'scissors':
        print('You won')
        user_scores += 1    
    elif user_input == 'paper' and computer_pick == 'rock':
        print("you won")
        user_scores += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print('you won')
        user_scores += 1
    elif user_input =="rock" and computer_pick == 'rock':
        print('Draw')
    elif user_input =="paper" and computer_pick == 'paper':
        print('Draw')
    elif user_input =="scissors" and computer_pick == 'scissors':
        print('Draw')
    else:
        print("you lost")
        computer_scores += 1

print("you scored", user_scores)
print("The computer scored", computer_scores)
print('Goodbye!')