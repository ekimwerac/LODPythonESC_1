def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext


def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


def main():
    while True:
        choice = input("Enter 'E' for encryption or 'D' for decryption (or 'Q' to quit): ")
        if choice.upper() == 'Q':
            break

        text = input("Enter the text: ")
        shift = int(input("Enter the shift value: "))

        if choice.upper() == 'E':
            encrypted_text = caesar_encrypt(text, shift)
            print("Encrypted text:", encrypted_text)
        elif choice.upper() == 'D':
            decrypted_text = caesar_decrypt(text, shift)
            print("Decrypted text:", decrypted_text)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
