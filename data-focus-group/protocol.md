# Protocol

## Focus Group Experimental Protocol — Automated Documentation using Amazon Q Developer (AWS)

---

# Overview

This section describes the complete methodological protocol adopted during the execution of the focus group conducted as part of the Master's Degree research project.

The protocol was designed to evaluate the quality, usefulness, consistency, semantic value, and practical applicability of automatically generated documentation produced through Amazon Q Developer (AWS) in a real industrial software engineering environment.

The methodology aimed to reproduce a realistic collaborative code review scenario using GitLab Merge Requests and real Java classes extracted from a legacy system.

---

# Research Objective

The main objective of this protocol was to investigate how experienced developers perceive AI-generated documentation in practical software engineering activities.

The evaluation focused on:

- documentation clarity;
- semantic usefulness;
- contextual understanding;
- consistency;
- maintainability;
- trustworthiness;
- industrial adoption feasibility.

---

# Experimental Design

The study was structured as a qualitative exploratory investigation using a focus group methodology.

The protocol included:

- automated documentation generation;
- controlled collaborative evaluation;
- guided discussions;
- interpretative analysis;
- thematic categorization.

---

# Experimental Environment

The experiment was conducted using:

- Amazon Q Developer (AWS);
- Java source code;
- GitLab Merge Requests;
- Python automation scripts;
- a real industrial legacy system (SARSB).

---

# Automated Documentation Pipeline

## Step 1 — Class Selection

A Python script randomly selected 10 real Java classes from the legacy system.

The selected classes represented different architectural categories, including:

- DTOs;
- Entities;
- Services;
- Utilities;
- Reporting components.

---

## Step 2 — Documentation Generation

The selected classes were processed through Amazon Q Developer.

The AI was responsible for:

- interpreting the source code;
- inferring contextual information;
- generating JavaDoc documentation automatically.

---

## Step 3 — Documentation Injection

The generated documentation was inserted directly into the source code, including:

- class descriptions;
- method comments;
- parameter descriptions;
- inferred behavioral explanations.

---

## Step 4 — Versioning and Review

The modified source files were organized into:

- a dedicated Git branch;
- a GitLab Merge Request;
- a collaborative review workflow.

This approach simulated a real industrial code review process.

---

# Focus Group Structure

## Participants

The focus group consisted of:

- 3 experienced software developers;
- 1 researcher/facilitator.

---

## Participant Selection Criteria

Participants were selected according to the following criteria:

- professional software development experience;
- familiarity with code review practices;
- knowledge of the project/system context;
- experience with Java-based systems.

---

# Session Structure

| Stage | Duration |
|---|---|
| Introduction | 5 minutes |
| Contextualization | 5 minutes |
| Individual Analysis | 15 minutes |
| Guided Discussion | 25 minutes |
| Closing | 10 minutes |

---

# Session Introduction

At the beginning of the session, the researcher explained:

- the objectives of the experiment;
- the evaluation process;
- the expected participant activities.

It was emphasized that:

- the goal was not to evaluate functional correctness;
- the focus was documentation quality;
- participants were free to provide critical opinions;
- the researcher would maintain methodological neutrality.

---

# Practical Evaluation Activity

Participants were instructed to:

- access the GitLab Merge Request;
- inspect the generated documentation;
- compare documented and non-documented versions;
- provide comments directly in GitLab;
- discuss their perceptions collaboratively.

---

# Evaluation Criteria

Participants evaluated the generated documentation according to the following criteria:

- clarity;
- usefulness;
- consistency;
- correctness;
- semantic value;
- contextual adequacy;
- maintainability.

---

# Guided Questions

The discussion was guided through predefined analytical questions related to:

- documentation quality;
- redundancy;
- semantic usefulness;
- contextual understanding;
- language consistency;
- granularity;
- industrial adoption;
- code review impact.

---

# Data Collection

## Objective Data

The following objective artifacts were collected:

- generated JavaDocs;
- GitLab comments;
- review threads;
- Merge Request discussions;
- session timing information.

---

## Subjective Data

The following subjective data were collected:

- participant perceptions;
- criticisms;
- opinions;
- adoption concerns;
- usability observations;
- trust-related comments.

---

# Main Data Sources

The primary analytical sources included:

- full focus group transcript;
- GitLab review comments;
- recorded observations from the session;
- generated documentation artifacts.

---

# Analytical Methodology

The collected data were analyzed using:

- qualitative thematic analysis;
- interpretative analysis;
- recurrence analysis;
- contextual interpretation;
- quantitative frequency analysis.

---

# Ethical Considerations

The protocol ensured:

- participant anonymity when necessary;
- voluntary participation;
- freedom of expression;
- non-coercive discussion;
- methodological transparency.

---

# Research Validity

The experimental design aimed to strengthen:

- ecological validity;
- contextual realism;
- analytical consistency;
- reproducibility of the methodological process.

The use of:
- real source code;
- industrial workflows;
- collaborative code review;
- experienced developers;

helped approximate real-world software engineering conditions.

---

# Expected Contributions

The protocol was designed to support the investigation of:

- practical limitations of LLM-based documentation;
- semantic challenges in automated documentation;
- cognitive impacts during code review;
- industrial feasibility of AI-assisted documentation workflows;
- human trust in AI-generated artifacts.

---

# Final Considerations

This protocol establishes the methodological foundation for evaluating automated documentation generated by Large Language Models in industrial software engineering environments.

The structure combines:
- real development workflows;
- collaborative evaluation;
- qualitative interpretation;
- quantitative analysis;

allowing a scientifically grounded investigation regarding the effectiveness and limitations of AI-generated documentation systems.
