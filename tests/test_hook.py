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
            "artisan-visual-brainstorming",
            "artisan-php",
            "artisan-react",
            "artisan-typescript",
            "writing",
        ):
            self.assertIn(skill, context)
        self.assertNotIn("ponytail", context.lower())
        self.assertNotIn("superpowers", context.lower())

    def test_parallel_skill_requires_independent_ownership(self):
        skill = (ROOT / "skills/artisan-parallel/SKILL.md").read_text()

        self.assertIn("independent", skill)
        self.assertIn("non-overlapping", skill)
        self.assertIn("evidence", skill)

    def test_frontend_skill_requires_rendered_verification(self):
        frontend = (ROOT / "skills/artisan-frontend-design/SKILL.md").read_text()

        for term in ("rendered result", "100dvh", "IntersectionObserver", "empty states"):
            self.assertIn(term, frontend)

    def test_review_skill_flags_low_value_tests(self):
        skill = (ROOT / "skills/artisan-review/SKILL.md").read_text()

        for term in ("render-only", "mock tautologies", "manifest"):
            self.assertIn(term, skill)

    def test_visual_brainstorming_skill_has_a_live_mockup_workflow(self):
        skill = (ROOT / "skills/artisan-visual-brainstorming/SKILL.md").read_text()
        switcher = (ROOT / "skills/artisan-visual-brainstorming/assets/visual-direction-switcher.js").read_text()

        for term in ("2–3", "Tailwind CDN", "visual-serve"):
            self.assertIn(term, skill)
        for term in ("Compare directions", "aria-current", "Escape"):
            self.assertIn(term, switcher)

    def test_php_skill_covers_frameworks_and_validation(self):
        skill = (ROOT / "skills/artisan-php/SKILL.md").read_text()

        for term in ("Laravel", "Symfony", "Pest", "PHPStan", "Rector", "composer", "idempotent"):
            self.assertIn(term, skill)

    def test_writing_skill_covers_evidence_and_clarity(self):
        skill = (ROOT / "skills/writing/SKILL.md").read_text()

        for term in ("active voice", "concrete nouns", "Cite verifiable sources", "terminology consistent", "CC BY 4.0"):
            self.assertIn(term, skill)

    def test_react_and_typescript_skills_cover_vite_testing_and_contracts(self):
        react = (ROOT / "skills/artisan-react/SKILL.md").read_text()
        typescript = (ROOT / "skills/artisan-typescript/SKILL.md").read_text()

        for term in (
            "Vite",
            "Vitest",
            "vitest-browser-react",
            ".browser.test.tsx",
            "ResizeObserver",
            "dispatchEvent",
        ):
            self.assertIn(term, react)
        for term in (
            "tsconfig",
            "type-only imports",
            "type coverage",
            "tsc --noEmit",
            "expectTypeOf",
            "publint",
        ):
            self.assertIn(term, typescript)


if __name__ == "__main__":
    unittest.main()
