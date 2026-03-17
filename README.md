## Claude Security Auditor Skill

A professional-grade system prompt engineered to transform Claude into a **Principal Application Security Architect**. This tool is designed for deep-dive Static Application Security Testing (SAST) and manual code review emulation across enterprise-grade codebases.

---

### Capabilities

This configuration forces the AI to utilize industry-standard methodologies to analyze any code provided, regardless of language or framework:
* **Source-to-Sink Taint Analysis**: Traces untrusted user inputs to sensitive execution sinks to identify weaponizable paths.
* **CVSS v3.1 Scoring**: Generates standardized vulnerability vectors for immediate integration into risk management platforms.
* **CWE Identification**: Maps every finding to the Common Weakness Enumeration database for compliance tracking.
* **Logical Scratchpad**: Utilizes Chain-of-Thought reasoning to reduce false positives by analyzing trust boundaries before reporting.

---

### Analysis Scope

The auditor identifies a wide spectrum of critical vulnerabilities:
* **Injection**: SQL, NoSQL, OS Command, and LDAP Injection.
* **Broken Access Control**: BOLA/IDOR and missing function-level authorization.
* **Cryptographic Failures**: Weak entropy, deprecated algorithms, and hardcoded secrets.
* **Memory/Logic Errors**: Race conditions, insecure deserialization, and Remote Code Execution (RCE).

---

### How to Use

1. **Download**: Download the ZIP file of this repository.
2. **Go to Claude**: Visit the [Claude.ai](https://claude.ai) website.
3. **Customize**: Open the sidebar and go to **Customize**.
4. **Skills**: Navigate to the **Skills** section.
5. **Upload**: Click the **plus (+)** icon to upload a skill, then drag and drop the ZIP file.
6. **Enjoy**: Save it and start auditing! Enjoy!

---

### Output Schema

The tool returns a machine-readable JSON object containing:
* **Analytical Scratchpad**: The step-by-step reasoning process of the auditor.
* **Audit Metadata**: Executive summary and severity distribution.
* **Findings**: Detailed technical descriptions, line numbers, attack mechanics, and remediation code.

---

### Project Structure

- `system_prompt.txt`: The core system prompt for Claude.
- `examples/`: Directory containing test cases and sample reports.
  - `vulnerable_example.py`: A sample Python file with intentional security flaws.
  - `example_report.json`: An example of the JSON report Claude generates.
- `LICENSE`: MIT License.
- `CONTRIBUTING.md`: Guidelines for contributors.

---

### Examples

To see the tool in action without pasting your own code, you can use the files in the `examples/` directory.

1.  Copy the content of `system_prompt.txt`.
2.  Start a new Claude chat.
3.  Paste the prompt, replacing `{code_snippet}` with the content of `examples/vulnerable_example.py`.
4.  Compare the output with `examples/example_report.json`.

---

### License

Distributed under the MIT License.