def encrypt(message, key):
    encrypted_message = ""
    key = key * (len(message) // len(key)) + key[:len(message) % len(key)]
    for i in range(len(message)):
        encrypted_char = chr(ord(message[i]) ^ ord(key[i]))
        encrypted_message += encrypted_char
    return encrypted_message

def decrypt(encrypted_message, key):
    decrypted_message = ""
    key = key * (len(encrypted_message) // len(key)) + key[:len(encrypted_message) % len(key)]
    for i in range(len(encrypted_message)):
        decrypted_char = chr(ord(encrypted_message[i]) ^ ord(key[i]))
        decrypted_message += decrypted_char
    return decrypted_message

message = "|OP`Z<E]|Y\$"
key = "Jai Shree Ram!"

decrypted_message = decrypt(message, key)
print("Decrypted message:", decrypted_message)