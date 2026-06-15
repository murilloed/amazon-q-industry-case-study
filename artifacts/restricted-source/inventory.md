# Restricted Archive Inventory

## Input Archive

- Extracted files observed during audit: 601
- Java source files observed: 523
- Build system: Maven
- Application family: Java 11 / Spring Boot

The archive also contains environment and deployment configuration, database
scripts, authentication and integration code, documents, images, fonts, and
data-model concepts involving personal identifiers. Those categories are not
appropriate for unconditional public release.

## Output Archive

The output preserves the input tree and includes:

- a source copy with generated JavaDocs;
- `analysis/manifest.json`;
- `analysis/javadoc_report.json`;
- `analysis/docs_generation_report.json`;
- generated `README.md`;
- generated `ARCHITECTURE.md`; and
- attempted generated `API.md`.

The generated code copy changed 523 Java files relative to the input. Publishing
that output would disclose nearly the complete industrial source tree and is
therefore not a meaningful anonymization strategy.
