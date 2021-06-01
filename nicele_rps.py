import random
message = '''
Choose letters r/p/s for your pick!
r = rock
p = paper
s = scissor
'''

print(message)
pick = input('choose your weapon: ')

if len(pick) == 1:
    letters = ['r', 'p', 's', 'r', 'p', 's', 'r', 'p', 's']
    coRandom = random.choice(letters)
    print('comp. pick: ', coRandom)
    while pick in letters:
        if coRandom == pick:
            print('TIE')
        elif coRandom == 'r' and pick == 'p':
            print('You win!')
        elif coRandom == 'r' and pick == 's':
            print('You lose!')
        elif coRandom == 'p' and pick == 'r':
            print('You lose')
        elif coRandom == 'p' and pick == 's':
            print('You win')
        elif coRandom == 's' and pick == 'p':
            print('You lose')
        else:
            print('You win')
        break 
    else:
        print('not in choices')