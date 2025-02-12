import cv2#library

def decode_message(image_path, password, correct_password):
    if password != correct_password:
        print("YOU ARE NOT AUTHORIZED")
        return
    
    img = cv2.imread(image_path)
    
    c = {i: chr(i) for i in range(256)}

    message = ""
    m, n, z = 0, 0, 0
    for _ in range(len(img)):
        try:
            message += c[img[n, m, z]]
        except KeyError:
            break
        n += 1
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    print("Decryption message:", message)

if __name__ == "__main__":
    image_path = input("Enter encrypted image path: ")
    password = input("Enter passcode for decryption: ")
    correct_password = input("Enter the correct passcode: ")  # Store this securely
    decode_message(image_path, password, correct_password)