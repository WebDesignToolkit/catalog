# Curation policy

An upstream GitHub repository is a candidate when it is relevant to web design, site delivery, component tooling, accessibility, testing, automation or agent interfaces.

## Source of truth
GitHub API provides repository identity, description, stars, license metadata, archived state and timestamps. Metadata is evidence of what GitHub reports, not independent verification of license terms or tool quality.

## Review progression
- candidate: automatically imported; unreviewed and not recommended.
- reviewed: maintainer confirms license files, use cases, maintenance, permissions, privacy and a basic functionality check. Add evidence in knowledgebase before promoting.
- rejected: unsuitable or incompatible, with documented rationale.

No rankings inferred from star counts. Avoid false equivalence: a tool's GitHub license metadata may be NOASSERTION despite an upstream license file. Mark unresolved rather than guess.

## Refresh frequency
Use an explicitly run local job with GitHub CLI. No GitHub Actions. Keep manual review outcomes stable when refreshing metadata.
