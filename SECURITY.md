# Security Policy

## 🛡️ Our Commitment
The ATAP project is a **children’s educational tool** and we take safety
extremely seriously. While the application is purely offline and does not
transmit any data, we still aim to follow secure development practices.

## Reporting a Vulnerability

If you discover a security vulnerability within ATAP, please **do not** open a
public issue. Instead, send an email to:

**security-atap@example.com**

We will respond within 48 hours and work with you to assess and fix the issue.
We request that you keep the vulnerability confidential until we have released a
patch.

## Scope
Security concerns relevant to ATAP include, but are not limited to:
- **File handling**: Project save/load must not be exploitable (e.g., path traversal).
- **Code execution**: No usage of `eval()` or unsafe deserialization (we only load JSON and PNG images).
- **Dependency vulnerabilities**: We monitor our dependencies (PyQt5, Pillow, imageio) for known CVEs.
- **Child safety**: No network access, no in‑app purchases, no advertising.

## Best Practices We Follow
- All file operations use `os.path` to avoid path traversal.
- We use JSON (not pickle) for project metadata.
- The app never connects to the internet.
- Dependencies are pinned in `requirements.txt` with minimum versions.

## Supported Versions
Currently, only the latest version (`main` branch) is supported.  
Please make sure you are using an up‑to‑date copy.

---

**Thank you for helping keep ATAP safe for little artists! 🧒🔒**