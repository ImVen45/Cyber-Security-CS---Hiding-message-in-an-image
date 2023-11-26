import cv2
import numpy as np

# Function to convert text message to binary
def text_to_binary(msg):
    binary_msg = ''.join(format(ord(char), '08b') for char in msg)
    return binary_msg

# Function to convert binary message to text
def binary_to_text(binary_msg):
    text_msg = ''.join(chr(int(binary_msg[i:i+8], 2)) for i in range(0, len(binary_msg), 8))
    return text_msg

# Function to encrypt a message into an image
def encrypt_message(img, msg):
    binary_msg = text_to_binary(msg)
    n, m, c = 0, 0, 0

    for i in range(len(binary_msg)):
        img[n, m, c] = int(binary_msg[i])
        n += 1
        m += 1
        c = (c + 1) % 3

    return img

# Function to decrypt a message from an image
def decrypt_message(img, password):
    binary_msg = ''
    n, m, c = 0, 0, 0

    for i in range(len(msg) * 8):  # Multiply by 8 to account for the bits in each character
        binary_msg += str(img[n, m, c])
        n += 1
        m += 1
        c = (c + 1) % 3

    decrypted_msg = binary_to_text(binary_msg)
    return decrypted_msg


if __name__ == "__main__":

    # Read the original image
    img = cv2.imread("Offer_Letter.jpg")

    while True:
        # Ask the user to choose an operation
        choice = input("Choose operation (encrypt/decrypt): ")

        if choice == "encrypt":
            # Get the message to be encrypted from the user
            msg = input("Enter Secret Message:")
            password = input("Enter Password for Encryption:")

            # Encryption
            encrypted_img = encrypt_message(np.copy(img), msg)
            cv2.imwrite("EncryptedMessage.jpg", encrypted_img)
            cv2.imshow("Encrypted Message", encrypted_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif choice == "decrypt":
            # Check if an image has been encrypted before attempting decryption
            decrypt_password = input("Enter Password for Decryption:")

            if decrypt_password == password:
                # Get the password for decryption (in this case, the password is the length of the original message)
                decrypted_msg = decrypt_message(encrypted_img, password)
                print("Decrypted Message:", decrypted_msg)
            else:
                print("Invalid Decryption Password")

        else:
            print("Invalid Choice. Please enter 'encrypt' or 'decrypt'.")

        # Ask the user if they want to continue
        if input("Continue (y/n): ") != "y":
            break
