# File-Encryption-Tool
A lightweight and secure Python-based utility to encrypt and decrypt files using AES-256 in CBC mode. Ideal for protecting confidential data during storage or transmission.

# Features

- ✅ AES-256 encryption and decryption
- ✅ CBC mode with secure IV handling
- ✅ Random key generation and safe storage
- ✅ Automatic padding for any file size
- ✅ Simple command-line interface

# Use Cases

- Securely storing personal documents
- Sending sensitive files over insecure channels
- Basic educational demonstration of AES encryption

# Installation

### 1. Clone the Repository
git clone https://github.com/14stella/File-Encryption-Tool.git
cd file-encryption-tool
### 2. Set Up a Virtual Environment 
python3 -m venv venv
source venv/bin/activate
### 3. Install Dependencies
pip install -r requirements.txt
Or manually:
pip install pycryptodome

# Usage
🔒 Encrypt a file
python filecrypt.py encrypt <filename>
Example:
python filecrypt.py encrypt notes.txt
Output: notes.txt.enc

🔓 Decrypt a file
python filecrypt.py decrypt <encrypted_filename>`
Example:
python filecrypt.py decrypt notes.txt.enc
Output: notes.txt.dec
