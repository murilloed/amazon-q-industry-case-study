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

## Automated Documentation Reconstruction Pipeline:

<img width="1536" height="1024" alt="pipeline aws" src="https://github.com/user-attachments/assets/f5ed9816-8b10-447b-8138-65ac102c654d" />

- High-level pipeline overview
- General AWS architecture
- Macro execution flow

The figure above presents a high-level overview of the automated documentation reconstruction pipeline proposed in this research. The architecture integrates AWS cloud services, static source-code analysis techniques, and Large Language Models (LLMs) to automatically generate contextualized technical documentation for Java systems. The execution flow begins with the upload of a Java project through a web interface, followed by artifact storage in Amazon S3 and orchestration through AWS CodeBuild. During execution, the pipeline performs structural analysis using JavaParser and AST extraction mechanisms, generating metadata representations through the ManifestGenerator component. Subsequently, the JavadocInjector and DocsGenerator components invoke Amazon Bedrock and Amazon Q to synthesize JavaDocs, architectural documentation, API documentation, and auxiliary technical artifacts. Finally, the generated outputs are organized, persisted, and made available for monitoring and download, ensuring traceability, auditability, reproducibility, and support for software maintenance and architectural comprehension activities.

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

## Full AWS pipeline architecture:
- Full AWS pipeline architecture
- Component communication flow
- Infrastructure overview

<img width="1536" height="1024" alt="Full AWS pipeline architecture" src="https://github.com/user-attachments/assets/00bb4f58-74b8-41e7-a459-a108d9becb88" />


The figure above presents the complete AWS-based architecture of the automated documentation reconstruction pipeline proposed in this research. The infrastructure integrates cloud-native orchestration services, static source-code analysis components, and Large Language Model (LLM) providers to enable the automated generation of contextualized technical documentation for Java systems. The execution flow starts with the upload of a Java project through a web interface, followed by storage and event triggering in Amazon S3. AWS CodeBuild orchestrates the execution lifecycle of the pipeline, coordinating multiple internal components responsible for structural analysis, metadata extraction, JavaDoc generation, architectural reconstruction, and high-level documentation synthesis. During execution, JavaParser performs AST-based source-code parsing, while the ManifestGenerator, JavadocInjector, and DocsGenerator components interact with Amazon Bedrock and Amazon Q to generate contextualized documentation artifacts. The resulting outputs are then organized into standardized structures and persisted in Amazon S3 for monitoring, auditing, download, and integration with external tools. The architecture also incorporates supporting services related to security, observability, traceability, and operational monitoring, including AWS IAM, KMS, CloudWatch, CloudTrail, and AWS X-Ray.



---

# 4. Pipeline Construction Process

The construction of the pipeline involved the integration of static code analysis techniques, AWS cloud services, and LLM-based generation strategies.

<img width="945" height="529" alt="image" src="https://github.com/user-attachments/assets/211e463b-43ae-4848-b78a-612a87a5309b" />

The figure above presents the implementation environment of the proposed pipeline, including the project structure, execution flow, and generated documentation preview. The image illustrates the integration between the documentation generation tool, the execution workflow, and the generated technical artifacts produced through the automated pipeline.

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
- Technology stack
- AWS service interaction
- Tool integration architecture

---

# 6. Execution Flow

The operational flow of the pipeline begins when a Java project is uploaded through the web interface.

The uploaded ZIP artifact is stored in Amazon S3 and associated with a unique Job ID responsible for tracking the execution lifecycle.

---

# 6.1 Initial Upload

The upload interface allows users to submit real Java systems for automated analysis.

<img width="945" height="506" alt="image" src="https://github.com/user-attachments/assets/5f036f98-3285-442c-b1a1-3dbad57dc15c" />

The figure above illustrates the initial upload interface of the automated documentation reconstruction pipeline. Through this interface, users can submit real Java projects in ZIP format, thereby initiating the execution lifecycle of the pipeline.

The upload process collects:
- project name;
- ZIP source-code package;
- execution metadata.

<img width="945" height="493" alt="image" src="https://github.com/user-attachments/assets/bdb07c94-76fc-4d3e-a786-d1ee7d5b02a9" />

The figure above presents the upload stage of the automated documentation reconstruction pipeline. The image illustrates the submission of a real Java project ZIP artifact during transfer to the AWS infrastructure.

At this stage:
- no analysis is performed yet;
- the job context is created;
- the artifact is prepared for execution.

<img width="945" height="460" alt="image" src="https://github.com/user-attachments/assets/638a422e-076c-4ec8-acf3-39de248f0a77" />

The figure above presents the formalization stage of the execution job after the upload process is completed.

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

The generation process preserves:
- formatting;
- source-code structure;
- syntactic consistency.

<img width="945" height="506" alt="image" src="https://github.com/user-attachments/assets/7c125466-8611-41df-9c19-2828c5a5025b" />

The figure above presents the operational execution environment of the JavaDoc generation phase.

<img width="945" height="506" alt="image" src="https://github.com/user-attachments/assets/527b4388-1e48-4b75-bdc6-22c76fca23f4" />

The figure above presents the JavaDoc generation process applied to the model layer of the analyzed Java project.

<img width="1536" height="1024" alt="examples of automatically generated javaDocs and Execution Report" src="https://github.com/user-attachments/assets/fd3ab4cc-5b41-44b9-b244-0ac2bc5ab521" />


The figure above presents an example of automatically generated JavaDocs injected directly into the analyzed Java source code.

The execution also produces `javadoc_report.json`, which records:
- modified files;
- generated documentation;
- execution results;
- possible failures.

The generated report includes:
- modified files;
- generated entries;
- failures;
- execution status;
- coverage information.

---

# 6.4 Documentation Generation — DocsGenerator

The pipeline also generates high-level documentation artifacts.

Using the previously extracted metadata and generated JavaDocs, the DocsGenerator component creates:
- README.md;
- ARCHITECTURE.md;
- API documentation;
- execution reports.

<img width="945" height="657" alt="image" src="https://github.com/user-attachments/assets/0afe5b55-f515-48ec-bfa3-f105c660d7f1" />

The figure above presents an example of automatically generated README documentation produced by the DocsGenerator component.

<img width="945" height="650" alt="image" src="https://github.com/user-attachments/assets/2f4c44ce-7d52-4def-8808-a45f7b109010" />

The figure above presents an example of automatically generated API documentation produced by the DocsGenerator component.

<img width="945" height="657" alt="image" src="https://github.com/user-attachments/assets/c49f26b9-340f-4aa5-a83b-e7291ce8b965" />

The figure above presents an example of automatically generated architectural documentation produced by the DocsGenerator component.

This stage enables documentation generation at multiple abstraction levels:
- micro level (methods/classes);
- macro level (architecture/system).

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
- Output directory structure
- Final artifact organization

---

# 7. AWS Infrastructure Execution

The pipeline execution is fully integrated with AWS infrastructure.

<img width="945" height="405" alt="image" src="https://github.com/user-attachments/assets/1897808f-28e9-4e39-bf9e-0e806c7d14d5" />

The figure above presents the AWS CodeBuild environment used to execute the automated documentation reconstruction pipeline.

The operational flow includes:
1. Upload to S3;
2. Event triggering;
3. AWS CodeBuild execution;
4. LLM invocation through Bedrock;
5. Artifact persistence in S3.

<img width="945" height="411" alt="image" src="https://github.com/user-attachments/assets/cee46cb3-d872-4586-a7e9-bd323efd18c5" />

The figure above presents the active execution state of the automated documentation reconstruction pipeline within AWS CodeBuild.

The execution process is monitored through:
- logs;
- execution history;
- job states;
- execution metadata.

<img width="945" height="416" alt="image" src="https://github.com/user-attachments/assets/1cd899a7-f698-41dc-aa64-055c8165fa9c" />

The figure above presents the runtime execution logs of the automated documentation reconstruction pipeline inside AWS CodeBuild.

The core execution command is:

```bash
java -jar docgen-ai-tool.jar run
```

This command initiates the complete automated documentation reconstruction process.

<img width="945" height="463" alt="image" src="https://github.com/user-attachments/assets/ad62ec85-efef-4987-b073-9de6bb4e37f0" />

FThe figure above presents the final execution stage of the automated documentation reconstruction pipeline inside AWS CodeBuild.

---

# 8. Monitoring and Execution Tracking

The system provides execution visibility through a monitoring interface.

Users can:
- view all jobs;
- monitor execution progress;
- inspect execution details;
- access logs;
- verify generated artifacts.

<img width="945" height="451" alt="image" src="https://github.com/user-attachments/assets/860867cc-a65c-478e-b424-94af80ba5884" />

The figure above presents the monitoring interface of the automated documentation reconstruction pipeline.

The monitoring layer avoids "black-box execution" scenarios and improves transparency during processing.

<img width="945" height="496" alt="image" src="https://github.com/user-attachments/assets/87b1c85e-7962-47c8-98cd-7ada971e862b" />

The figure above presents the real-time monitoring interface of the automated documentation reconstruction pipeline.

The system also exposes:
- Build IDs;
- input artifacts;
- timestamps;
- execution states.

<img width="945" height="456" alt="image" src="https://github.com/user-attachments/assets/036f4618-38ea-442e-a29f-6083d71f3317" />

The figure above presents the detailed execution status interface of the automated documentation reconstruction pipeline.

<img width="945" height="631" alt="image" src="https://github.com/user-attachments/assets/ee75b644-4a17-4b19-ada0-5dc020c76319" />

The figure above presents the expanded execution details view of the automated documentation reconstruction pipeline.

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

<img width="945" height="506" alt="image" src="https://github.com/user-attachments/assets/f9a07a68-67b5-4f78-be9b-15d602e5b3a4" />

The figure above presents the artifact packaging stage of the automated documentation reconstruction pipeline.

These artifacts support:
- onboarding;
- maintenance;
- code review;
- architectural understanding;
- auditing.

<img width="945" height="505" alt="image" src="https://github.com/user-attachments/assets/0420a361-3e1c-4ffc-a466-e0b6f1906d8a" />

The figure above presents the final artifact delivery interface of the automated documentation reconstruction pipeline.

<img width="945" height="653" alt="image" src="https://github.com/user-attachments/assets/782c92a5-6ee3-460c-8fb1-48fa2a26d93b" />

The figure above presents the final completion stage of the automated documentation reconstruction pipeline.

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
