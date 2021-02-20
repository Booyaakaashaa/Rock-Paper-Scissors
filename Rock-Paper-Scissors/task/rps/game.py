# Write your code here
import random
while 1:
    user = input()
    if user == "!exit":
        print("Bye!")
        break
    opt = random.choice(['rock', 'paper', 'scissors'])
    if opt == 'rock':
        if user == 'rock':
            print('There is a draw (rock)')
        elif user == 'scissors':
            print('Sorry, but the computer chose rock')
        elif user == "paper":
            print('Well done. The computer chose rock and failed')
        else:
            print('Invalid input')
    elif opt == 'scissors':
        if user == 'scissors':
            print('There is a draw (scissors)')
        elif user == 'paper':
            print('Sorry, but the computer chose scissors')
        elif user == "rock":
            print('Well done. The computer chose scissors and failed')
        else:
            print('Invalid input')
    elif opt == 'paper':
        if user == 'paper':
            print('There is a draw (paper)')
        elif user == 'rock':
            print('Sorry, but the computer chose paper')
        elif user == 'scissors':
            print('Well done. The computer chose paper and failed')
        else:
            print('Invalid input')
