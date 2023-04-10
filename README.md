## _**What is Hybrid Cryptography?**_

Hybrid cryptography is a mode of encryption that merges two or more encryption systems.
It incorporates a combination of asymmetric and symmetric encryption to derive benefits from the strengths of each. 
The approach takes advantage of public-key cryptography for sharing keys and the speed of the symmetric encryption for encrypting messages. 
A hybrid encryption scheme combines the ease of use of an asymmetric encryption scheme with the effectiveness of a symmetric encryption technique.
To encrypt a message first generate a symmetric key and then encrypt the data. Then the person to whom we wish to send the message will share her public key and keep the private key a secret. 
After this, encrypt the symmetric key using the public key of the receiver and send the encrypted symmetric key to the receiver.
To decrypt a message the receiver decrypts the encrypted symmetric key using her private key and gets the symmetric key needed for decryption and then the receiver uses the decrypted symmetric key to decrypt the message.

## _**What is Multiple Encryption?**_

Multiple encryption is the process of encrypting an already encrypted message one or more times, either using the same or a different algorithm. 
The terms cascade encryption, cascade ciphering, multiple encryption, multiple ciphering, double strength encryption, multiphase encryption, and superencipherment are used with the same meaning.

## _**Hybrid-Multiple Cryptography - version 1:**_

This Hybrid-Multiple Cryptosystem will implement both the multiple and hybrid cryptosystems as one system. 
This system will double the data security and your privacy is also maintained at the best level. 
This Cryptosystem will provide data encryption multiple times by using multiple and hybrid cryptosystem with each step being encrypted with a different algorithm along with randomization. 
At first, the keys are generated for both the AES and RSA algorithms. 
The connection is established between the sender and receiver. 
The sender encrypts the message first using AES public key and then encrypted using RSA public key. 
As a result, we will get a ciphertext-2. Then the AES public key is encrypted using the RSA public key. 
After that, the ciphertext-2 and encrypted AES key is sent to the receiver through the medium i.e., the internet. 
The receiver already has the RSA private key when the connection is made. 
With that key, the receiver decrypts the encrypted AES key and ciphertext-2. 
As a result, we will a ciphertext-1 and AES key. Using the AES key, the ciphertext-1 is decrypted. 
Finally, we got the message without any losses.

## _**Hybrid-multiple Cryptography Version 2:**_

This scheme implements an approach that seeks to incorporate both Hybrid cryptography and Multiple cryptography as a way to provide an enhanced layer of security by combining both of their strengths while also mitigating the drawbacks that are present in each individual approach. The process begins with the creation of a symmetric key as well as an asymmetric key pair consisting of a public and a private key. Initially, the message is encrypted using the symmetric key encryption technique with the symmetric key that can encrypt the message for n number of times. The resulting encrypted text and symmetric key are encrypted with the asymmetric public key using the asymmetric key encryption algorithm. The decryption process, on the other hand, is a reversal of the encryption process.Thus the scheme is a reliable and effective data encryption system that can offer greater data protection than conventional encryption approaches.

## _**Pseudocode for Version 2:**_
![HMC pseudocode](https://user-images.githubusercontent.com/91528427/230816572-89e90ea2-40e0-447c-9c27-b604f0b77eae.jpg)

## _**Architecture Diagram for Version 2:**_
![Architecture V2](https://user-images.githubusercontent.com/91528427/230817229-38593611-995f-4d76-ba3d-306ace99a2b2.jpg)


