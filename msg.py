from cryptography.fernet import Fernet

class SecureMessagingApp:
    def __init__(self, key):
        self.key = key
        self.cipher_suite = Fernet(key)

    def encrypt_message(self, message):
        encrypted_message = self.cipher_suite.encrypt(message.encode())
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = self.cipher_suite.decrypt(encrypted_message).decode()
        return decrypted_message

if __name__ == "__main__":
    # Generate a random key for encryption
    key = Fernet.generate_key()
    app = SecureMessagingApp(key)

    # Example of sending and receiving messages
    message_to_send = "Hello, Alice! This is a secure message."
    encrypted_message = app.encrypt_message(message_to_send)
    print("Encrypted message:", encrypted_message)

    decrypted_message = app.decrypt_message(encrypted_message)
    print("Decrypted message:", decrypted_message)
