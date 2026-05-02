# Caesar Cipher

A lightweight Python utility for encoding and decoding messages using the Caesar cipher algorithm.

## Overview

The Caesar cipher is a substitution cipher that shifts each letter in the plaintext by a fixed number of positions in the alphabet. This implementation supports both encryption and decryption with customizable shift values.

## Features

- **Encode messages** – Encrypt text with a specified shift value
- **Decode messages** – Decrypt previously encoded text
- **Character preservation** – Non-alphabetic characters remain unchanged
- **Case handling** – Automatically converts input to lowercase for consistent processing

## Usage

Run the program and follow the interactive prompts:

```bash
python caesar_cipher.py
```

**Input Requirements:**
1. **Direction:** Enter `encode` to encrypt or `decode` to decrypt
2. **Message:** Enter the text to process
3. **Shift:** Enter an integer representing the shift value (1-25)

**Example:**
```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
3
Encoded: khoor zruog
```

## How It Works

The cipher shifts each letter by N positions in the alphabet:
- `shift = 3`: A→D, B→E, C→F, ..., Z→C
- Non-alphabetic characters (spaces, numbers, punctuation) are preserved
- Wrapping occurs automatically (Z + 1 = A)

## Algorithm

```
Encoding:   new_index = (current_index + shift) % 26
Decoding:   new_index = (current_index - shift) % 26
```

## Requirements

- Python 3.x
- No external dependencies

## Limitations

- Only processes lowercase letters
- Single shift value for entire message
- No key management or advanced cryptographic features

## Security Note

Caesar cipher is for educational purposes only. It provides minimal security and should not be used for protecting sensitive information.