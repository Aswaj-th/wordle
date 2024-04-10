import requests
import re
import random

backup = ['aisle', 'crane', 'taxes', 'avail', 'wanes', 'cedar', 'lousy', 'dread', 'dirts', 'aired', 'flood', 'birth', 'purge', 'uncut', 'vowed', 'alike', 'slabs', 'prime', 'human', 'salad']

class Word:
    def get_data(self):
        response = requests.get(f"{self.api}")
        if response.status_code == 200:
            self.data = response.json()[0]
        else:
            self.data = backup[random.randint(0, len(backup)-1)]

    def validate_data(self):
        #print(self.data)
        z = re.match("([a-z]{5})", self.data)
        if bool(z) and len(self.data) == 5:
            return True
        return False

    def __init__(self):
        self.api = "https://random-word-api.herokuapp.com/word?length=5"
        self.get_data()
        if(not self.validate_data()):
            self.data = "broom"

wordobj = Word()
newword = wordobj.data