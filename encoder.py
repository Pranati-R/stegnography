import cv2
import os

def encode_message(image_path, message, password):
    img = cv2.imread(image_path)

    d = {chr(i): i for i in range(256)}
    
    m, n, z = 0, 0, 0
    for i in range(len(message)):
        img[n, m, z] = d[message[i]]
        n = n + 1
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    cv2.imwrite("encryptedImage.jpg", img)
    print("Message encoded and saved as 'encryptedImage.jpg'")

if __name__ == "__main__":
    image_path = input("Enter image path: ")
    message = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    encode_message(image_path, message, password)