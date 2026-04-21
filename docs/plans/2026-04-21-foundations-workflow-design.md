# Foundations Workflow Design

**Context:** Gentlii Foundations already exposes a local Python CLI and a GitHub Actions CI workflow. The product needs to run automatically in a repository workflow now on GitHub, while keeping the automation contract portable to Azure DevOps later.

**Goal:** Trigger generation only when source files change in `product-definitions/foundations-input`, regenerate managed artifacts into `product-definitions/product-description`, and commit those generated files back to the repository.

## Recommended Approach

Use a path-filtered workflow in GitHub Actions that calls one stable CLI command against the `product-definitions` root. Keep the workflow thin and let the CLI own discovery, extraction, analysis, rendering, and file replacement for managed artifacts.

This keeps the automation portable:
- GitHub Actions handles trigger detection and git write-back.
- The CLI remains the single product entry point.
- Azure DevOps can later call the same CLI command with different pipeline YAML.

## Trigger Model

The workflow triggers only when files under `product-definitions/foundations-input/**` change.

Expected event flow:
1. A user adds or updates one or more source files under `foundations-input`.
2. GitHub Actions matches the changed path and starts the workflow.
3. The workflow installs the project and runs the CLI against `product-definitions`.
4. The CLI regenerates the managed output artifacts in `product-description`.
5. The workflow stages only `product-description` and commits if there is an actual diff.

Because the trigger is limited to `foundations-input`, the workflow does not retrigger itself when it commits generated files under `product-description`.

## Output Ownership

Managed artifact files in `product-definitions/product-description` are replaceable outputs. When the CLI regenerates a managed artifact, it fully replaces that file's contents.

Unrelated files already present in `product-description` must remain untouched if they are not part of the managed artifact set. The workflow stages only the `product-description` path, but the CLI contract is responsible for limiting writes to known artifact targets.

## Operational Behavior

- Use a bot git identity for generated commits.
- Commit only when `product-description` changed.
- Fail the workflow if extraction, analysis, rendering, or writing fails.
- Do not commit partial or stale output on failure.
- Leave the workflow implementation small so the same command can be reused in Azure DevOps later.

## Testing Expectations

Testing should focus on the stable command contract and managed-file behavior:
- Unit and integration tests for pipeline behavior that replaces managed artifact files.
- Tests proving unrelated files in `product-description` are preserved.
- A minimal workflow definition that invokes the CLI instead of re-implementing logic in YAML.

## Deferred Scope

Not included in this version:
- Manual workflow dispatch
- Broader path triggers
- PR-specific write-back behavior
- Azure DevOps pipeline files
- Additional source locations beyond `foundations-input`
