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

### Integration Instructions

#### Option 1: Claude Projects (Enterprise/Pro)
1. Create a new **Project** in Claude.ai named "Security Auditor Core".
2. Open `system_prompt.txt` from this repository and copy the full text.
3. Paste into the **Custom Instructions** section of the Project.
4. Save the project. Any code uploaded will be automatically analyzed according to the structured JSON format.

#### Option 2: Pre-prompting in a Chat
1. Open `system_prompt.txt` and copy the contents.
2. Start a new chat session in Claude.
3. Paste the prompt and replace `{code_snippet}` with the target code.
4. The output is **strictly JSON**, making it ready for parsing by internal security dashboards or automated triaging scripts.

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