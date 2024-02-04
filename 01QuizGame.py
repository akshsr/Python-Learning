print('Welcome to my computer quiz!') # print the words 

playing = input("Do you want to play? ") # to take input from user 

# used lower funtion to convert str to lowercase
if playing.lower() != 'yes': # if statement is condition statement where != 'not equal to'
    quit()
print ('okay lets play ;)')

score = 0 # will increment further in if statement 

answer = input('What does CPU stand for? ')
if answer.lower()== "central processing unit":
    print('correct!')
    score += 1
else:      # else statement is where 'if not then'
    print('incorrect!')

answer = input('What does GPU stand for? ') # we can same variable bc we're done with previous "answer" variable
if answer.lower()== "graphics processing unit":
    print('correct!')
    score += 1
else:      # else statement is where 'if not then'
    print('incorrect!')

answer = input('What does HDD stand for? ')
if answer.lower()== "hard disk drive":
    print('correct!')
    score += 1
else:      # else statement is where 'if not then'
    print('incorrect!')

answer = input('What does HTML stand for? ')
if answer.lower()=="hypertext markup language":
    print('correct!')
    score += 1
else:      # else statement is where 'if not then'
    print('incorrect!')

print('you got ' + str(score) + ' questions correct!') # we concatinated here in b/w two str and changed int to str as in output
print('you got ' + str((score/4)*100) + '%.') #performed addition operation here before changing into str
