import sys
import time
import os
import random
from words import words


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def start():
    program = ScrollingText()
    final_word = []
    word_lst = words.split()

    for _ in range(20):
        final_word.append(random.choice(word_lst))
        program.data = ' '.join(final_word)
    # program.data = input("Enter string : ") + " "
    program.scroll()


class ScrollingText:
    def __init__(self):
        self.rows, self.width = os.popen('stty size', 'r').read().split()
        self.data = ""
        # self.width = self.rows

    def scroll(self):
        index = 0
        try:
            while True:
                for x in range(int(self.width), 0, -1):
                    clear_console()
                    import pdb; pdb.set_trace()

                    # While len of msg is not longer than self.width,
                        #append the cut off section of the msg to the scrolling text line.
                        # slice off the end of msg so it doesnt appear on two lines.

                    msg = "{}{}".format(" " * x, self.data)
                    print(msg[150:])
                    index += 1
                    if index > len(msg[index:-30]):
                        index = 0
                    time.sleep(0.1)
        except KeyboardInterrupt:
            pass
        # try:
        #     while True:

        #         for x in range(int(self.width), 0, -1):
        #             time.sleep(0.1)
        #             msg = "\r{}{}".format(" " * x, self.data)
        #             print(msg, end='\r')
        #             # sys.stdout.write(msg)
        #             # sys.stdout.flush()
        # except KeyboardInterrupt:
        #     print("Exiting")


if __name__ == "__main__":
    start()