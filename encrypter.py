from flask import Flask, request, send_file, jsonify, after_this_request
from cryptography.fernet import Fernet
import os

import traceback


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

        # Prepare a function to run after sending the file to delete it
        @after_this_request
        def remove_file(response):
            try:
                os.remove(encrypted_file_path)
            except Exception as e:
                app.logger.error("Error removing the encrypted file", exc_info=e)
            return response
        
        # Set the custom header with the encryption key
        response = send_file(
            encrypted_file_path,
            as_attachment=True,
            download_name='encrypted_file.txt',
            mimetype='text/plain'
        )
        response.headers['Encryption-Key'] = key.decode('utf-8')
        return response

    except Exception as e:
        # Log the full exception traceback to the console
        tb = traceback.format_exc()
        print(tb)
        return jsonify(error=str(e)), 500


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
