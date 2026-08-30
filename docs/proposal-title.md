# Proposal: standardize pull request titles

This is the spec the sandbox validates as code. It is self-contained; the
implementation lives in `scripts/pr_title_check.py`,
`.github/workflows/pr-title.yml`, and `.github/pr-title.yml`.

## The problem

There is no documented or enforced convention for PR titles. Contributors
have generally adopted a `type(scope): description` format by following the
existing commit style, but usage is inconsistent — some titles follow the
pattern, some use it loosely, and others omit the type or scope entirely.

PRs also do not consistently identify the work they address. Work may be
tracked in either GitHub issues or Jira tickets under the `PTC` project.
GitHub issues are synced to Jira through `jira-sync.yml`, but Jira is also
used directly for work that has no corresponding GitHub issue. As a result,
some PRs reference a GitHub issue, some reference a Jira ticket, and some
reference neither.

One title convention can address both problems: a PR title should give a
readable summary, identify the kind of change, and point to the issue or
ticket the work belongs to.

## Proposed format

```text
type(scope): description
```

### Type

One of: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `ci`.

### Scope

For `feat`, `fix`, `refactor`, `test`, and `docs`, the scope must identify
the work being addressed:

- `gh-<N>` for a GitHub issue in this repository
- `PTC-<N>` for a Jira ticket

```text
feat(gh-128): add layer materialization command
fix(PTC-300): correct dbt profile resolution on Windows
docs(gh-142): explain release branch workflow
```

For `chore` and `ci`, the scope may be free-form:

```text
chore(deps): bump typer to 0.16
ci(pypi-publish): use trusted publishing
```

`chore` and `ci` are exempt from the issue-reference requirement because
routine maintenance and CI changes do not always justify creating a separate
issue first.

### Description

Must be present and must not end with a period.

### Length

The complete title, including type and scope, must not exceed **100
characters**.

## Why put the issue reference in the title?

Making the reference part of the scope gives every non-maintenance PR a
visible, searchable connection to its underlying work, and keeps enforcement
simple: the format and the issue-reference requirement can be checked
together when a PR is opened or edited, without parsing the body or querying
either tracker.

The trade-off: a reference such as `gh-128` in the title will not
auto-close the GitHub issue on merge. Contributors can still add
`Closes #128` to the PR body when they want that. The check does not verify
that a referenced issue or ticket exists, is open, or matches the PR —
contributors are trusted to use the right reference. Deeper validation can
be added later.

## Why `PTC` is uppercase

Jira ticket references use the canonical uppercase form (`PTC-300`). The
existing `jira-sync.yml` looks for ticket references with the case-sensitive
pattern `PTC-\d+`; allowing `ptc-300` would introduce a second convention
that automation does not recognize. GitHub references stay lowercase
(`gh-128`) to distinguish them clearly from Jira keys.

## Why `chore` and `ci` are exempt

Dependency updates, lint config, release automation, and similar work do not
always need their own issue. Keeping the exemption type-based makes the rule
predictable: `chore` and `ci` may use a free-form scope; every other type
must use a `gh-<N>` or `PTC-<N>` reference. This means `fix(ci): ...` fails —
the contributor must either classify the change as `ci`, or reference the
issue the fix addresses. That is preferable to maintaining a growing list of
special-case scopes.

## Why 100 characters?

Based on the repository's own history rather than a generic convention.
Across the merged PRs examined:

| Statistic | Length |
| --- | ---: |
| Minimum | 14 |
| Maximum | 88 |
| Mean | 58.4 |
| Median | 66 |
| 90th percentile | 80 |
| 95th percentile | 86 |

A 72-character limit would reject roughly one fifth of historical titles,
including clear, well-scoped ones. 100 characters covers the existing
history with headroom above the current maximum of 88, while still
preventing titles from becoming full descriptions.

## Release-promotion exemption

A PR is exempt from the title convention when its base branch is `main` and
its head branch matches `v\d+\.\d+\.\d+`. Such a PR is a collection of
already-reviewed changes, not a single unit of work, so requiring one
reference would not be useful.

## Bots

No separate bot exemption is expected to be needed — Dependabot's titles
already use `chore(deps): bump X from A to B`. `ignore_authors` in the
config is available as a narrow escape hatch if another bot produces
non-conforming titles.

## Multi-PR work

When an issue is too large for one reasonably sized PR, the preferred
pattern is to split it into smaller GitHub sub-issues, each addressed by one
focused PR using its own `gh-<N>` scope. The parent issue stays the record
of the overall goal. This is a documented convention, not something the
check enforces — verifying sub-issue relationships would require API calls.

## Rollout

The check starts as a visible but non-blocking warning (`mode: warn`), so
contributors have time to adopt the convention and we can find cases the
rule does not handle well. Once the format has settled, flip `mode: fail` to
make it required.

## What the check validates

1. The type is allowed.
2. `feat`, `fix`, `refactor`, `test`, `docs` use a `gh-<N>` or `PTC-<N>` scope.
3. `chore` and `ci` have a non-empty, free-form scope.
4. A description is present with no trailing period.
5. The complete title is no longer than 100 characters.
6. Release-promotion PRs, and `ignore_authors`, are exempt.

## Open question

Should small documentation corrections be allowed a free-form `docs` scope,
or should every documentation change point to an issue or ticket? The
stricter rule (the default here — `docs` is in `issue_ref_types`) is simpler
and keeps docs work traceable, but adds overhead for minor fixes. Moving
`docs` from `issue_ref_types` to `freeform_scope_types` in
`.github/pr-title.yml` is the whole change if we decide to relax it.
