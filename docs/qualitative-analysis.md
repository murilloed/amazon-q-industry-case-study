# Qualitative Findings

The findings below summarize the ten-class pilot. They do not generalize to all
1,478 pipeline targets.

## 1. Technical Feasibility Does Not Imply Adoption

The pipeline completed large-scale JavaDoc insertion and produced auditable
reports. Developers nevertheless required human review before accepting the
documentation.

## 2. Usefulness Varies by Code Context

Documentation for simple DTOs and entities was often perceived as redundant.
Services, utilities, reporting code, and behavior with less obvious business
meaning offered more opportunities for useful explanations.

## 3. Repeating the Code Adds Little Value

Comments that merely restated identifiers, fields, or syntax increased volume
without improving understanding. Participants valued purpose, constraints,
behavior, inputs, outputs, side effects, and business rules.

## 4. Consistency and Language Affect Trust

Variation in detail, terminology, and language made review less predictable.
Participants expressed different preferences for Portuguese or English, but the
shared concern was consistency with one project-wide convention.

## 5. Plausible Errors Make Review Mandatory

Participants identified incorrect inferences and references to elements that
did not exist. The audited narrative API document also mapped unrelated
operations to a generic `/api/users` path. Such fluent but unsupported content
can be more misleading than missing documentation.

## 6. Documentation Can Expose Existing Design Problems

When names and observed behavior diverged, the generated description sometimes
made an existing naming or responsibility problem easier to notice. This is a
secondary maintenance benefit, not proof that the generated explanation is
correct.

## 7. Adoption Depends on Selectivity and Review Cost

Participants saw potential value for onboarding and initial comprehension of
complex code. Redundancy, low confidence, and the cost of reviewing large Merge
Requests were barriers. The refined study therefore prioritizes selective
generation and smaller, contextually grouped review units.
