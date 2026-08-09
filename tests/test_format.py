import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FORMAT = ROOT / "bin" / "format"


class FormatTests(unittest.TestCase):
    def test_formats_markdown_and_supports_check_mode(self):
        with tempfile.TemporaryDirectory() as directory:
            markdown = Path(directory) / "notes.md"
            markdown.write_text("# Notes\n\n-   first item\n- second item\n")

            unchecked = subprocess.run([str(FORMAT), "--check", str(markdown)], text=True)
            self.assertNotEqual(unchecked.returncode, 0)

            formatted = subprocess.run([str(FORMAT), str(markdown)], text=True)
            self.assertEqual(formatted.returncode, 0)
            self.assertEqual(markdown.read_text(), "# Notes\n\n- first item\n- second item\n")

            checked = subprocess.run([str(FORMAT), "--check", str(markdown)], text=True)
            self.assertEqual(checked.returncode, 0)


if __name__ == "__main__":
    unittest.main()
