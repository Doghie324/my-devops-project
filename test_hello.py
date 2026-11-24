import subprocess
import unittest


class HelloTest(unittest.TestCase):
    def test_hello_script_prints_message(self):
        result = subprocess.run(
            ["python3", "hello.py"],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(result.stdout.strip(), "Hello, DevOps!")


if __name__ == "__main__":
    unittest.main()
