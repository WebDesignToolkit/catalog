# catalog

The canonical, machine-readable inventory of curated open-source resources.

WebDesignToolkit is a community-maintained, zero-cost-first directory of open-source resources for building better websites. We prefer evidence over hype, original documentation over copied descriptions, and agent-readable formats over loose bookmarks.

## Start here

- [.github](https://github.com/WebDesignToolkit/.github) — Organization governance, contribution standards, agent guardrails and public profile.
- [catalog](https://github.com/WebDesignToolkit/catalog) — Canonical catalog of open-source tools, design resources and verified source metadata.
- [skills](https://github.com/WebDesignToolkit/skills) — Reusable AI-agent skills for research, web design, accessibility and tool evaluation.
- [mcp-servers](https://github.com/WebDesignToolkit/mcp-servers) — MCP server directory, compatibility notes and safe setup guides.
- [workflows](https://github.com/WebDesignToolkit/workflows) — Repeatable web-design agency procedures from intake to delivery.
- [design-system](https://github.com/WebDesignToolkit/design-system) — Shared hardline tactile design tokens, CSS primitives and examples.
- [knowledgebase](https://github.com/WebDesignToolkit/knowledgebase) — Evidence-backed guides, architectural decisions and tool comparisons.
- [website](https://github.com/WebDesignToolkit/website) — Searchable zero-dependency WebDesignToolkit resource portal.

## Principles

- Favor free and open-source projects; record actual license evidence, never assume.
- Curate links and original summaries instead of copying source code.
- Every proposal retains source, review status and dates.
- Keep AI automation controlled, auditable and minimally privileged.
- No GitHub Actions workflows or unauthorized third-party crawling.

## Data

- data/resources.json: resource records derived from upstream GitHub API metadata. All start as **candidate** until reviewed.
- data/taxonomy.json: categories.
- data/resource.schema.json: JSON Schema for consumers.
- sources/seeds.json: the hand-curated seed list.
- scripts/validate.py: dependency-free structural validation.
- scripts/refresh.py: refresh upstream metadata using authenticated GitHub CLI.

The website is a derived snapshot; do not edit its copied records by hand.

## Contributing

Read [organization contributor guidance](https://github.com/WebDesignToolkit/.github/blob/main/CONTRIBUTING.md) and [agent guardrails](https://github.com/WebDesignToolkit/.github/blob/main/AGENTS.md).
