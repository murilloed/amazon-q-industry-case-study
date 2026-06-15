# Expected Structural Outcome

Exact prose is nondeterministic. A successful run should:

- discover two public classes;
- discover their public constructor and methods;
- create a manifest with stable source locations;
- produce a JavaDoc report;
- preserve compilable Java syntax after insertion; and
- keep generated artifacts separate from the original input.

Review generated text for unsupported business assumptions. For example, the
model must not invent payment rules, customer attributes, endpoints, or
exceptions absent from the sample.
