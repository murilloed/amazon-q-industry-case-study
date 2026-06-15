# Reproducibility Guide

## Public Reproduction

The public experiment uses the synthetic project under
`artifacts/sanitized-sample/input/`. It is designed to exercise the same
pipeline stages without disclosing the industrial application.

1. Obtain the pipeline implementation pinned in `pipeline/README.md`.
2. Configure a dedicated AWS account or sandbox with least-privilege access.
3. Package the synthetic input as a ZIP file.
4. Submit it through the pipeline interface or its documented upload path.
5. Preserve the produced manifest, JavaDoc report, documentation report, and
   generated files.
6. Compare aggregate output with the example under
   `artifacts/sanitized-sample/expected/`.

Exact generated prose may vary with model version, inference parameters, prompt
version, and service updates. Structural counts and execution provenance should
therefore be reported separately from textual quality.

## Industrial Replication

The original archives are not needed to validate the public workflow. Access to
them requires software-owner authorization and compliance with applicable
privacy and research-governance requirements. See
`artifacts/restricted-source/ACCESS.md`.

## Human Evaluation

The qualitative pilot reviewed a ten-class sample through a Merge Request. A
replication should preserve:

- the sample-selection rule;
- the exact generated revision;
- participant inclusion criteria;
- the individual-review period;
- facilitator questions;
- comments linked to code locations;
- the coding procedure; and
- negative as well as positive evidence.

The complete pipeline output must not be conflated with the human-reviewed
sample.
