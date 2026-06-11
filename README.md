\# File Encryptor CLI



A lightweight command-line file encryption tool using modern cryptography.

Install dependencies: 

pip install cryptography argon2-cffi 

pip install requirements.txt



\## Features

\- AES-256-GCM authenticated encryption

\- Argon2id password-based key derivation

\- Secure random salt and nonce

\- Integrity protection (detects tampering)



\## Security design

\- AES-GCM ensures confidentiality + integrity

\- Argon2id protects against brute-force attacks

\- Each file uses a unique salt and nonce



\## Usage



Encrypt a file:

```bash

python cli.py encrypt input.txt output.enc mypassword```

Decrypt a file:
```bash

python cli.py decrypt input.txt output.enc mypassword```

After successful encryption, you may safely remove the original file manually:

```bash
rm input.txt```


