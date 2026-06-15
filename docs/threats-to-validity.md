# Threats to Validity

## Construct Validity

The pipeline's operational success does not measure documentation quality.
Target counts, generated entries, developer perceptions, and correctness checks
must be reported separately.

The term “API documentation” may be misunderstood. The pilot generated
narrative Markdown, not a validated OpenAPI specification.

## Internal Validity

Participant knowledge of the system, facilitator behavior, prompt design,
selected examples, and Merge Request size may have influenced perceptions.
Claims should remain linked to concrete review evidence.

## External Validity

The qualitative pilot involved three developers, one industrial Java system,
and ten reviewed classes. Findings are analytical observations for this case,
not population estimates.

## Reliability

LLM outputs may change with model identifiers, service updates, temperature,
prompt versions, timeouts, and retry behavior. Reproductions should preserve
configuration and raw execution reports where publication is authorized.

## Publication and Selection Bias

Positive examples are easier to showcase than failures. This package therefore
reports failed document generation, validation failures, skipped targets, and a
concrete hallucinated endpoint pattern.
