import os
import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

KEY_FILE = "key.bin"

def generate_key():
    key = get_random_bytes(32)  # AES-256
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

def load_key():
    if not os.path.exists(KEY_FILE):
        return generate_key()
    with open(KEY_FILE, "rb") as f:
        return f.read()

def encrypt_file(filename):
    key = load_key()
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(filename, "rb") as f:
        data = f.read()

    ciphertext = cipher.encrypt(pad(data, AES.block_size))

    with open(filename + ".enc", "wb") as f:
        f.write(iv + ciphertext)

    print(f"[+] Encrypted file saved as {filename}.enc")

def decrypt_file(filename):
    key = load_key()

    with open(filename, "rb") as f:
        iv = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    output_filename = filename.replace(".enc", ".dec")
    with open(output_filename, "wb") as f:
        f.write(plaintext)

    print(f"[+] Decrypted file saved as {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python filecrypt.py <encrypt|decrypt> <filename>")
        sys.exit(1)

    command = sys.argv[1].lower()
    file = sys.argv[2]

    if command == "encrypt":
        encrypt_file(file)
    elif command == "decrypt":
        decrypt_file(file)
    else:
        print("Invalid command. Use 'encrypt' or 'decrypt'.")

