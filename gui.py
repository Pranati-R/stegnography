import tkinter as tk#lbrary
from tkinter import filedialog, messagebox
import encoder
import decoder

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Steganography")

        tk.Label(root, text="Select Image:").grid(row=0, column=0)
        self.image_path_entry = tk.Entry(root, width=40)
        self.image_path_entry.grid(row=0, column=1)
        tk.Button(root, text="Browse", command=self.browse_image).grid(row=0, column=2)

        tk.Label(root, text="Enter Secret Message:").grid(row=1, column=0)
        self.message_entry = tk.Entry(root, width=40)
        self.message_entry.grid(row=1, column=1)

        tk.Label(root, text="Enter Passcode:").grid(row=2, column=0)
        self.passcode_entry = tk.Entry(root, width=40, show="*")
        self.passcode_entry.grid(row=2, column=1)

        tk.Button(root, text="Encode", command=self.encode).grid(row=3, column=1)

        tk.Label(root, text="Enter Passcode for Decryption:").grid(row=4, column=0)
        self.decode_passcode_entry = tk.Entry(root, width=40, show="*")
        self.decode_passcode_entry.grid(row=4, column=1)

        tk.Button(root, text="Decode", command=self.decode).grid(row=5, column=1)

    def browse_image(self):
        file_path = filedialog.askopenfilename()
        self.image_path_entry.delete(0, tk.END)
        self.image_path_entry.insert(0, file_path)

    def encode(self):
        image_path = self.image_path_entry.get()
        message = self.message_entry.get()
        password = self.passcode_entry.get()

        if not image_path or not message or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        encoder.encode_message(image_path, message, password)
        messagebox.showinfo("Success", "Message encoded successfully!")

    def decode(self):
        image_path = self.image_path_entry.get()
        password = self.decode_passcode_entry.get()
        correct_password = self.passcode_entry.get()  # Get stored password

        if not image_path or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        decoder.decode_message(image_path, password, correct_password)

if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()