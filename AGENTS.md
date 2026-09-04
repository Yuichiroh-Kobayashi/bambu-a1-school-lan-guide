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

Do not commit or publish school names (except when a school or institution name is part of the permitted public-source attribution described below), local government names, real internal network values, real SSIDs, passwords, access codes, proxy details, internal domains, device names, user IDs, email addresses, MAC addresses, identifiable student/staff information, internal scripts, or internal manual content.

When explaining networks, use schematic and general wording only.

## Public source attribution

Public bibliographic attribution is allowed when it is necessary to identify or credit an already-public source.

Allowed attribution may include:

- the author's name as published in the cited source;
- the author's institutional affiliation as published in the cited source;
- the publishing institution, school, university, college, company, organization, or research body;
- the official title of the public document; and
- the public source URL.

This exception covers only information that is already public in the cited source and that is needed to identify or credit that source.

As a rule, a public source URL or an equally public document must exist for any author name or affiliation that is published here. Do not add a person or an affiliation that cannot be confirmed in a public source. Private knowledge, such as personal acquaintance, private conversations, or meeting someone at a training session, is not a basis for publication.

Do not use this exception to identify the user's own school, a participating or cooperating school, a local government, students, teachers, staff, or other people involved in field practice.

Do not enrich a citation with information that is not present in the cited public source, such as email addresses, phone numbers, social accounts, researcher profiles, separately searched or inferred affiliations, or private relationships. Do not link a cited author's published affiliation to the field-practice sites described in this repository.

Publication attribution and field-practice identification are separate categories. Public attribution does not relax the privacy or internal-information rules in this file. Anonymization of school practice, student privacy, teacher and staff privacy, network secrecy, and internal operational secrecy remain unchanged.

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
