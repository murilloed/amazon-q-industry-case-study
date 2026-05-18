# General Scope of the Focus Group Process

## Complete Methodological Process

---

# 1. Research Planning

## Objective of the Stage

Define how LLM-based technology would be evaluated within a real industrial context.

---

## What Was Defined

- Use of Amazon Q Developer (AWS)
- Automatic JavaDoc generation
- Application to real classes from the SARSB system
- Qualitative evaluation through a focus group
- Simulation of a real review process using GitLab Merge Request

---

## Methodological Foundation

The research was structured as:

- qualitative exploratory study;
- contextual observation;
- interpretative analysis of developers’ perceptions.

---

# 2. Construction of the Automated Pipeline

## Objective

Automate the generation of technical documentation using generative AI.

---

## Executed Process

### Step 1 — Class Selection

A Python script was developed to randomly select 10 real classes from the legacy system.

---

### Step 2 — Processing via Amazon Q

The pipeline sent the classes to Amazon Q Developer, responsible for:

- interpreting the code;
- inferring context;
- automatically generating JavaDocs.

---

### Step 3 — Documentation Injection

The documentation was inserted directly into the source code:

- class comments;
- method comments;
- parameter descriptions;
- inferred behavior descriptions.

---

### Step 4 — Versioning

The changes were organized into:

- a dedicated branch;
- a GitLab Merge Request;
- a workflow similar to a real industrial environment.

---

# 3. Focus Group Preparation

## Objective

Create a controlled environment for collaborative evaluation.

---

## Participants

- 3 experienced developers;
- 1 researcher/facilitator.

---

## Participant Criteria

Participants had:

- software development experience;
- familiarity with code review practices;
- knowledge of the system context.

---

# 4. Definition of the Experimental Dynamics

## Session Structure

| Stage | Duration |
|---|---|
| Introduction | 5 min |
| Context Setting | 5 min |
| Individual Analysis | 15 min |
| Guided Discussion | 25 min |
| Closing | 10 min |

---

# 5. Focus Group Execution

## Session Opening

The researcher explained:

- that the objective was not to evaluate the functional code;
- but rather the quality of the automated documentation.

It was also emphasized:

- researcher neutrality;
- absence of solution advocacy;
- participants’ freedom for critical evaluation.

---

# 6. Practical Activity

## Executed Process

Participants:

- accessed the Merge Request;
- analyzed the documented classes;
- compared versions;
- submitted comments directly in GitLab.

---

## Evaluation Criteria

- clarity;
- usefulness;
- consistency;
- correctness;
- semantic value.

---

# 7. Data Collection

## Collected Data

### Objective Data

- 10 analyzed classes;
- 15 comments in GitLab;
- multiple review threads.

---

### Subjective Data

- opinions;
- criticisms;
- suggestions;
- trust perception;
- adoption perception.

---

## Main Source

Full focus group transcript.

---

# 8. Qualitative Analysis Process

## Analytical Strategy

The following procedures were performed:

- interpretative reading;
- thematic categorization;
- recurrence grouping;
- participant perception analysis.

---

# 9. Emergent Categories

The analysis revealed six major central themes.

---

# THEME 1 — Documentation Redundancy

## Observed Evidence

Participants reported:

- repetition of the code itself;
- absence of new information;
- excessive unnecessary text.

---

## Examples

> “Redundant documentation, no real gain.”

> “You could just read the file name.”

---

## Interpretation

The AI was able to syntactically describe the code; however:

- it failed to add semantic value;
- it did not contextualize business rules;
- it merely transformed names into sentences.

---

## Observed Impacts

### Technical

- visual pollution;
- increased maintenance effort.

### Cognitive

- mental overload;
- loss of efficiency in code review.

---

# THEME 2 — Lack of Semantic Value

## Evidence

Participants pointed out that the documentation:

- described “what” the code does;
- but did not explain “why” it exists.

---

## Identified Problem

Absence of:

- context;
- business rules;
- expected behavior;
- architectural motivation.

---

## Relevant Scientific Insight

This was one of the most important results of the research:

> “Good documentation explains why, not only what.”

This finding strengthens the hypothesis that LLMs still present semantic limitations in complex legacy systems.

---

# THEME 3 — Inconsistency

## Evidence

Participants identified:

- different levels of detail;
- varying patterns;
- mixed languages;
- irregular formats.

---

## Interpretation

The AI failed to maintain:

- uniformity;
- standardization;
- documentation predictability.

---

## Impacts

### Organizational

- reduced trust;
- adoption difficulty.

### Technical

- heterogeneous documentation;
- inconsistent maintenance.

---

# THEME 4 — Critical AI-Generated Errors

## Most Critical Result of the Research

The AI:

- added nonexistent imports;
- inferred removed integrations;
- created incorrect elements.

João explicitly highlighted this during the session:

> “The AI inserted package imports.”

---

## Interpretation

Behavior similar to hallucination was identified.

---

## Scientific Implications

This point is extremely strong for the dissertation because it demonstrates:

- operational risk;
- the need for human supervision;
- practical limitations of full automation.

---

# THEME 5 — Positive Cases

## Where the AI Performed Better

The documentation achieved better acceptance in:

- services;
- complex rules;
- business flows;
- less trivial logic.

---

## Important Insight

The value of the AI proved to be:

- context-dependent;
- code-complexity-dependent.

---

# THEME 6 — Misalignment Between Name and Behavior

## Important Discovery

The AI exposed hidden architectural problems.

---

## Observed Example

Methods:

- had simple names;
- but performed multiple responsibilities.

---

## Relevant Scientific Result

Automated documentation also began acting as:

- an indirect architectural auditing mechanism;
- a design problem detector.

This is a VERY strong point for academic discussion.

---

# 10. Analysis by Class Type

| Type | Perception |
|---|---|
| DTO | Highly redundant |
| Entity | Low value |
| Service | High usefulness |
| Utility | Good clarity |
| Reporting/POI | Mixed result |

---

## General Interpretation

Automated documentation:

- performs better in complex code;
- adds little value in trivial code.

---

# 11. Guided Questions

The focus group also analyzed:

- quality;
- granularity;
- consistency;
- language;
- Merge Request strategy;
- real-world adoption.

---

# General Results of the Guided Questions

## Quality

### Conclusion

- useful in complex scenarios;
- redundant in simple scenarios.

---

## Classes vs Methods

### Dominant Preference

- class-level documentation;
- methods only when critical.

---

## Language

### Result

- mandatory need for standardization;
- contextual preference according to the project.

---

## Delivery Strategy

### Conclusion

- documentation should accompany development;
- it should not be created in isolation.

---

## Adoption

### General Result

- partial adoption;
- only in complex areas;
- mandatory human review required.

---

# 12. Final Analytical Conclusion

The focus group demonstrated that:

# LLM-Based Automated Documentation

## Has Potential

- onboarding;
- initial understanding;
- support for complex code.

---

## However, It Still Presents Critical Limitations

- redundancy;
- inconsistency;
- superficiality;
- hallucinations;
- low reliability without supervision.

---

# Main Scientific Finding

The main contribution of the research is demonstrating that:

> The value of automated documentation does not lie in describing syntax, but in explaining meaning, context, and architectural intention.

---

# Academic Contribution of the Dissertation

This work contributes by empirically demonstrating:

- real limitations of LLM usage in software engineering;
- human perception regarding automated documentation;
- cognitive impact of AI during code review;
- need for human governance;
- importance of semantic context.

---

# Potential Dissertation Chapters

The results can be structured as follows:

1. Experimental Context
2. Pipeline Construction
3. Focus Group Execution
4. Data Collection Strategy
5. Thematic Analysis
6. Emergent Categories
7. Discussion of Results
8. Implications for Software Engineering
9. Limitations
10. Future Work

---

# Strongest Result of the Research

In practice, the research demonstrated that:

LLMs are capable of generating syntactic documentation.

However, they still:

- do not fully understand context;
- do not replace human knowledge;
- require supervision;
- add value mainly in complex code.

This is an extremely consistent scientific result for an exploratory study conducted in a real industrial environment.
