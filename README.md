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
Run from gui.py
## Usage

Cryptography Calculator has two modes:  
A regular calculator mode  
A hidden encryption mode (triggered by a secret code)

---

### Secret Mode Walkthrough

#### 1. Start the application

```bash
python gui.py
You’ll see a simple calculator interface.

<p align="center"> <img src="https://via.placeholder.com/400x200.png?text=Calculator+GUI" alt="Calculator GUI" /> </p>
2. Enter the secret code
Type:

yaml
Copy
Edit
1337*1337
and press =.

This will unlock the encryption panel.

<p align="center"> <img src="https://via.placeholder.com/400x200.png?text=Secret+Code+Entered" alt="Secret Trigger Example" /> </p>
3. If no encrypted data is found in the database
You’ll be prompted to insert a USB drive

Enter the text you want to encrypt

Select the USB drive from the dropdown list

Click the Encrypt and Write button

What happens:

The text is encrypted using RSA 2048

The private key is saved to your USB as private_key.pem

The encrypted message is stored in an SQLite database

<p align="center"> <img src="https://via.placeholder.com/400x200.png?text=Encryption+Panel" alt="Encryption Panel" /> </p>
4. If encrypted data already exists
You’ll see a prompt asking you to decrypt:

Insert the USB with the private_key.pem file

Select the key file when prompted

The application will decrypt the message if the key matches

You now have two options:

Close – to hide the decrypted message

Delete – to remove the encrypted data from the database

<p align="center"> <img src="https://via.placeholder.com/400x200.png?text=Decrypted+Message+UI" alt="Decryption UI" /> </p>
Notes
Encryption is only available when no encrypted data exists.

Decryption is only triggered when encrypted data is present.

All encryption keys are unique per session and stored only on the USB drive.

If the USB with the private key is lost, the data cannot be recovered.
```
