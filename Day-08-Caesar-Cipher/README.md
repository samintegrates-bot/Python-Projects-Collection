# Caesar Cipher 🛡️

A lightweight Python utility for encoding and decoding messages using the Caesar cipher algorithm. This project is part of the **100 Days of Code: The Complete Python Pro Bootcamp**.

## 📖 Overview

The Caesar cipher is a substitution cipher that shifts each letter in the plaintext by a fixed number of positions in the alphabet. This implementation supports both encryption and decryption with customizable shift values.

## ✨ Features

- **Encode messages** – Encrypt text with a specified shift value.
- **Decode messages** – Decrypt previously encoded text.
- **Character preservation** – Non-alphabetic characters (spaces, numbers, symbols) remain unchanged.
- **Case handling** – Automatically converts input to lowercase for consistent processing.
- **Flexible Shifts** – Supports any integer as a shift value (including values > 26).

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### Running the Program

1. Navigate to the project directory:
   ```bash
   cd Day-08-Caesar-Cipher
   ```
2. Run the script:
   ```bash
   python caesar_cipher.py
   ```

## 🛠️ Usage

Follow the interactive prompts:

1. **Direction:** Enter `encode` to encrypt or `decode` to decrypt.
2. **Message:** Enter the text you want to process.
3. **Shift:** Enter an integer representing the shift value.

### Example

```text
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world!
Type the shift number:
3
Encoded: khoor zruog!
```

## 🧠 How It Works

The cipher shifts each letter by N positions in the alphabet:
- `shift = 3`: A→D, B→E, C→F, ..., Z→C
- Non-alphabetic characters are preserved.
- The modulo operator (`% 26`) is used to handle shifts larger than the alphabet length and to wrap around from Z to A.

### Algorithm

```python
Encoding: new_index = (current_index + shift) % 26
Decoding: new_index = (current_index - shift) % 26
```

## 💡 Tips & Troubleshooting

- **Large Shifts:** You can enter any number as a shift (e.g., 5000). The program will automatically calculate the effective shift using `shift % 26`.
- **Lowercase Only:** The current implementation converts all input to lowercase. Uppercase letters in the input will be processed as their lowercase equivalents.

## ⚠️ Security Note

The Caesar cipher is for **educational purposes only**. It provides minimal security and can be easily broken with frequency analysis or brute-force attacks. Do not use it to protect sensitive information.
