import unittest
from unittest.mock import MagicMock
from word import Word
from word import backup

class TestWord(unittest.TestCase):
    def setUp(self):
        self.wordobj = Word()

    def test_get_data_success(self):
        with unittest.mock.patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = ["apple"]
            self.wordobj.get_data()
        self.assertEqual(self.wordobj.data, "apple")

    def test_get_data_failure(self):
        with unittest.mock.patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 404
            self.wordobj.get_data()
        self.assertIn(self.wordobj.data, backup, "word is not in backup array")

    def test_validate_data_valid(self):
        self.wordobj.data = "hello"
        self.assertTrue(self.wordobj.validate_data())

    def test_validate_data_invalid(self):
        self.wordobj.data = "python"
        self.assertFalse(self.wordobj.validate_data())

if __name__ == '__main__':
    unittest.main()
