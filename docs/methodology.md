# Methodology

## Research Design

The pilot uses a qualitative, exploratory case-study design supported by
technical execution evidence. It combines artifact observation, individual code
review, and a facilitated focus group.

## Technical Phase

1. A Java project ZIP is uploaded.
2. The project is stored in Amazon S3 and the asynchronous workflow is
   orchestrated through the pipeline infrastructure.
3. AWS CodeBuild executes JavaParser-based structural analysis.
4. The manifest records public classes, interfaces, constructors, methods, and
   enums eligible for documentation.
5. The JavaDoc injector invokes an LLM through Amazon Bedrock Runtime and inserts
   validated comments.
6. The documentation generator attempts project-level documents.
7. Reports and output files are persisted for inspection.

## Human Evaluation Phase

1. Ten documented Java classes were presented in a GitLab Merge Request.
2. Participants reviewed the files individually, including the methods and
   generated JavaDocs contained in each class.
3. Fifteen review comments were registered.
4. Three developers participated in a guided discussion led by a facilitator.
5. Evidence was organized into emerging categories covering positive and
   negative perceptions, improvement suggestions, and recurring patterns.

## Evaluation Dimensions

- clarity;
- correctness;
- semantic usefulness;
- consistency;
- language and terminology;
- appropriate documentation scope;
- review effort;
- trust; and
- adoption potential.

## Traceability

The desired evidence chain is:

`pipeline target -> generated change -> reviewed file/method -> MR comment or
participant statement -> analytical category -> reported finding`

Only claims supported by this chain should be treated as empirical findings.
