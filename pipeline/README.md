# Pipeline Reference

The pipeline is maintained separately:

- Repository: <https://github.com/murilloed/simple-java-docs-pipeline>
- Audited commit: `a5c098661725272d58b093c1f28520e6b3758c65`
- Commit date: 2026-02-03

Pin this commit when reproducing the reported technical run. Later revisions may
change prompts, selection rules, AWS resources, model configuration, or report
schemas.

## Verified Behavior at the Pinned Commit

- JavaParser identifies eligible public declarations.
- `maxTargets` limits all target types collectively, not methods alone.
- Target kinds include classes/interfaces, constructors, methods, and enums.
- The implementation invokes an LLM through Amazon Bedrock Runtime.
- JavaDocs are injected into a copied source tree.
- Project-level generation targets `README.md`, `ARCHITECTURE.md`, and `API.md`.
- `API.md` is narrative Markdown and is not OpenAPI.

Consult the pipeline repository for infrastructure and execution instructions.
Do not copy industrial credentials or environment configuration into a
reproduction.
