In this assignment, we took the assignment from Module 2 and added the ability to create a digital signature and verify it. 
The user can now choose to encrypt, decrypt, hash, sign, or verify a message.

In order to use this correctly, we had to modify the menu to make it somewhat more user friendly. We also had to add the ability to create a digital signature and verify it.

To explain what and why we use Hashes and the OpenSSL, it comes down to protections and cryptography. 

The SHA-256 expansion in this application allows the user to take a passwork or a line of text a encrypt it into SHA-256 and give them an outcome. this makes decrypting passwords that much harder. 

The second part ofthe applicaiton that is new is the Signature Creation and Verification. We are now abel to create a document in the app, have the OpenSSL commands encrypt it to 2048 bits like what we learned
in the reading, and then generate public and private keys from the outcome. With verification, we can then check the document through the same app to see if it is verified and okay, or if the information has been tampered with. 

A video to show this is attached in the Githup Repo for the assignment. 

This allows the usersto not only protect their own information but also when moving information, they will know that nothing was altered in the communication or transfer of data (meaning it was not tampered with, and nobody
was able to take it and attempt to steal it with the amount of bits). The brute force attack that would be nessecary to do this would be a long process for someone to accomplish. 
