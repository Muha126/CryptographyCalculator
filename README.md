<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/cryptography-calculator">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Cryptography Calculator</h3>

  <p align="center">
    A calculator with a hidden asymmetric encryption engine. Secure and stealthy.
    <br />
    <a href="https://github.com/github_username/cryptography-calculator"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/cryptography-calculator">View Demo</a>
    ·
    <a href="https://github.com/github_username/cryptography-calculator/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/cryptography-calculator/issues">Request Feature</a>
  </p>
</div>

---

## 📌 About The Project

Cryptography Calculator looks like a regular math calculator... until you enter the secret code.

Once triggered, it allows you to:
- Input sensitive text
- Asymmetrically encrypt it (using RSA 2048)
- Store the encrypted data in an SQLite database
- Write the private key to a connected USB drive
- Later decrypt the data by inserting the USB with the key file

If encrypted data exists in the database, it prompts for a key to decrypt and display it, with options to delete or close.

> Use it to hide sensitive notes, passwords, or secrets on shared computers without raising suspicion.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## ⚙️ Built With

* [PyQt6](https://pypi.org/project/PyQt6/) - GUI framework
* [cryptography](https://cryptography.io/en/latest/) - for RSA encryption
* [sqlite3](https://docs.python.org/3/library/sqlite3.html) - for storing encrypted data
* [wmi](https://pypi.org/project/WMI/) - for detecting USB drives (Windows only)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🧪 Getting Started

To get a local copy up and running follow these simple steps.

### ✅ Prerequisites

* Python 3.11+
* pip (Python package manager)

Install dependencies:

```bash
pip install -r requirements.txt
