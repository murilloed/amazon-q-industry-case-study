# Industrial Java Documentation Reconstruction: Replication Package

This repository contains the public research artifacts for a master's study on
LLM-assisted documentation reconstruction in an industrial Java system.

The study combines:

- an AWS pipeline that performs static analysis and invokes an LLM through
  Amazon Bedrock Runtime;
- automated JavaDoc and project-level documentation generation;
- review of a ten-class sample through a GitLab Merge Request;
- a focus group with three experienced developers and one facilitator; and
- qualitative analysis of clarity, correctness, usefulness, consistency, and
  adoption conditions.

## Important Scope Distinctions

The pipeline processed the complete submitted project and identified 1,478
public documentation targets. It modified 523 Java files by adding 1,466
JavaDoc entries. The human pilot did not evaluate all those entries. It
reviewed a deliberately limited sample of ten classes, including the methods
contained in those files, across different architectural roles.

The versioned pipeline invokes models through Amazon Bedrock Runtime. References
to Amazon Q in early study materials describe the initial technological framing
of the pilot and should not be interpreted as evidence that the released
implementation called an Amazon Q API.

`API.md` is a generated narrative artifact. It is not an OpenAPI specification.
OpenAPI generation and documentation for manual testing are planned extensions,
not completed pilot results.

## Repository Map

| Path | Content |
|---|---|
| [`docs/`](docs/) | Study design, methodology, architecture, ethics, threats, and future work |
| [`pipeline/`](pipeline/) | Reproduction instructions and the exact pipeline implementation reference |
| [`artifacts/`](artifacts/) | Restricted-data manifest and a publishable synthetic example |
| [`results/`](results/) | Verified technical results and qualitative findings |
| [`scripts/`](scripts/) | Release verification and sanitization utilities |

## Restricted Industrial Artifacts

The original SARSB source archive and the full generated output are not
published in this repository. They contain institutional implementation
details, environment information, authentication and integration code, and
personal-data concepts. Sanitization alone does not establish redistribution
rights.

The archives are represented by cryptographic checksums, an inventory, and an
access protocol in [`artifacts/restricted-source/`](artifacts/restricted-source/).
This preserves provenance without exposing protected material.

## Reproduction Levels

1. **Public structural reproduction:** run the pipeline on the synthetic Java
   sample included here.
2. **Pipeline reproduction:** use the independently versioned pipeline at the
   pinned commit documented in [`pipeline/README.md`](pipeline/README.md).
3. **Restricted industrial replication:** requires authorization from the
   software owner and approval under the applicable ethics, privacy, and data
   governance procedures.

## Citation

Use the metadata in [`CITATION.cff`](CITATION.cff). Until the dissertation or a
related paper receives a persistent identifier, cite this repository and its
release or commit hash.

## License and Data Rights

Repository-authored documentation and scripts are covered by the repository
license. No license is granted here for the SARSB source code, generated
derivatives of that code, institutional identifiers, third-party assets, or
personal data.
