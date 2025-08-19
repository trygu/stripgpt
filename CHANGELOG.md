# Changelog

All notable changes to this project will be documented in this file.

The format loosely follows Keep a Changelog, with semantic-ish versioning.

## [0.2.0] - 2025-08-19
### Added
- Detection mode: `--detect` CLI flag outputs JSON artifact counts (no modification).
- Library function `detect_artifacts` exported.
- Comprehensive tests updated (now 13) covering detection logic and CLI.
- GitHub Actions CI workflow.
- `.gitignore` for typical Python artifacts.

### Changed
- Refactored core logic into `core.py` (earlier change but part of first feature release).
- README expanded and restored after accidental wipe.

## [0.1.0] - 2025-08-19
### Added
- Initial release: cleaning of ChatGPT markers, zero-width chars, PUA chars, optional bare tokens & line ranges.
- In-place editing with backup suffix.
- Basic test suite (later expanded).

