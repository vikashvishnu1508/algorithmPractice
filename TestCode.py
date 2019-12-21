def caesarCipherEncryptor(string, key):
    # Write your code here.
    return ''.join([chr(ord(ch) + key) if (ord(ch) + key) <= 122 else chr(96 + ord(ch) + key - 122) for ch in string])

print(caesarCipherEncryptor('xyz', 26))