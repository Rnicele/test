import random

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
print(rword)
print(countGuess)

while numberGuess != countGuess and lives != 0:
    letter = input('Letter: ')
    print('-------------------------------------------------------------------------------------')
    if len(letter) == 1:
        while letter in listrword:
            find = ''.join(guessword).find(letter)
            if find == True:
                print('letter is in the word already. input another letter')
                break
            else:
                print('Letter is not in the word yet')
                print('Lives left: ', lives)
                letFind = rword.find(letter)
                guessword[letFind] = letter
                countGuess += 1
                print("GUESS THE WORD: ", ''.join(guessword))
                print("Counted Correct Letters: ", countGuess)
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
