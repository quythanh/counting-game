from random import randint

class Process_input():
    def __init__(self, limit, numberList, numberInputed, winNumber):
        self.limit = limit # Limit on the amount of numbers can be entered each time
        self.numberList = numberList # List of numbers [1; 30]
        self.inputList = numberInputed.split(',')
        self.winNumber = winNumber
        self.length = len(self.inputList)
        for i in range(self.length):
            self.inputList[i] = int(self.inputList[i].strip(' ')) # Change string-typed numbers to integer


    def check_length(self):
        if self.length == 0 or self.length > self.limit:
            print(f'--->> Error: You must type at least 1 number and NO MORE {self.limit} numbers')
            return False
        return True


    def check_ordinarily(self):
        if self.check_length():
            if self.inputList == self.numberList[:self.length]:
                return True
            else:
                print('--->> Error: You must type in a correct order.')
        return False


    def delete_list(self):
        if self.check_ordinarily():
            del self.numberList[:self.length]
            return True
        else:
            return []


    def return_list(self):
        if self.delete_list():
            if len(self.numberList) == 0:
                print('You win! Congratulation :)')
                return []
            elif len(self.numberList) < (self.limit + 1):
                print('Computer:\t' + str(self.numberList).strip('[]'))
                print('You lose :(')
                return []
            elif (int(self.inputList[-1]) % (self.limit + 1)) != self.winNumber:
                if (int(self.inputList[-1]) % (self.limit + 1)) < self.winNumber:
                    catch = self.winNumber - (int(self.inputList[-1]) % (self.limit + 1))
                else:
                    catch = self.limit - (int(self.inputList[-1]) % (self.limit + 1)) + self.winNumber + 1
                print('Computer:\t' + str(self.numberList[:catch]).strip('[]'))
                del self.numberList[:catch]
                return self.numberList
            else:
                random_number = randint(1, self.limit)
                print('Computer:\t' + str(self.numberList[:random_number]).strip('[]'))
                del self.numberList[:random_number]
                return self.numberList
        return []
