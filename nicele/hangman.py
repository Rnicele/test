import enum
import random
import re

words = ['accident', 'designer', 'exchange', 'original', 'spectrum', 'unlawful']
lives = 6

message = '''
    Guess the word!

    _ _ _ _ _ _ _ _

'''
guessword = ['_', '_', '_', '_', '_', '_', '_', '_']
numberGuess = 8
countGuess = 0

rword = random.choice(words)
listrword = list(rword)

while numberGuess != countGuess and lives != 0:
    letter = input('Letter: ')
    
    print('-------------------------------------------------------------------------------------')
    if len(letter) == 1:
        while letter in listrword:
            find = ''.join(guessword).find(letter)
            print("find: ", find)
            if find >= 0:
                print('letter is in the word already. input another letter')
                break
            else:
                indexes = [m.start() for m in re.finditer(letter, rword)]
                print('Correct!')
                print('Lives left: ', lives)
                
                if len(indexes) > 0:
                    for index in indexes:
                        guessword[index] = letter
                    
                    countGuess += len(indexes)
                else:
                    index = indexes[0]
                    guessword[index] = letter
                    countGuess += 1
                
                print("GUESS THE WORD: ", ''.join(guessword))
                print('-------------------------------------------------------------------------------------')
                break
            
        else:
            lives = lives - 1
            fullMsg = f'Letter is not in the word! you have {lives} lives left.'
            print(fullMsg)
            print('-------------------------------------------------------------------------------------')
    else:
        print('Only 1 letter is allowed')
        lives = lives - 1

else:
    if numberGuess != countGuess and lives == 0:
        print("You don't have lives left. GAME OVER")
    elif numberGuess == countGuess:
        print("CONGRATULATIONS! YOU GUESS THE WORD!")


