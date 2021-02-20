# Write your code here
import random
opt = random.choice(['rock', 'paper', 'scissors'])
user = input()

if opt == 'rock':
    if user == 'rock':
        print('There is a draw (rock)')
    elif user == 'scissors':
        print('Sorry, but the computer chose rock')
    else:
        print('Well done. The computer chose rock and failed')
elif opt == 'scissors':
    if user == 'scissors':
        print('There is a draw (scissors)')
    elif user == 'paper':
        print('Sorry, but the computer chose scissors')
    else:
        print('Well done. The computer chose scissors and failed')
elif opt == 'paper':
    if user == 'paper':
        print('There is a draw (paper)')
    elif user == 'rock':
        print('Sorry, but the computer chose paper')
    else:
        print('Well done. The computer chose paper and failed')
