import random
name = input("Enter your name: ")
print(f"Hello, {name}")
ratings = open('rating.txt', 'r')
score = 0
rps = input().strip().split(",")
if rps[0] == "":
    rps = ['rock', 'paper', 'scissors']
print(rps)
for line in ratings:
    line = line.strip().split()
    if line[0] == name:
        score = int(line[1])
game = ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun']
print("Okay, let's start")
while 1:
    user = input()
    if user == '!rating':
        print(f"Your rating: {score}")
        continue
    if user == "!exit":
        print("Bye!")
        break
    opt = random.choice(rps)
    if user == game[0]:
        if opt == game[0]:
            print(f'There is a draw ({user})')
            score += 50
        elif opt in game[8:]:
            print(f'Sorry, but the computer chose {opt}')
        elif opt in game[1:8]:
            print(f'Well done. The computer chose {opt} and failed')
            score += 100
    elif user == game[1]:
        if opt == game[1]:
            print(f'There is a draw ({user})')
            score += 50
        elif opt in game[9:] or opt in game[0]:
            print(f'Sorry, but the computer chose {opt}')
        elif opt in game[2:9]:
            print(f'Well done. The computer chose {opt} and failed')
            score += 100
    elif user == game[2]:
        if opt == game[2]:
            print(f'There is a draw ({user})')
            score += 50
        elif opt in game[10:] or opt in game[0:2]:
            print(f'Sorry, but the computer chose {opt}')
        elif opt in game[3:10]:
            print(f'Well done. The computer chose {opt} and failed')
            score += 100
    elif user == game[3]:
        if opt == game[3]:
            print(f'There is a draw ({user})')
            score += 50
        elif opt in game[11:] or opt in game[0:3]:
            print(f'Sorry, but the computer chose {opt}')
        elif opt in game[4:11]:
            print(f'Well done. The computer chose {opt} and failed')
            score += 100
    elif user == game[4]:
        if opt == game[4]:
            print(f'There is a draw ({user})')
            score += 50
        elif opt in game[12:] or opt in game[0:4]:
            print(f'Sorry, but the computer chose {opt}')
        elif opt in game[5:12]:
            print(f'Well done. The computer chose {opt} and failed')
            score += 100
    elif user == game[5]:
        if opt == game[5]:
            print(f'There is a draw ({user})')
            score += 50
        elif opt in game[13:] or opt in game[0:5]:
            print(f'Sorry, but the computer chose {opt}')
        elif opt in game[6:13]:
            print(f'Well done. The computer chose {opt} and failed')
            score += 100
    elif user == game[6]:
        if opt == game[6]:
            print(f'There is a draw ({user})')
            score += 50
        elif opt in game[14] or opt in game[0:6]:
            print(f'Sorry, but the computer chose {opt}')
        elif opt in game[7:]:
            print(f'Well done. The computer chose {opt} and failed')
            score += 100
    elif user == game[7]:
        if opt == game[7]:
            print(f'There is a draw ({user})')
            score += 50
        elif opt in game[0:7]:
            print(f'Sorry, but the computer chose {opt}')
        elif opt in game[8:]:
            print(f'Well done. The computer chose {opt} and failed')
            score += 100
    elif user == game[8]:
        if opt == game[8]:
            print(f'There is a draw ({user})')
            score += 50
        elif opt in game[1:8]:
            print(f'Sorry, but the computer chose {opt}')
        elif opt in game[9:] or opt in game[0]:
            print(f'Well done. The computer chose {opt} and failed')
            score += 100
    elif user == game[9]:
        if opt == game[9]:
            print(f'There is a draw ({user})')
            score += 50
        elif opt in game[2:9]:
            print(f'Sorry, but the computer chose {opt}')
        elif opt in game[10:] or opt in game[0:2]:
            print(f'Well done. The computer chose {opt} and failed')
            score += 100
    elif user == game[10]:
        if opt == game[10]:
            print(f'There is a draw ({user})')
            score += 50
        elif opt in game[3:10]:
            print(f'Sorry, but the computer chose {opt}')
        elif opt in game[11:] or opt in game[0:3]:
            print(f'Well done. The computer chose {opt} and failed')
            score += 100
    elif user == game[11]:
        if opt == game[11]:
            print(f'There is a draw ({user})')
            score += 50
        elif opt in game[4:11]:
            print(f'Sorry, but the computer chose {opt}')
        elif opt in game[12:] or opt in game[0:4]:
            print(f'Well done. The computer chose {opt} and failed')
            score += 100
    elif user == game[12]:
        if opt == game[12]:
            print(f'There is a draw ({user})')
            score += 50
        elif opt in game[5:12]:
            print(f'Sorry, but the computer chose {opt}')
        elif opt in game[13:] or opt in game[0:5]:
            print(f'Well done. The computer chose {opt} and failed')
            score += 100
    elif user == game[13]:
        if opt == game[13]:
            print(f'There is a draw ({user})')
            score += 50
        elif opt in game[6:13]:
            print(f'Sorry, but the computer chose {opt}')
        elif opt in game[14] or opt in game[0:6]:
            print(f'Well done. The computer chose {opt} and failed')
            score += 100
    elif user == game[14]:
        if opt == game[14]:
            print(f'There is a draw ({user})')
            score += 50
        elif opt in game[7:]:
            print(f'Sorry, but the computer chose {opt}')
        elif opt in game[0:7]:
            print(f'Well done. The computer chose {opt} and failed')
            score += 100
    else:
        print('Invalid input')
ratings.close()
