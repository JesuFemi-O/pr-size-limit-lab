# Proposal: a size limit for pull requests

This is the spec the sandbox validates as code. It is self-contained; the
implementation lives in `scripts/pr_size_check.py`, `.github/workflows/pr-size.yml`,
and `.github/pr-size.yml`.

## The problem

When contributions are developed with the help of coding agents, a focused
task can quietly turn into a much broader change — adjacent refactors,
cleanup, and related work picked up along the way. Large diffs cause two
problems:

- Review quality falls as the number of changed files grows. Details are
  easier to miss and reviewers need much more time to see how everything
  fits together.
- Work that could be reviewed as a series of small changes arrives as one
  large PR instead.

The goal is a predictable, mechanically enforced guardrail that keeps each
PR focused and reviewable, communicated early — before a sprawling change
reaches review.

## Proposed rule

Limit each PR to **8 counted files changed**.

Eight files leaves room for a typical change: implementation, tests,
documentation, configuration, and a few supporting updates. Changes that
need more files should be submitted as a sequence of PRs — stacked manually
by choosing the base branch, or managed with a tool such as `gh-stack`.

## Why count files instead of lines?

A line-count limit sounds more precise but rejects changes that are large
without being broad — e.g. a focused change that rewrites one existing large
module. File count is a rougher but more useful proxy for how widely a
change reaches: it discourages sprawl without penalising deep work in an
existing file.

## Exemptions

### Template contents

Files under `src/minicity/templates/**` do not count toward the limit. A
contributor-facing template is an atomic bundle; splitting its files across
PRs would leave it broken at intermediate stages without making the final
change easier to review. Only files inside the template directory are
excluded — registration, tests, and other files changed alongside it still
count.

### Release-promotion PRs

A PR whose head branch matches `^v\d+\.\d+\.\d+$` and targets `main` is
fully exempt. It rolls up changes already reviewed individually during the
release cycle, so it is not a new unit of work.

## Optional addition: limit the size of new source files

Newly **added** `src/**/*.py` files are capped at **300 lines**. This
applies only to new files, so it does not penalise edits to modules that are
already large. Scoping it to Python under `src/` naturally excludes tests,
docs, fixtures, data, and template contents.

## Rollout

Both checks start as non-blocking **warnings** (`mode: warn`). That surfaces
how often they trigger and which legitimate cases need a new exemption.
Once the limits have proven useful, flip `mode: fail` to make the check
required.
