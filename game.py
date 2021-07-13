from random import randint
from os import system
from process import *

class Game():
    def __init__(self, Range, limit, roles):
        self.Range = Range
        self.limit = limit
        self.numberList = [i for i in range(1, self.Range + 1)]
        self.roles = roles
        self.winNumber = self.Range % (self.limit + 1)


    def role_1(self):
        while self.numberList != []:
            numberInput = input('You:     \t')
            AI = Process_input(self.limit, self.numberList, numberInput, self.winNumber)
            self.numberList = AI.return_list()


    def role_2(self):
        if self.winNumber != 0:
            print('Computer:\t' + str(self.numberList[:self.winNumber]).strip('[]'))
            del self.numberList[:self.winNumber]
        else:
            random_number = randint(1, self.limit)
            print('Computer:\t' + str(self.numberList[:random_number]).strip('[]'))
            del self.numberList[:random_number]

        self.role_1()


    def start(self):
        if self.roles == 1:
            self.role_1()
        elif self.roles == 2:
            self.role_2()
        else:
            print('Error')
            return
