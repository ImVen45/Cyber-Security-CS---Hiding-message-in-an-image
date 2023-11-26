# Cyber-Security-CS---Hiding-message-in-an-image

The provided code defines functions for text encryption and decryption using image steganography. It utilizes least significant bit (LSB) modification to embed the message bits within the image's color values.

**Function Overview:**

1. `text_to_binary`: Converts a text message into its binary representation.

2. `binary_to_text`: Converts a binary string back into its corresponding text message.

3. `encrypt_message`: Encrypts a message by embedding its binary representation into an image's LSBs.

4. `decrypt_message`: Decrypts a message from an image by extracting the embedded binary representation and converting it back to text.

**Main Execution:**

1. Reads an image using OpenCV's `imread` function.

2. Enters a loop to handle encryption or decryption based on user input.

3. For encryption:
    - Prompts for the secret message and encryption password.
    - Encrypts the message using `encrypt_message` and saves the encrypted image.
    - Displays the encrypted image.

4. For decryption:
    - Prompts for the decryption password.
    - Decrypts the saved encrypted image using `decrypt_message` if the password matches.
    - Displays the decrypted message.

5. Exits the loop if the user chooses not to continue.
