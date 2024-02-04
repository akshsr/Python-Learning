import random # importing library

top_of_range = input('Type a upper limit: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range) # we changed the input str to int

    if top_of_range <= 0:
        print('Please type number larger than 0 next time')
        quit()
else:
    print('Please type the number next time')
    
random_number = random.randint(0, top_of_range)

guesses = 0

while True:   # we started a loop here where condition is true
    guesses += 1
    user_guess  = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Type number next time')
        continue # this will bring us back to while loop condition

    if user_guess == random_number:
        print('You guessed this right')
        break
    elif user_guess > random_number:
        print('You were above the number!') # elif used after if statement and when there are more than one if possible
    else:
        print('You were below the number!')

print('You got in', guesses, "guesses")