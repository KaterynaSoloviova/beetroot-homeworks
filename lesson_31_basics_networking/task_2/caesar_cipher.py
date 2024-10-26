def caesar_encrypt(text: str, key: int) -> str:
    cipher_text = ""
    for char in text:
        if char.isalpha():
            shift = ord(char) + key
            if char.isupper():
                if shift > ord('Z'):
                    shift -= 26
                cipher_text += chr(shift)
            else:
                if shift > ord('z'):
                    shift -= 26
                cipher_text += chr(shift)
        else:
            cipher_text += char
    return cipher_text


def caesar_decrypt(cipher_text: str, key: int) -> str:
    text = ""
    for char in cipher_text:
        if char.isalpha():
            shift = ord(char) - key
            if char.isupper():
                if shift < ord('A'):
                    shift += 26
                text += chr(shift)
            else:
                if shift < ord('a'):
                    shift += 26
                text += chr(shift)
        else:
            text += char
    return text
