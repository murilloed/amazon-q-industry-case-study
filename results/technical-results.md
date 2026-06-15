# Verified Technical Results

These values were extracted from the restricted output archive identified by
the checksums in `artifacts/restricted-source/checksums.sha256`.

## Structural Manifest

| Measure | Value |
|---|---:|
| Total public targets | 1,478 |
| Classes/interfaces recorded as `CLASS` | 521 |
| Methods | 866 |
| Constructors | 84 |
| Enums | 7 |
| Targets with existing JavaDoc | 9 |
| Targets without existing JavaDoc | 1,469 |

## JavaDoc Execution

| Measure | Value |
|---|---:|
| Files represented in the JavaDoc report | 523 |
| JavaDoc entries added | 1,466 |
| Skipped targets | 9 |
| Validation failures | 3 |
| Bedrock calls attempted | 1,466 |
| Bedrock calls reported successful | 1,463 |
| Bedrock calls reported failed | 0 |

The aggregate fields distinguish generated entries, model-call outcomes,
validation failures, and skipped targets. Their semantics should be reported as
recorded rather than collapsed into a single unsupported “accuracy” or
“success” percentage.

## Project-Level Documents

| Measure | Value |
|---|---:|
| Documents attempted | 3 |
| Documents reported successful | 2 |
| Documents reported failed | 1 |
| Validation failures | 0 |

The failed document was `API`, with a 30-second Bedrock client timeout recorded
in `docs_generation_report.json`. An `API.md` file nevertheless existed in the
output archive and contained incorrect endpoint associations. This discrepancy
should be treated as an artifact-provenance issue and investigated before a
future release.

## Input/Output Comparison

- Input files compared: 601
- Java files changed: 523
- Input files missing from output: 0
- Additional files inside the copied code tree: 0

Generated reports and project-level documents were stored outside that copied
code tree.
