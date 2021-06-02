import random
import re


class Hangman:
    def __init__(self, words, retry=6):
        self.words = words
        self.retry = retry

    def start(self):
        selected: str = random.choice(self.words)
        filtered = selected
        output = list(map(self.__toUnderscore, list(range(len(selected)))))

        print('_ ' * len(selected))

        while len(filtered) > 0:
            valid = False

            while not valid:
                letter = input('Guess a letter: ')
                valid = self.__validate(letter)

            indexes = [m.start() for m in re.finditer(letter, selected)]

            if len(indexes) > 0:
                for index in indexes:
                    output[index] = letter

            print(' '.join(map(self.__toUpper, output)))
            temp = filtered.replace(letter, '')

            if len(temp) == len(filtered):
                self.retry -= 1

                if self.retry == 0:
                    print('YOU LOSE')
                    break

                else:
                    print(f"{self.retry} retries left.")

            filtered = temp

        else:
            print('YOU WIN')

    def __validate(self, letter: str):
        return False if (len(letter) != 1) or letter.isdecimal() else True

    def __toUnderscore(self, o):
        return '_'

    def __toUpper(self, o: str):
        return o.upper()


again = 'y'

while again == 'y':
    words = ['accuracy', 'currency', 'explicit']
    Hangman(words).start()

    again = input('Continue playing? (y/n): ')

else:
    print('Thanks for playing')
