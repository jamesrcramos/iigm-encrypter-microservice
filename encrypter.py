from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'This service is running!'


@app.route('/encrypt_file', methods=['POST'])
def encrypt_file():
    try:
        print("Hello world!")
    except Exception as e:
        print("Hello world!")


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
