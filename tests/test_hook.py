import json
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HOOK = ROOT / "hooks" / "session-start"


class SessionHookTests(unittest.TestCase):
    def test_emits_a_concise_skill_router(self):
        result = subprocess.run([str(HOOK)], text=True, capture_output=True)

        self.assertEqual(result.returncode, 0, result.stderr)
        context = json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"]
        self.assertLessEqual(len(context.split()), 100)
        for skill in (
            "artisan-shape",
            "artisan-build",
            "artisan-debug",
            "artisan-review",
            "artisan-parallel",
            "artisan-frontend-design",
            "artisan-web-art-direction",
            "artisan-php",
            "artisan-react",
            "artisan-typescript",
        ):
            self.assertIn(skill, context)
        self.assertNotIn("ponytail", context.lower())
        self.assertNotIn("superpowers", context.lower())

    def test_parallel_skill_requires_independent_ownership(self):
        skill = (ROOT / "skills/artisan-parallel/SKILL.md").read_text()

        self.assertIn("independent", skill)
        self.assertIn("non-overlapping", skill)
        self.assertIn("evidence", skill)

    def test_frontend_skills_keep_code_and_image_work_separate(self):
        frontend = (ROOT / "skills/artisan-frontend-design/SKILL.md").read_text()
        art_direction = (ROOT / "skills/artisan-web-art-direction/SKILL.md").read_text()

        self.assertIn("rendered result", frontend)
        self.assertIn("one horizontal reference image per section", art_direction)

    def test_php_skill_covers_frameworks_and_validation(self):
        skill = (ROOT / "skills/artisan-php/SKILL.md").read_text()

        for term in ("Laravel", "Symfony", "PHPUnit", "static analysis"):
            self.assertIn(term, skill)

    def test_react_and_typescript_skills_cover_vite_testing_and_contracts(self):
        react = (ROOT / "skills/artisan-react/SKILL.md").read_text()
        typescript = (ROOT / "skills/artisan-typescript/SKILL.md").read_text()

        for term in ("Vite", "Vitest", "vitest-browser-react", ".browser.test.tsx"):
            self.assertIn(term, react)
        for term in ("tsconfig", "type-only imports", "type coverage", "tsc --noEmit"):
            self.assertIn(term, typescript)


if __name__ == "__main__":
    unittest.main()
