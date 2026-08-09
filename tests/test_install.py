import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTALL = ROOT / "bin" / "install"
CHECK = ROOT / "bin" / "check"
SKILLS = (
    "artisan-shape",
    "artisan-build",
    "artisan-debug",
    "artisan-review",
    "artisan-parallel",
    "artisan-frontend-design",
    "artisan-web-art-direction",
    "artisan-kotlin-backend",
    "artisan-react",
    "artisan-typescript",
)


class InstallTests(unittest.TestCase):
    def run_install(self, home):
        environment = os.environ | {"HOME": str(home)}
        return subprocess.run(
            [str(INSTALL)], cwd=ROOT, env=environment, text=True, capture_output=True
        )

    def test_installs_links_and_preserves_marketplace_entries(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            marketplace = home / ".agents/plugins/marketplace.json"
            marketplace.parent.mkdir(parents=True)
            marketplace.write_text(
                json.dumps({"name": "personal", "plugins": [{"name": "existing"}]})
            )

            result = self.run_install(home)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual((home / "plugins/artisan-skills").resolve(), ROOT)
            for runtime in (".agents/skills", ".claude/skills"):
                for skill in SKILLS:
                    self.assertEqual((home / runtime / skill).resolve(), ROOT / "skills" / skill)

            plugins = json.loads(marketplace.read_text())["plugins"]
            self.assertEqual([plugin["name"] for plugin in plugins], ["existing", "artisan-skills"])
            self.assertEqual(plugins[-1]["source"]["path"], "./plugins/artisan-skills")

    def test_is_idempotent_and_refuses_conflicting_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)

            self.assertEqual(self.run_install(home).returncode, 0)
            self.assertEqual(self.run_install(home).returncode, 0)
            plugins = json.loads((home / ".agents/plugins/marketplace.json").read_text())["plugins"]
            self.assertEqual([plugin["name"] for plugin in plugins].count("artisan-skills"), 1)

        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            conflict = home / ".claude/skills/artisan-build"
            conflict.parent.mkdir(parents=True)
            conflict.write_text("keep me")

            result = self.run_install(home)

            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(conflict.read_text(), "keep me")

    def test_check_accepts_an_installed_framework(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            self.assertEqual(self.run_install(home).returncode, 0)

            result = subprocess.run(
                [str(CHECK)],
                cwd=ROOT,
                env=os.environ | {"HOME": str(home)},
                text=True,
                capture_output=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("ok", result.stdout)

    def test_plugin_manifest_has_required_presentation_metadata(self):
        manifest = json.loads((ROOT / ".codex-plugin/plugin.json").read_text())

        self.assertIsInstance(manifest.get("author"), dict)
        self.assertIsInstance(manifest.get("interface"), dict)


if __name__ == "__main__":
    unittest.main()
