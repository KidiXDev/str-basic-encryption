# String Basic Encryption
Python simple library to encrypt strings with MD5, SHA256 and SHA512 hashes

## Installation
```shell
pip install str-basic-encryption
```

## Usage
Basic Usage:
```python
from str_basic_encryption import StrEncryption

encryptor = StrEncryption()

some_text = "Hello World!"
result = encryptor.str2md5(some_text)
print(f"Encrypted String: {result}")
```