# AGENTS.md

This repository is a public documentation repository for a GitHub Pages site about operating Bambu Lab A1 / A1 mini printers in school and FabLab contexts.

## Public content rules

- Treat this repository as public-only.
- Do not include school-specific information.
- Do not add internal manuals or internal operational documents.
- Keep confirmed facts, field observations, and future plans clearly separated.
- Do not describe unpracticed or planned items as completed results.
- Prefer official primary sources for product and software specifications.
- Do not fill unknown or unconfirmed details with speculation.
- Do not reproduce long passages from external materials.
- Do not include personal information about students, teachers, or staff.
- Do not use student photos or campus/school photos.

## Prohibited details

Do not commit or publish school names, local government names, real internal network values, real SSIDs, passwords, access codes, proxy details, internal domains, device names, user IDs, email addresses, MAC addresses, identifiable student/staff information, internal scripts, or internal manual content.

When explaining networks, use schematic and general wording only.

## Git workflow

- Do not push or commit directly to `main`.
- Use Pull Requests for review.
- If public content changes, check whether `CHANGELOG.md` needs an update.
- Run inspection scripts even for documentation-only changes.
- Passing the public-content inspection script does not guarantee that the content is safe to publish. Human review of diffs is still required before publication.

## Validation

Before finishing documentation changes, run at least:

```bash
git diff --check
python scripts/check_public_content.py
python scripts/check_internal_links.py
```
