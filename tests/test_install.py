import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTALL = ROOT / "bin" / "install"
CHECK = ROOT / "bin" / "check"
PLUGIN_NAME = "artisan"
SKILLS = tuple(sorted(path.name for path in (ROOT / "skills").iterdir() if path.is_dir()))
RETIRED_SKILLS = (
    "artisan-build",
    "artisan-debug",
    "artisan-frontend-design",
    "artisan-kotlin-backend",
    "artisan-parallel",
    "artisan-php",
    "artisan-react",
    "artisan-review",
    "artisan-shape",
    "artisan-typescript",
    "artisan-visual-brainstorming",
    "artisan-web-art-direction",
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
            self.assertEqual((home / f"plugins/{PLUGIN_NAME}").resolve(), ROOT)
            for runtime in (".agents/skills", ".claude/skills"):
                for skill in SKILLS:
                    self.assertEqual((home / runtime / skill).resolve(), ROOT / "skills" / skill)

            plugins = json.loads(marketplace.read_text())["plugins"]
            self.assertEqual([plugin["name"] for plugin in plugins], ["existing", PLUGIN_NAME])
            self.assertEqual(plugins[-1]["source"]["path"], f"./plugins/{PLUGIN_NAME}")

    def test_is_idempotent_and_refuses_conflicting_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)

            self.assertEqual(self.run_install(home).returncode, 0)
            self.assertEqual(self.run_install(home).returncode, 0)
            plugins = json.loads((home / ".agents/plugins/marketplace.json").read_text())["plugins"]
            self.assertEqual([plugin["name"] for plugin in plugins].count(PLUGIN_NAME), 1)

        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            conflict = home / ".claude/skills/build"
            conflict.parent.mkdir(parents=True)
            conflict.write_text("keep me")

            result = self.run_install(home)

            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(conflict.read_text(), "keep me")

    def test_removes_legacy_retired_skill_links(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            for runtime in (".agents/skills", ".claude/skills"):
                for skill in RETIRED_SKILLS:
                    stale_link = home / runtime / skill
                    stale_link.parent.mkdir(parents=True, exist_ok=True)
                    stale_link.symlink_to(ROOT / "skills" / skill)

            result = self.run_install(home)

            self.assertEqual(result.returncode, 0, result.stderr)
            for runtime in (".agents/skills", ".claude/skills"):
                for skill in RETIRED_SKILLS:
                    self.assertFalse((home / runtime / skill).exists())
                    self.assertFalse((home / runtime / skill).is_symlink())

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

    def test_check_rejects_unsupported_skill_frontmatter(self):
        with tempfile.TemporaryDirectory() as directory:
            temporary_root = Path(directory)
            repository = temporary_root / "repository"
            home = temporary_root / "home"
            shutil.copytree(ROOT, repository)
            skill = repository / "skills/git-and-github/SKILL.md"
            skill.write_text(
                skill.read_text().replace(
                    "name: git-and-github\n",
                    "name: git-and-github\nmodel: unsupported-model\n",
                    1,
                )
            )
            environment = os.environ | {"HOME": str(home)}

            install = subprocess.run(
                [str(repository / "bin/install")],
                cwd=repository,
                env=environment,
                text=True,
                capture_output=True,
            )
            result = subprocess.run(
                [str(repository / "bin/check")],
                cwd=repository,
                env=environment,
                text=True,
                capture_output=True,
            )

            self.assertEqual(install.returncode, 0, install.stderr)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("unsupported frontmatter field", result.stderr)

    def test_plugin_manifest_has_required_presentation_metadata(self):
        manifest = json.loads((ROOT / ".codex-plugin/plugin.json").read_text())
        claude_manifest = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())

        self.assertIsInstance(manifest.get("author"), dict)
        self.assertIsInstance(manifest.get("interface"), dict)
        self.assertEqual(manifest.get("name"), PLUGIN_NAME)
        self.assertNotIn("hooks", manifest)
        self.assertEqual(manifest["name"], claude_manifest["name"])
        release_version = manifest["version"].split("+", 1)[0]
        self.assertEqual(release_version, claude_manifest["version"].split("+", 1)[0])
        self.assertEqual(release_version, marketplace["metadata"]["version"].split("+", 1)[0])

    def test_skills_have_complete_openai_interface_metadata(self):
        for skill in SKILLS:
            metadata = ROOT / "skills" / skill / "agents/openai.yaml"

            self.assertTrue(metadata.is_file(), metadata)
            text = metadata.read_text()
            for field in ("display_name", "short_description", "default_prompt"):
                self.assertIn(f"  {field}:", text)
            self.assertIn(f"${skill}", text)


if __name__ == "__main__":
    unittest.main()
