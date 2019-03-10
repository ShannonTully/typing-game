import time
import random
from getch import getch as gc
from random_word import RandomWords as rand
from pygame import mixer 
from words import words
from words import starting_message, game_mode_message, speed_message, name_message, round_message
from words import line


class KeyPlay:

    def __init__(self):

        self.timer = 0
        self.song = mixer

        self.load_song()

    def load_song(self):
        self.song.init()
        self.song.music.load('03_Klad_Get.mp3')
        self.play_music()

    def play_music(self):
        while type(gc()) is str:
            # import pdb; pdb.set_trace()
            if self.timer == 0:
                self.song.music.play(start=self.timer)
            else:
                self.song.music.unpause()
            time.sleep(.12)
            self.song.music.pause()
            self.timer += 1
        self.play_music()


class Typing_game:

    def __init__(self):
        self.words = words.split()
        self.word = ''
        self.user_input = ''
        self.points = 0
        self.rounds = 0
        self.rounds_left = -1
        self.speed = ''
        self.name = ''
        self.divisor = 2
        self.total_rounds = ''
        self.accuracy = 0
        self.yeet = False
        self.leaderboards = []
        self.split_leaderboards = []
        self.joined_leaderboards = []
        self.words_per_minute = 0

        self.starting_input()

    def get_word(self):
        self.word = random.choice(self.words)
        # self.word = rand.get_random_word(self, hasDictionaryDef="true")

    def get_input(self):
        if self.yeet:
            self.word = 'yeet'

        self.user_input = input(f'\nType this:\n\n{self.word}\n')

    def get_name(self):
        self.name = input(name_message)

        if not self.name:
            self.get_name()
        elif len(self.name) > 8:
            print('\nName too long\n')
            self.get_name()
        elif ' ' in self.name:
            print('\nSorry, no spaces please.')
            self.get_name()

    def get_game_mode(self):
        self.game_type = input(game_mode_message)

    def get_rounds(self):
        self.total_rounds = input(round_message)

        if self.total_rounds == '10':
            self.rounds_left = 10
        elif self.total_rounds == '25':
            self.rounds_left = 25
        elif self.total_rounds == '50':
            self.rounds_left = 50
        elif not self.total_rounds:
            self.rounds_left = -1
        else:
            print('\nPick a valid number\n')
            self.get_rounds()

    def get_speed(self):
        self.speed = input(speed_message)

        if self.speed == 'yeet':
            self.yeet = True
            self.divisor = 4
        elif self.speed == '2':
            self.divisor = 3
        elif self.speed == '3':
            self.divisor = 4
        else:
            print('\nSpeed: 1\n')
            self.speed = '1'
            self.divisor = 2

    def response_cycle(self):
        print('\nReady\n')
        time.sleep(1)
        print('\nSet\n')
        time.sleep(1)
        print('\nGo!\n')
        wpm_start = time.time()
        while self.rounds_left != 0:
            if self.rounds_left < 0:
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
                    wpm_end = time.time()
                    wpm_timer = wpm_end - wpm_start
                    self.words_per_minute = round(60 / wpm_timer * self.points)
                    print(f'\n\nAt speed {self.speed} you got {self.points} points in {self.rounds} rounds!\nThat\'s {self.words_per_minute} words per minute!\n')
                    if self.points == self.rounds:
                        print(f'Try a harder level!\n')
                    break

            else:
                self.get_word()
                start = time.time()
                print(f'Words left: {self.rounds_left}')
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
                self.rounds_left -= 1

        if self.rounds_left == 0:
            wpm_end = time.time()
            wpm_timer = wpm_end - wpm_start
            self.words_per_minute = round(60 / wpm_timer * self.points)
            print(f'\n\nAt speed {self.speed} you got {self.points} points in {self.rounds} rounds!\nThat\'s {self.words_per_minute} words per minute!\n')
            if self.points == self.rounds:
                    print(f'Try a harder level!\n')
            self.save_to_leaderboards()

    def save_to_leaderboards(self):
        save_input = input('\nWould you like to save your results (Y or n)\n')
        if save_input.lower() == 'y':
            print('\n')
            with open('leaderboards.txt', "r") as f:
                data = f.readlines()
                for l in data:
                    self.leaderboards.append(l)
            with open('leaderboards.txt', "w") as f:
                self.leaderboards.append(f'{self.name}: Speed {self.speed} | Accuracy {round((self.points / self.rounds) * 100)}% | Rounds {self.rounds} | WPM {self.words_per_minute}')

                for l in self.leaderboards:
                    self.split_leaderboards.append(l.split())

                self.split_leaderboards.sort(key=lambda x: int(x[5][:-1]), reverse=True)

                for l in self.split_leaderboards:
                    self.joined_leaderboards.append(' '.join(l))
                print(line)
                print('\n:Leaderboard:\n')
                print(line)

                for l in self.joined_leaderboards:
                    print(l)
                    f.write(l + '\n')

        elif save_input.lower() == 'n':
            print('\nGoodbye\n')
        else:
            print('Sorry Y or n only')
            self.save_to_leaderboards()

    def starting_input(self):
        print(starting_message)
        print(line)
        self.get_name()
        print(line)
        self.get_game_type()
        print(line)
        self.get_rounds()
        print(line)
        self.get_speed()
        print(line)

        self.response_cycle()


if __name__ == '__main__':
    Typing_game()
