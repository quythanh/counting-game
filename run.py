from time import sleep
from os import system
from game import *

class Handle():
    def __init__(self):
        pass


    def play(self):
        try:
            Range = int(input('Which number do you want to count to?\t')) # 30
            assert(Range >= 20), 'The range should be at least 20'

            limit = int(input(f'How many numbers can you add each time? (2 to {round(Range/5)})\t'))
            assert(limit >= 2 and limit <= round(Range/5)), 'You Suck'

            roles = int(input('Who will go first? (1: You, 2: Computer)\t'))

            game = Game(Range, limit, roles)
            game.start()
            game.play_again()

            print('=' * 50)

        except AssertionError as error:
            print('--->> Error: '+ error)
            print('=' * 50)

        except ValueError:
            print('--->> Error: You should type number')
            print('=' * 50)


    def help(self):
        lst_help = ["How to play\n\n", "Which number do you want to count to?\t", 3, 0,
        "\nHow many numbers can you add each time?\t", 3, "\nWho will go first? (1: You, 2: Computer)\t", 1,
        "\n\nThe goal of the game is to be the first person to say “30”. The rules are that you can only add 1, 2 or 3 to whatever the other player says.\n\n",
        "For example:\n\nYou:     \t", "1", ",", " ", "2", ",", " ", "3", "\nComputer:\t4, 5, 6\nYou:     \t", "7", ",", " ", "8",
        "\nComputer:\t9\nYou:     \t", "1", "0", ",", " ", "1", "1", ",", " ", "1", "2",
        "\nComputer:\t13, 14\nYou:     \t", "1", "5", ",", " ", "1", "6",
        "\nComputer:\t17, 18\nYou:     \t", "1", "9", ",", " ", "2", "0", ",", " ", "2", "1",
        "\nComputer:\t22\nYou:     \t", "2", "3", ",", " ", "2", "4",
        "\nComputer:\t25, 26\nYou:     \t", "2", "7", "\nComputer:\t28, 29, 30\nYou lose :(\n\n"]
        for i in lst_help:
            print(i, end='')
            sleep(0.5)
        a = input("Press Enter to back")
        self.main()


    def main(self):
        system('cls')
        print("Counting Strategy Game")
        option = input("1. How to play\n2. Start\n3. Exit\nChoose the option:\t")
        if option == "1":
            system('cls')
            self.help()
        elif option == "2":
            system('cls')
            self.play()
        else:
            return


if __name__ == '__main__':
    Handle().main()
