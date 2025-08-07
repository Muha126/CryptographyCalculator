##  Getting Started

To get a local copy up and running, follow these simple steps.

###  Prerequisites

- Python 3.11+
- pip (Python package manager)

###  Install dependencies

```bash
pip install -r requirements.txt
```

###  Run the app

```bash
python gui.py
```

---

##  Usage

Cryptography Calculator has two modes:

- A regular calculator mode  
- A hidden encryption mode (triggered by a secret code)

---

##  Secret Mode Walkthrough

### 1. Start the application

```bash
python gui.py
```

You’ll see a simple calculator interface.

<p align="center">
  <img src="https://i.imgur.com/4zQ6UUu.png" alt="Calculator GUI" width="400" />
</p>

---

### 2. Enter the secret code

Type:

```
1337*1337
```

and press `=`. This will unlock the encryption panel.

<p align="center">
  <img src="https://i.imgur.com/4ixwZa0.png" alt="Secret Trigger Example" width="400" />
</p>

---

### 3. If no encrypted data is found

You’ll be prompted to insert a USB drive.

- Enter the text you want to encrypt
- Select the USB drive from the dropdown
- Click **Encrypt and Write**

What happens:

- The text is encrypted using RSA 2048
- Private key is saved to USB as `private_key.pem`
- Encrypted message stored in SQLite database

<p align="center">
  <img src="https://i.imgur.com/ChbkFaS.png" alt="Encryption Panel" width="400" />
</p>

---

### 4. If encrypted data already exists

You’ll see a prompt asking you to decrypt.

- Insert the USB with `private_key.pem`
- Select the key file when prompted
- The app will decrypt the message if the key matches

Then you can:

- **Close** – to hide the decrypted message
- **Delete** – to remove the encrypted data

<p align="center">
  <img src="https://i.imgur.com/p7CIvyT.pngI" alt="Decryption UI" width="400" />
</p>

---

##  Notes

- Encryption is only available if no encrypted data exists.
- Decryption is only triggered when encrypted data is present.
- Keys are unique per session and stored only on the USB.
- If the USB is lost, the data **cannot be recovered**.
