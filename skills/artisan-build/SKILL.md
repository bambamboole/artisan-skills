---
name: artisan-build
description: Use when implementing a feature, bug fix, refactor, template, or UI behavior.
---

# Build Minimally

Trace the touched flow and reuse existing code before adding anything. Prefer standard library, native platform
features, and the smallest safe diff. Do not add speculative configuration, abstractions, or dependencies. For backend
or domain behavior, write a failing focused test first, then implement only enough to pass. For templates and
client-only UI behavior, implement first and verify the observable result; use a browser test when the behavior exists
only in the browser. Run the narrowest relevant check and report what it proved.
