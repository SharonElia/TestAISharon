import io
import runpy
import unittest
from contextlib import redirect_stdout
from pathlib import Path
import sys


class TestHelloScript(unittest.TestCase):
    def test_hello_script_prints_expected_output(self):
        repo_root = Path(__file__).resolve().parent
        script_path = repo_root / "hello.py"

        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            globals_dict = runpy.run_path(str(script_path))

        output_lines = captured_output.getvalue().strip().splitlines()
        self.assertEqual(output_lines, ["Sharon Test, world!", "7"])
        self.assertEqual(globals_dict.get("b"), 7)

    def test_hello_script_sets_b_to_int_7(self):
        repo_root = Path(__file__).resolve().parent
        script_path = repo_root / "hello.py"

        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            globals_dict = runpy.run_path(str(script_path))

        self.assertIn("b", globals_dict)
        self.assertIsInstance(globals_dict["b"], int)
        self.assertEqual(globals_dict["b"], 7)

    def test_hello_script_restores_stdout(self):
        repo_root = Path(__file__).resolve().parent
        script_path = repo_root / "hello.py"

        original_stdout = sys.stdout
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            runpy.run_path(str(script_path))

        self.assertIs(sys.stdout, original_stdout)


if __name__ == "__main__":
    unittest.main()

