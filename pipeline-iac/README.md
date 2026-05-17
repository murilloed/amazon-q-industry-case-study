
# Architecture, Construction and Implementation of the Automated Documentation Reconstruction Pipeline Based on LLMs

---

# 1. Introduction

Software maintenance activities are strongly dependent on code comprehension, architectural understanding, and availability of technical documentation. However, many long-lived enterprise systems suffer from incomplete, outdated, or nonexistent documentation, increasing maintenance complexity and operational risks.

In this context, this document presents the architecture, implementation, and operational flow of an automated documentation reconstruction pipeline designed for Java systems. The proposed solution integrates static source-code analysis, cloud infrastructure, and Large Language Models (LLMs) provided by AWS to automatically generate contextualized technical documentation.

The pipeline was designed and implemented as part of the experimental infrastructure used in this master's research, enabling the empirical evaluation of AI-assisted documentation generation in real industrial environments.

---

# 2. Pipeline Overview

The pipeline developed in this research consists of an automated documentation reconstruction architecture for Java systems, based on the integration of structural source-code analysis, Large Language Models (LLMs) provided by AWS, and automated technical artifact generation mechanisms.

Its primary objective is to reconstruct contextualized technical documentation from real-world source code while preserving the original structure of the system and producing artifacts that support software maintenance, architectural understanding, onboarding, and code review activities.

The solution was designed to operate in corporate Java projects characterized by the absence, incompleteness, or obsolescence of technical documentation.

The pipeline automates activities traditionally performed manually, including:
- JavaDoc generation;
- architectural documentation synthesis;
- API documentation generation;
- README generation;
- structural metadata extraction.

From an architectural perspective, the solution is composed of multiple integrated components organized into sequential processing phases.

The execution flow begins with the upload of a Java project through a React-based web interface. The uploaded artifact is stored in Amazon S3 buckets, which trigger processing events responsible for starting the automated pipeline inside AWS CodeBuild.

The pipeline then performs:
1. Structural source-code analysis;
2. Metadata extraction;
3. Context preparation;
4. LLM invocation through Amazon Bedrock and Amazon Q;
5. JavaDoc generation;
6. Documentation synthesis;
7. Artifact organization and persistence.

The generated artifacts include:
- JavaDocs;
- architecture documentation;
- API documentation;
- README files;
- execution reports;
- analysis artifacts.

The pipeline was also designed to guarantee:
- auditability;
- reproducibility;
- traceability;
- preservation of the original source code.

---

## Insert image related to:
- High-level pipeline overview
- General AWS architecture
- Macro execution flow

---

# 3. Architectural Design

The pipeline architecture was designed to separate responsibilities between analysis, orchestration, generation, and artifact organization components.

The architecture combines:
- frontend orchestration;
- cloud-based execution;
- static source-code analysis;
- LLM-based documentation generation;
- structured artifact persistence.

The main architectural components are:

| Component | Responsibility |
|---|---|
| React Frontend | Upload and orchestration |
| Amazon S3 | Artifact storage |
| AWS CodeBuild | Pipeline execution |
| JavaParser | AST generation and parsing |
| ManifestGenerator | Structural metadata extraction |
| JavadocInjector | JavaDoc generation and injection |
| DocsGenerator | High-level documentation synthesis |
| Amazon Bedrock | LLM inference |
| Amazon Q | AI-assisted generation |

The frontend does not execute heavy processing logic. Instead, it acts as an orchestration and monitoring layer for the automated execution pipeline.

---

## Insert image related to:
- Full AWS pipeline architecture
- Component communication flow
- Infrastructure overview

---

# 4. Pipeline Construction Process

The construction of the pipeline involved the integration of static code analysis techniques, AWS cloud services, and LLM-based generation strategies.

<img width="945" height="529" alt="image" src="https://github.com/user-attachments/assets/211e463b-43ae-4848-b78a-612a87a5309b" />

Figure X presents the implementation environment of the proposed pipeline, including the project structure, execution flow, and generated documentation preview. The image illustrates the integration between the documentation generation tool, the execution workflow, and the generated technical artifacts produced through the automated pipeline.

The implementation was structured around four major operational phases:
1. Project Scanning;
2. JavaDoc Generation;
3. Documentation Generation;
4. Output Structuring.

The architecture was designed to:
- avoid sending entire repositories directly to the LLM;
- preserve source-code integrity;
- support reproducibility;
- maintain execution traceability;
- enable future scalability.

Special attention was given to:
- AST-based structural extraction;
- contextual prompt generation;
- artifact organization;
- execution logging;
- automated orchestration.

---

## Insert image related to:
- Tool execution flow
- Internal pipeline modules
- Construction phases

---

# 5. Technologies Used

The pipeline integrates multiple technologies distributed across frontend, backend, orchestration, analysis, and AI generation layers.

## Frontend
- React
- CloudFront

## Storage
- Amazon S3

## Execution Infrastructure
- AWS CodeBuild

## Source-Code Analysis
- JavaParser
- AST-based parsing

## AI and LLM Integration
- Amazon Bedrock
- Amazon Q

## Development Language
- Java

## Documentation Artifacts
- JavaDoc
- Markdown
- JSON reports

These technologies were selected to provide:
- scalability;
- cloud-native execution;
- modularity;
- reproducibility;
- AI-assisted generation capabilities.

---

## Insert image related to:
- Technology stack
- AWS service interaction
- Tool integration architecture

---

# 6. Execution Flow

The operational flow of the pipeline begins when a Java project is uploaded through the web interface.

The uploaded ZIP artifact is stored in Amazon S3 and associated with a unique Job ID responsible for tracking the execution lifecycle.

---


## # Tool Execution Flow

## 1. Project Scanning (ManifestGenerator)

- Walks through Java source files
- Uses JavaParser to parse each `.java` file
- Extracts class/method/constructor metadata
- Generates `manifest.json` with project structure

---

## 2. Javadoc Generation (JavadocInjector)

- Reads `manifest.json`
- For each class/method without JavaDoc:
  - Calls Amazon Bedrock (`BedrockJavadocClient`)
    - Sends code context + metadata
    - Retry logic:
      - 3 attempts with exponential backoff
      - 1s → 2s → 3s
    - Returns AI-generated JavaDoc
  - Validates generated JavaDoc:
    - parameters
    - return types
    - exceptions
  - Injects using JavaParser's `LexicalPreservingPrinter`
  - Falls back to deterministic placeholder on failure
- Preserves original code formatting
- Generates `javadoc_report.json`

---

## 3. Documentation Generation (DocsGenerator)

- Reads:
  - `manifest.json`
  - `javadoc_report.json`
- Calls Amazon Bedrock (`BedrockDocsClient`)
  - Sends project context + structure
  - Retry logic:
    - 3 attempts with exponential backoff
  - Returns AI-generated documentation

Generated artifacts:
- `README.md`
  - overview
  - build instructions
  - components
- `ARCHITECTURE.md`
  - system design
  - data flow
  - architectural layers
- `API.md`
  - endpoints
  - interfaces
  - service contracts
- `docs_generation_report.json`

---

## 4. Output Structure

### `code/`
Contains:
- source code with injected JavaDocs

### `analysis/`
Contains:
- JSON reports
- `manifest.json`
- `javadoc_report.json`
- `docs_generation_report.json`

### `docs/`
Contains:
- README documentation
- architecture documentation
- API documentation

---

## Additional Pipeline Characteristics

- Preserves original source-code formatting
- Uses AST-based structural analysis
- Avoids direct repository-wide LLM prompting
- Maintains execution traceability
- Supports reproducibility
- Provides deterministic fallback handling
- Supports auditability through JSON reports
- Integrates cloud-native AWS execution
- Uses contextualized LLM prompting
- Generates both:
  - micro-level documentation
  - macro-level architectural documentation

# 6.1 Initial Upload

The upload interface allows users to submit real Java systems for automated analysis.

<img width="945" height="506" alt="image" src="https://github.com/user-attachments/assets/5f036f98-3285-442c-b1a1-3dbad57dc15c" />

Figure X presents the initial upload interface of the automated documentation reconstruction pipeline. Through this interface, users can submit real Java projects in ZIP format, initiating the execution lifecycle of the pipeline. The frontend acts as an orchestration layer, responsible for collecting project metadata, transferring artifacts to the AWS infrastructure, and formalizing the execution job.

The upload process collects:
- project name;
- ZIP source-code package;
- execution metadata.

At this stage:
- no analysis is performed yet;
- the job context is created;
- the artifact is prepared for execution.

---

## Insert image related to:
- Upload interface
- Initial submission screen

---

# 6.2 Project Scanning — ManifestGenerator

The first processing phase performs structural analysis of the Java project.

This phase:
- scans `.java` files;
- parses source code using JavaParser;
- generates AST structures;
- extracts metadata about:
  - classes;
  - methods;
  - constructors;
  - signatures;
  - parameters;
  - return types.

The extracted information is consolidated into `manifest.json`, which acts as a summarized structural representation of the system.

This artifact is essential because it:
- avoids sending unnecessary repository information to the LLM;
- enables reproducibility;
- supports traceability.

---

## Insert image related to:
- Project scanning flow
- AST generation
- manifest.json generation

---

# 6.3 JavaDoc Generation — JavadocInjector

After structural analysis, the pipeline identifies undocumented classes and methods.

The JavadocInjector component:
1. reads `manifest.json`;
2. selects undocumented elements;
3. prepares contextual prompts;
4. invokes the LLM through Amazon Bedrock and Amazon Q;
5. receives generated JavaDocs;
6. validates generated outputs;
7. injects documentation back into the original source code.

The injection process preserves:
- formatting;
- source-code structure;
- syntactic consistency.

<img width="945" height="506" alt="image" src="https://github.com/user-attachments/assets/527b4388-1e48-4b75-bdc6-22c76fca23f4" />

Figure X presents the JavaDoc generation process applied to the model layer of the analyzed Java project. The image shows the `User.java` class being analyzed within the pipeline execution environment, demonstrating how the tool processes domain/model classes while preserving the original source-code structure and preparing contextualized documentation through the automated LLM-based workflow.


The execution also produces `javadoc_report.json`, which records:
- modified files;
- generated documentation;
- execution results;
- possible failures.

---

## Insert image related to:
- JavaDoc generation process
- Bedrock invocation
- LLM execution flow
- Injected JavaDocs in source code

<img width="945" height="506" alt="image" src="https://github.com/user-attachments/assets/7c125466-8611-41df-9c19-2828c5a5025b" />

Figure X presents the operational execution environment of the JavaDoc generation phase. The image illustrates the interaction between the source-code structure, the internal execution flow of the pipeline, and the Java project being analyzed. The environment also demonstrates the integration between the documentation generation tool, the execution process, and the generated contextualized artifacts produced through the automated pipeline.

---

# 6.4 Documentation Generation — DocsGenerator

The pipeline also generates high-level documentation artifacts.

Using the previously extracted metadata and generated JavaDocs, the DocsGenerator component creates:
- README.md;
- ARCHITECTURE.md;
- API documentation;
- execution reports.

This stage enables documentation generation at multiple abstraction levels:
- micro level (methods/classes);
- macro level (architecture/system).

---

## Insert image related to:
- Generated README
- Architecture documentation
- API documentation
- Documentation synthesis flow

---

# 6.5 Output Structuring

At the end of execution, the pipeline organizes generated artifacts into structured directories.

The final structure includes:

## code/
Contains:
- original source code;
- injected JavaDocs.

## docs/
Contains:
- README;
- architecture documentation;
- API documentation.

## analysis/
Contains:
- manifest.json;
- execution reports;
- analysis artifacts;
- logs.

This structure guarantees:
- auditability;
- reproducibility;
- experimental traceability.

---

## Insert image related to:
- Output directory structure
- Final artifact organization

---

# 7. AWS Infrastructure Execution

The pipeline execution is fully integrated with AWS infrastructure.

<img width="945" height="405" alt="image" src="https://github.com/user-attachments/assets/1897808f-28e9-4e39-bf9e-0e806c7d14d5" />

Figure X presents the AWS CodeBuild environment used to execute the automated documentation reconstruction pipeline. The dashboard provides visibility into build history, execution status, duration, and operational monitoring of the pipeline. This infrastructure is responsible for orchestrating the execution lifecycle of the documentation generation process within the AWS cloud environment.

The operational flow includes:
1. Upload to S3;
2. Event triggering;
3. AWS CodeBuild execution;
4. LLM invocation through Bedrock;
5. Artifact persistence in S3.

The execution process is monitored through:
- logs;
- execution history;
- job states;
- execution metadata.

The core execution command is:

java -jar docgen-ai-tool.jar run

This command initiates the complete automated documentation reconstruction process.

---

## Insert image related to:
- AWS CodeBuild execution
- Active pipeline execution
- Build logs
- Execution monitoring

---

# 8. Monitoring and Execution Tracking

The system provides execution visibility through a monitoring interface.

Users can:
- view all jobs;
- monitor execution progress;
- inspect execution details;
- access logs;
- verify generated artifacts.

The monitoring layer avoids "black-box execution" scenarios and improves transparency during processing.

The system also exposes:
- Build IDs;
- input artifacts;
- timestamps;
- execution states.

---

## Insert image related to:
- All Jobs screen
- Job details screen
- Watch execution screen
- Execution progress

---

# 9. Generated Artifacts

The pipeline automatically generates multiple technical artifacts.

## Source-Code Documentation
- JavaDocs for classes and methods.

## High-Level Documentation
- README files;
- architecture documentation;
- API documentation.

## Analysis and Traceability Artifacts
- manifest.json;
- javadoc_report.json;
- execution reports;
- logs.

These artifacts support:
- onboarding;
- maintenance;
- code review;
- architectural understanding;
- auditing.

---

## Insert image related to:
- Generated JavaDocs
- Generated architecture document
- Generated API documentation
- Final reports

---

# 10. Technical Results

The pipeline demonstrated the feasibility of automated documentation reconstruction using LLMs in real enterprise systems.

The implementation enabled:
- contextualized JavaDoc generation;
- architectural documentation synthesis;
- preservation of source-code integrity;
- auditability;
- reproducibility;
- traceability.

The generated documentation also supported:
- code comprehension;
- onboarding activities;
- architectural understanding;
- code-review processes.

---

# 11. Technical Limitations

Although the pipeline demonstrated practical viability, some limitations were identified during implementation and experimentation.

These limitations include:
- context-window constraints;
- dependency on architectural context;
- hallucination risks;
- semantic inconsistencies;
- limitations in undocumented business rules;
- necessity of human validation.

The study also observed that documentation quality varies according to the architectural layer being analyzed.

---

# 12. Final Considerations

The proposed pipeline represents an automated infrastructure for technical documentation reconstruction in Java systems using Large Language Models integrated with AWS cloud services.

The architecture combines:
- static source-code analysis;
- cloud-native orchestration;
- AI-assisted generation;
- structured artifact synthesis.

Beyond operational automation, the pipeline also served as the central experimental infrastructure supporting the empirical evaluation conducted in this master's research.

The generated artifacts enabled the execution of real-world qualitative evaluation through Merge Requests and focus-group analysis, providing evidence regarding the usefulness, consistency, and practical applicability of AI-generated documentation in industrial software-maintenance scenarios.

---
