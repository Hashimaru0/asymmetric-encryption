# Asymmetric encryption

Script for symmetrically encrypting files using a key and asymmetrically encrypting that key to facilitate secure file sharing.



## Usage
Files inside toEncrypt folder get encrypted and placed inside encrypted folder.
```python
from cryptography.fernet import Fernet
import rsa

# Generate symmetric, public and private keys first
generateKeys()

# Use symmetric key to encrypt files
encryptFiles()

# Use symmetric key to decrypt those files
decryptFiles()
```
