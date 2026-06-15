# Study Overview

## Objective

The study investigates whether LLM-generated technical documentation can aid
program comprehension and maintenance in an industrial Java system, and under
which conditions developers consider that documentation useful and trustworthy.

## Pilot Scope

The first cycle was a pilot. The AWS pipeline processed the submitted project,
but the human evaluation intentionally examined a smaller sample of ten Java
classes and the methods present in those files. The sample covered distinct
architectural roles such as DTOs, entities, services, utilities, and reporting
code.

Three experienced developers first reviewed the generated changes in a GitLab
Merge Request and registered 15 comments. A facilitated focus-group discussion
then explored recurring perceptions, disagreements, positive cases, and
adoption concerns.

## Units of Analysis

- **Technical execution:** pipeline run, targets, files, generated entries,
  validation outcomes, and documentation artifacts.
- **Review unit:** each selected Java file presented in the Merge Request,
  including class-level and method-level JavaDocs.
- **Qualitative evidence:** review comments, participant statements, discussion
  threads, and categories produced by interpretation.

Architectural layers are comparison categories, not individual units reviewed
in isolation.

## Current and Planned Artifacts

Completed in the pilot:

- structural manifest;
- generated JavaDocs;
- narrative `README.md`, `ARCHITECTURE.md`, and attempted `API.md`;
- execution reports;
- Merge Request review; and
- focus-group analysis.

Planned refinements:

- selective documentation of higher-value targets;
- valid OpenAPI generation and validation;
- functional service documentation;
- documentation supporting manual tests; and
- comparative developer evaluation of these artifact types.
