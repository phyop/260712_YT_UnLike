# Portfolio Collateral

## Resume bullets

- Automated the review of 1,676 YouTube liked videos with Python and YouTube Data API v3, using a deterministic rule to preserve the nine newest items.
- Reduced destructive-operation risk by implementing dry-run previews, explicit confirmation, bounded batches, and JSON audit reporting before production execution.
- Recovered a cloud-agent deliverable from Git history, reorganized it as a standalone public repository, and established credential-safe publishing controls.
- Diagnosed OAuth/API configuration and Windows Unicode failures, enabling reliable processing of multilingual YouTube metadata.
- Coordinated Cursor and Codex in a human-approved workflow that completed 102 account updates and stopped safely on API limits.

## LinkedIn project introduction

I built a Python command-line tool to clean a YouTube “Liked videos” playlist containing 1,676 entries while preserving the nine most recent likes. The engineering challenge was not the loop—it was making destructive automation safe. The tool defaults to dry-run mode, separates planning from execution, requires explicit confirmation, limits each batch, and records results for auditing. I also resolved Google OAuth and YouTube Data API configuration issues, handled multilingual titles on Windows consoles, and protected local credentials with strict Git ignore rules. Cursor accelerated the initial implementation, while Codex supported repository recovery, validation, documentation, and the controlled production run. This project demonstrates how AI-assisted development can remain practical, reproducible, and human-governed when automation touches a real user account.

## Commit message

```text
docs: publish English project and portfolio content
```

## Pull request description

### Summary

Publish English documentation and portfolio materials for the YouTube liked-video cleanup project.

### Changes

- replace corrupted multilingual copy with complete English content
- document the OAuth, dry-run, quota, and Unicode lessons
- add English resume and LinkedIn collateral
- preserve credential-safe repository guidance

### Testing

- `python -m unittest discover -s tests -v`
- `python -m py_compile cleanup_liked.py`
- `git diff --check`
- tracked-file secret scan and CJK-language audit

### Screenshots

Not applicable; this is a command-line project.

### Future work

- resumable SQLite checkpoints and idempotent retries
- scheduled quota-aware continuation
- web approval interface
- CI across supported operating systems

## Follow-on projects

1. **Resumable job engine:** Add SQLite checkpoints, structured error classes, retry policy, and progress dashboards.
2. **AI-assisted review:** Summarize removal candidates while preserving explicit user approval.
3. **Agent workflow:** Schedule quota checks and propose the next safe batch without autonomous execution.
4. **Web interface:** Build a FastAPI approval queue with OAuth callback handling.
5. **Delivery architecture:** Add Docker, CI, secret scanning, signed releases, and multi-platform tests.
6. **Consulting template:** Generalize the safety model into an auditable cleanup agent for other SaaS APIs.
