from word import newword
import re

class Main:
    def get_input(self):
        self.ip = input("Enter the guess letter: ")
        if(len(self.ip) != 1):
            print("Enter only one letter")
            self.ip = None
            return
        if(not bool(re.match("[a-z]", self.ip))):
            print("Enter a lowercase english letter")
            self.ip = None

    def __init__(self, data):
        self.cur = ['-', '-', '-', '-', '-']
        self.lives_left = 10
        self.guessed = 0
        self.data = data

    def print_state(self):
        print(''.join(self.cur))
        print(self.lives_left, " more chances left")

    def check_guess(self):
        match = False
        for i in range(len(self.data)):
            if(self.data[i] == self.ip and self.cur[i] == '-'):
                self.cur[i] = self.ip
                self.guessed += 1
                match = True
        if(not match):
            self.lives_left -= 1

    def run(self):
        result = ""
        while(self.lives_left > 0):
            if(self.guessed == 5):
                result = "You won"
                break
            self.print_state()
            self.get_input()
            self.check_guess()
            if(self.guessed == 5):
                result = "You won"
                break
        if(not result):
            result = "Good game but you lost\nThe word was " + self.data
        return result

if __name__ == '__main__':
    gameObj = Main(newword)
    print(gameObj.run())