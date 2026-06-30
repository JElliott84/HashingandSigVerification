#Module 3 Assignment: Hashing, Encryption, and Digital Signatures
#Jason Elliott
#In this assignment, we took the assignment from Module 2 and added the ability to create a digital signature and verify it. 
# The user can now choose to encrypt, decrypt, hash, sign, or verify a message.

#In order to use this correctly, we had to modify the menu to make it somewhat more user friendly. We also had to add the ability to create a digital signature and verify it.

#To start, we imported the hashlib and OS modules in order to use SHA and also create documents for signatures. 
import hashlib
import os

# We then created a menu that allows the user to choose between encrypting, decrypting, hashing, signing, or verifying a message.
choice = input("Encrypt (e), Decrypt (d), Hash (h), Signature (s), or Verify (v): ").lower()

key = 2
result = ""

# Here is the new logic that we use for the program. The first line is to verify any signature that has been created. 
#If no file exist, it will approve. However we want to create a signature from the menu above first. 
if choice == "v":
    os.system("openssl enc -base64 -d -in signature.txt -out signature.bin")
    os.system("openssl dgst -sha256 -verify public_key.pem -signature signature.bin document.txt")

# This is the remaining of the logic for our program.
else:
    userMessage = input("Enter a message: ")

# Encryption with Caesar Cipher
    if choice == "e":
        for char in userMessage:
            result += chr(ord(char) + key)
        print("Encrypted Message:", result)

# Decryption with Caesar Cipher
    elif choice == "d":
        for char in userMessage:
            result += chr(ord(char) - key)
        print("Decrypted Message:", result)

# Hashing with SHA-256
    elif choice == "h":
        hashMessage = hashlib.sha256(userMessage.encode()).hexdigest()
        print("SHA-256 Hash:", hashMessage)

# Digital Signature Creation. This uses the OpenSSL command line tool to generate a private key, public key, and create a digital signature for the message.
    elif choice == "s":
        with open("document.txt", "w") as file:
            file.write(userMessage)

        os.system("openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out private_key.pem")
        os.system("openssl rsa -pubout -in private_key.pem -out public_key.pem")
        os.system("openssl dgst -sha256 -sign private_key.pem -out signature.bin document.txt")
        os.system("openssl enc -base64 -in signature.bin -out signature.txt")

        print("Digital signature created successfully.")
        print("Files created: document.txt, private_key.pem, public_key.pem, signature.bin, signature.txt")

    else:
        print("Invalid choice, select again or exit the program.")
