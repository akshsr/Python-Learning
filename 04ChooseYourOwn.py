name = input("Type your name: ")
print("Welcome", name, "to the adventure")

answer = input(
    "You are on a dirty road, it has come to an end and you can go left or right. Which way would you like to go?: ").lower()

if answer == 'left':
    answer = input(
        "You come to a river, you can walk around it or swim accross? Type walk to walk around or swim to swim accross: ")

    if answer == "swim":
        print('You swam accrossed and were eaten by alligator')
    elif answer == "walk":
        print("You walked for many miles, you ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input('You come to a bridge, it looks wobbly, do you want to cross it? yes or no?: ').lower()

    if answer == "yes":
        print("You find a safe house. You won the game")
    elif answer == "no":
        answer = input("You got scared, so you want go back or take some different road? back/another road?: ").lower()
        if answer == 'back':
            print("Some wolfs attacked you and you lost the game")
        elif answer == "another road":
            print("You walked and walked thus due to exhaustion you passed out and you lost the game")
else:
    print("Not a valid option. You lose.")