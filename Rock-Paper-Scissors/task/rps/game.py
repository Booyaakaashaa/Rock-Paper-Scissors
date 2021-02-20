import random
name = input("Enter your name: ")
print(f"Hello, {name}")
ratings = open('rating.txt', 'r')
score = 0
for line in ratings:
    line = line.strip().split()
    if line[0] == name:
        score = int(line[1])
while 1:
    user = input()
    if user == '!rating':
        print(f"Your rating: {score}")
    if user == "!exit":
        print("Bye!")
        break
    opt = random.choice(['rock', 'paper', 'scissors'])
    if opt == 'rock':
        if user == 'rock':
            print('There is a draw (rock)')
            score += 50
        elif user == 'scissors':
            print('Sorry, but the computer chose rock')
        elif user == "paper":
            print('Well done. The computer chose rock and failed')
            score += 100
        else:
            print('Invalid input')
    elif opt == 'scissors':
        if user == 'scissors':
            print('There is a draw (scissors)')
            score += 50
        elif user == 'paper':
            print('Sorry, but the computer chose scissors')
        elif user == "rock":
            print('Well done. The computer chose scissors and failed')
            score += 100
        else:
            print('Invalid input')
    elif opt == 'paper':
        if user == 'paper':
            print('There is a draw (paper)')
            score += 50
        elif user == 'rock':
            print('Sorry, but the computer chose paper')
        elif user == 'scissors':
            print('Well done. The computer chose paper and failed')
            score += 100
        else:
            print('Invalid input')
