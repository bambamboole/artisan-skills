---
name: artisan-debug
description: Use when diagnosing a bug, regression, failing test, unexpected behavior, or production error.
---

# Debug Root Causes

Establish the failure with evidence before editing. Trace inputs, state, and every caller through the shared path;
distinguish the symptom from the first incorrect assumption or boundary. Fix the root cause where all affected callers
benefit, not each visible symptom. Preserve valid behavior and avoid unrelated cleanup. Add or update one focused
regression check that fails before the fix and passes after it. Verify the reported path and state any remaining
uncertainty plainly.
