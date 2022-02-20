# Asymmetric encryption

Script for symmetrically encrypting files and encrypting that key asymmetrically to facilitate secure file sharing.



## Usage
Files inside toEncrypt folder get encrypted using symmetric encryption and placed inside encrypted folder.
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