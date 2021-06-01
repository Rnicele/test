import random

selectables = ['✊', '✋', '✌']

confirm = 'y'

while confirm == 'y':
    validated = False

    while not validated:
        selected = input('Select ✊, ✋ or ✌ : ')
        validated = False if not selected in selectables else True

    ramdomized = random.choice(selectables)
    print(f"{selected} x {ramdomized}")

    if selected == ramdomized:
        print('Draw')

    elif (selected == '✊' and ramdomized == '✋') or (selected == '✋' and ramdomized == '✌') or (selected == '✌' and ramdomized == '✊'):
        print('You lose')

    else:
        print('You win')

    confirm = input('Do you want to try again? (y/n): ')
else:
    print('Thanks for playing')
