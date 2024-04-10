from main import Main
import unittest
from mock import patch

class TestAll(unittest.TestCase):
    def setUp(self):
        self.data = "apple"
        self.gameObj = Main(self.data)
        # print("setup")

    def test_get_input_valid(self):
        with patch('builtins.input', return_value='a'):
            self.gameObj.get_input()
            self.assertEqual(self.gameObj.ip, 'a')
        # print("correct guess")

    def test_get_input_invalid_length(self):
        with patch('builtins.input', return_value='ab'):
            self.gameObj.get_input()
            self.assertIsNone(self.gameObj.ip)
        # print('invalid length')

    def test_get_input_invalid_character(self):
        with patch('builtins.input', return_value='1'):
            self.gameObj.get_input()
            self.assertIsNone(self.gameObj.ip)
        # print('invalid character')

    def test_check_guess_correct_guess(self):
        self.gameObj.ip = 'a'
        self.gameObj.check_guess()
        self.assertEqual(self.gameObj.cur, ['a', '-', '-', '-', '-'])
        # print('hey')

    def test_check_guess_incorrect_guess(self):
        self.gameObj.ip = 'z'
        self.gameObj.check_guess()
        self.assertEqual(self.gameObj.lives_left, 9)
        # print('incorrect guess')

    def test_run_game_winning(self):
        self.gameObj.guessed = 5
        result = self.gameObj.run()
        self.assertTrue(result.startswith("You won"))
        # print('winning')

    def test_run_game_losing(self):
        self.gameObj.lives_left = 0
        result = self.gameObj.run()
        self.assertTrue(result.startswith("Good game but you lost"))
        # print('losing')

if __name__ == '__main__':
    unittest.main()
