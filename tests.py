import unittest
from functions.write_file import write_file

class TestMain(unittest.TestCase):
    def setUp(self):
        pass

    def test_write_file_valid(self):
        return_value = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(return_value)

    def test_write_file_valid_new_file(self):
        return_value = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(return_value)

    def test_write_file_invalid_outside_directory(self):
        return_value = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(return_value)
        self.assertIn("Error: Cannot list", return_value)

if __name__ == "__main__":
    unittest.main()