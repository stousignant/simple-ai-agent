import unittest
from functions.get_files_info import get_files_info, get_file_content

class TestMain(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_files_info_valid(self):
        return_value = get_file_content("calculator", "main.py")
        print(return_value)

    def test_get_files_info_valid2(self):
        return_value = get_file_content("calculator", "pkg/calculator.py")
        print(return_value)

    def test_get_files_info_invalid_outside_directory(self):
        return_value = get_file_content("calculator", "/bin/cat")
        self.assertIn("Error: Cannot list", return_value)
        print(return_value)

    def test_get_files_info_invalid_file(self):
        return_value = get_file_content("calculator", "pkg/does_not_exist.py")
        self.assertIn("Error: File not found", return_value)
        print(return_value)

if __name__ == "__main__":
    unittest.main()