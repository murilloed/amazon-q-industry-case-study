# Pipeline Architecture

The implementation referenced by this package uses AWS services to execute an
asynchronous documentation workflow.

## Execution Flow

1. The user uploads a Java project through the web interface.
2. An API layer creates job metadata and stores the archive in an input S3
   bucket.
3. Queue and processing components initiate an AWS CodeBuild job.
4. CodeBuild installs dependencies and runs the pipeline.
5. JavaParser builds an AST-derived inventory in `manifest.json`.
6. `JavadocInjector` invokes a model through Amazon Bedrock Runtime and inserts
   JavaDocs into eligible public targets.
7. `DocsGenerator` attempts project-level documentation.
8. The artifact organizer writes code, documents, analysis reports, and logs to
   the output structure.
9. Status components expose progress and download information to the frontend.

## Provider Terminology

The released implementation uses the Amazon Bedrock Runtime client. Earlier
figures and presentations used “Amazon Q” as the pilot's product framing. For
technical reproducibility, results in this repository are attributed to the
versioned AWS pipeline and the model invoked through Amazon Bedrock.

## Generated Document Semantics

`API.md` is narrative Markdown inferred by the LLM. It is not a machine-readable
OpenAPI contract and was not validated as one. In the audited run it contained
incorrect endpoint associations, illustrating why generated documentation
requires source-grounded validation and human review.
