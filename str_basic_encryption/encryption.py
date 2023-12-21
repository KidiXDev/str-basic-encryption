import hashlib

class StrEncryption:
    def str2md5(self, input_string):
        """
        Convert a string to its MD5 hash.

        Args:
            input_string (str): The string to be hashed.

        Returns:
            str: The MD5 hash of the string.
        """
        md5_hash = hashlib.md5()
        md5_hash.update(input_string.encode('utf-8'))
        hashed_string = md5_hash.hexdigest()

        return hashed_string

    def str2sha256(input_string):
        """
        Convert a string to its SHA256 hash.

        Args:
            input_string (str): The input string to be hashed.

        Returns:
            str: The SHA256 hash of the input string.
        """
        sha256 = hashlib.sha256()
        sha256.update(input_string.encode('utf-8'))
        encrypted_string = sha256.hexdigest()

        return encrypted_string
        
    def str2sha512(input_string):
        """
        Generates a SHA-512 hash from a given input string.

        Parameters:
            input_string (str): The input string to be hashed.

        Returns:
            str: The SHA-512 hash of the input string.
        """
        sha512 = hashlib.sha512()
        sha512.update(input_string.encode('utf-8'))
        encrypted_string = sha512.hexdigest()
        
        return encrypted_string
    