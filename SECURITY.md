# Security Policy

Do not open a public issue containing credentials, tokens, internal endpoints,
personal data, or excerpts from the restricted industrial archives.

Before publishing a new artifact:

1. run `python scripts/verify_public_release.py .`;
2. inspect every reported finding manually;
3. confirm redistribution authorization;
4. remove raw logs and environment-specific configuration; and
5. verify that participant evidence is anonymized and consented for release.

Potential disclosures should be reported privately to the repository owner.
