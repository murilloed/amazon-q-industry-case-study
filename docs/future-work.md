# Future Work

The pilot motivated a refined solution rather than establishing a final
documentation pipeline.

## Selective Documentation

Compare explicit developer selection, service-layer prioritization, structural
heuristics, and LLM-assisted ranking. The objective is to reduce redundant
documentation and review burden while preserving high-value targets.

## OpenAPI

Generate `openapi.yaml` or `openapi.json` without modifying source code, then
validate the specification syntactically and semantically. Developers should
review a purposeful endpoint sample covering representative operations, risk,
business importance, and data conditions rather than choosing endpoints
arbitrarily.

## Manual-Test Documentation

Use source code plus validated OpenAPI as inputs for candidate test scenarios:
preconditions, requests, test data classes, execution steps, expected responses,
and functional checks. Human testers remain responsible for selecting cases and
confirming expected behavior.

## Comparative Evaluation

Compare JavaDoc, functional service documentation, OpenAPI, and manual-test
support on usefulness, correctness, review effort, maintenance value, and
adoption intent.
