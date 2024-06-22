def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    choice = int(input("enter the following number of your operation \n1.Encryption  \n2.Decryption \nchoice no : "))
    
if choice == 1:
 plaintext = input("\nENCRYPTION\nEnter your message: ")
 shift = int(input("enter shift value : "))
 ciphertext = encrypt(plaintext, shift)
 print(f"Encrypted Message: {ciphertext}")
     
elif choice==2:
 ciphertext = input("\nDECRYPTION\nenter your encrypted message : ")
 shift = int(input("enter shift value : "))
 plaintext = decrypt(ciphertext, shift)
 print(f"Decrypted Message: {plaintext}")

else :
 print(f"enter a valid choice")
