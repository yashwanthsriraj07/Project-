import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet, InvalidToken

class SecureMessagingApp:
    def __init__(self, key):
        self.key = key
        self.cipher_suite = Fernet(key)

    def encrypt_message(self, message):
        encrypted_message = self.cipher_suite.encrypt(message.encode())
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        try:
            decrypted_message = self.cipher_suite.decrypt(encrypted_message)
            return decrypted_message.decode()
        except InvalidToken:
            messagebox.showerror("Error", "Invalid message or key")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def send_message():
    message_to_send = entry_send.get()
    encrypted_message = app.encrypt_message(message_to_send)
    entry_encrypted.delete(0, tk.END)  # Clear the field before inserting new value
    entry_encrypted.insert(tk.END, encrypted_message.decode())

def receive_message():
    encrypted_message = entry_receive.get().strip()  # Remove leading/trailing whitespace
    decrypted_message = app.decrypt_message(encrypted_message.encode())
    if decrypted_message:
        entry_decrypted.delete(0, tk.END)  # Clear the field before inserting new value
        entry_decrypted.insert(tk.END, decrypted_message)

if __name__ == "__main__":
    # Generate a random key for encryption
    key = Fernet.generate_key()
    app = SecureMessagingApp(key)

    # GUI setup
    root = tk.Tk()
    root.title("Secure Messaging Application")

    label_send = tk.Label(root, text="Enter message to send:")
    label_send.pack()
    entry_send = tk.Entry(root)
    entry_send.pack()

    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack()

    label_encrypted = tk.Label(root, text="Encrypted message:")
    label_encrypted.pack()
    entry_encrypted = tk.Entry(root)
    entry_encrypted.pack()

    label_receive = tk.Label(root, text="Enter received message:")
    label_receive.pack()
    entry_receive = tk.Entry(root)
    entry_receive.pack()

    receive_button = tk.Button(root, text="Receive", command=receive_message)
    receive_button.pack()

    label_decrypted = tk.Label(root, text="Decrypted message:")
    label_decrypted.pack()
    entry_decrypted = tk.Entry(root)
    entry_decrypted.pack()

    root.mainloop()
