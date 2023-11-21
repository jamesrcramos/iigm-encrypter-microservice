from flask import Flask, request, send_file, jsonify
from cryptography.fernet import Fernet
import os


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'This service is running!'

@app.route('/encrypt_file', methods=['POST'])
def encrypt_file():
    try:
        # Generate a key for encryption
        key = Fernet.generate_key()
        fernet = Fernet(key)

        # Get the file from the request
        file = request.files['file']
        file_content = file.read()

        # Encrypt the file
        encrypted_content = fernet.encrypt(file_content)

        # Save the encrypted file temporarily
        encrypted_file_path = 'encrypted_file.txt'
        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_content)

        # Send the encrypted file and the key as a response
        response = send_file(
            encrypted_file_path,
            as_attachment=True,
            attachment_filename='encrypted_file.txt'
        )

        # Set the key in a custom header
        response.headers['Encryption-Key'] = key.decode('utf-8')

        # Remove the encrypted file after sending it
        os.remove(encrypted_file_path)

        return response

    except Exception as e:
        return jsonify(error=str(e)), 500


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
