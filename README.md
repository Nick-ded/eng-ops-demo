# eng-ops-demo

Demo repository for the **Engineering Ops Desk** hackathon project.

This repo is watched by three AI agents:
- **Triage Agent** — classifies incoming issues
- **Fix Agent** — patches scoped bugs and opens PRs
- **Release Agent** — scores risk and gates deploys

## Files the agents work with

| File | Purpose |
|---|---|
| `config/auth.yaml` | Auth service config (JWT secret, token expiry) |
| `requirements.txt` | Python dependencies |
| `payments/processor.py` | Payment processing logic |

## Demo issues to file

1. **Critical** — `config/auth.yaml` has wrong `jwt_secret` value
2. **Medium** — `requirements.txt` has outdated `requests` version (CVE)
3. **Low** — cosmetic button label typo (triage only, no fix)
