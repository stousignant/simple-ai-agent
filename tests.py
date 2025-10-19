#get_files_info("calculator", ".")
#get_files_info("calculator", "pkg")
#get_files_info("calculator", "/bin")
#get_files_info("calculator", "../")


import unittest
from functions.get_files_info import get_files_info

class TestMain(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_files_info_calculator_current_directory(self):
        return_value = get_files_info("calculator", ".")
        self.assertIn("main.py", return_value)
        self.assertIn("tests.py", return_value)
        self.assertIn("pkg", return_value)
        print(return_value)

    def test_get_files_info_calculator_valid_directory(self):
        return_value = get_files_info("calculator", "pkg")
        self.assertIn("calculator.py", return_value)
        self.assertIn("render.py", return_value)
        print(return_value)

    def test_get_files_info_not_permitted_outside_directory1(self):
        return_value = get_files_info("calculator", "/bin")
        self.assertIn("Error: Cannot list", return_value)
        print(return_value)

    def test_get_files_info_not_permitted_outside_directory2(self):
        return_value = get_files_info("calculator", "../")
        self.assertIn("Error: Cannot list", return_value)
        print(return_value)

    def test_get_files_info_not_directory(self):
        return_value = get_files_info("calculator", "main.py")
        self.assertIn("Error:", return_value)
        self.assertIn("is not a directory", return_value)
        print(return_value)

if __name__ == "__main__":
    unittest.main()