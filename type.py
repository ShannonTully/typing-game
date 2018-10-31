import time
import random
from words import words
from words import starting_message
from words import line


class Typing:

    def __init__(self):
        self.words = words.split()
        self.word = ''
        self.user_input = ''
        self.points = 0
        self.rounds = 0
        self.level = ''
        self.divisor = 2
        self.yeet = False

    def get_word(self):
        self.word = random.choice(self.words)

    def get_input(self):
        if self.yeet:
            self.word = 'yeet'

        self.user_input = input(f'\nType this:\n\n{self.word}\n')

    def response_cycle(self):
        while True:
            try:
                self.get_word()
                start = time.time()
                self.get_input()
                end = time.time()

                timer = end - start

                if self.user_input == self.word:
                    if timer <= len(self.word) / self.divisor:
                        self.points += 1
                        print(f'\nNice job!  You had {round(len(self.word) / self.divisor - timer, 2)} seconds left.\n\n{line}')
                    else:
                        print(f'\nNot fast enough.  You were over by {round(timer - len(self.word) / self.divisor, 2)} seconds.\n\n{line}')
                else:
                    self.points -= 1
                    print(f'\nIncorrect spelling. Slow down!\n\n{line}')
                self.rounds += 1

            except (KeyboardInterrupt, EOFError, SystemExit):
                print(f'\n\nAt level {self.level} you got {self.points} points in {self.rounds} rounds!\n')
                if self.points == self.rounds:
                    print('Try a harder level!\n')
                break

    def starting_message(self):
        self.level = input(starting_message)
        print(line)
        try:
            if self.level == 'yeet':
                self.yeet = True
                self.divisor = 4
            elif self.level == 2:
                self.divisor = 3
            elif self.level == 3:
                self.divisor = 4
            else:
                self.level = 1
                self.divisor = 2
        except:
            self.level = 1
            self.divisor = 2

        self.response_cycle()


if __name__ == '__main__':
    Typing().starting_message()
