# IIGM Encrypter Microservice

This lightweight Flask microservice is designed to securely encrypt files sent over HTTP. The service provides an endpoint for clients to upload text files. After successfully uploading a text file, the client receives the text file back encrypted along with an encryption key for the session.

## Requesting Data

To request data from the microservice, you can send a POST request to the /encrypt_file endpoint with the file you wish to encrypt included in the form data. Here is an example done in Python below:

```python
import requests

# URL of the endpoint you are sending the file to
url = 'http://localhost:5000/encrypt_file'

# path to the text file you want to send
file_path = 'path/to/your/file.txt'

# open the file in binary read mode
with open(file_path, 'rb') as file:
    # define the file in a dictionary
    files = {'file': (file.name, file, 'text/plain')}

    # send the POST request
    response = requests.post(url, files=files)

    # check if the request was successful
    if response.status_code == 200:
        # save the encrypted file content to a file
        with open('encrypted_file.txt', 'wb') as encrypted_file:
            encrypted_file.write(response.content)
        print('The encrypted file has been saved.')
    else:
        print(f'Failed to encrypt the file. Status code: {response.status_code}')
        print(response.text)

```

## Receiving Data

The service will respond with the encrypted file and a unique key for decryption. The encrypted file is sent back in the response body. The encryption key is provided in the response headers, which can be accessed programmatically for client applications not using a web browser.

If you make a request via a web browser, the browser typically interprets the Content-Disposition header in the response as an instruction to download the file. This usually results in the browser automatically downloading the file to the user's default download directory, or it may ask the user where to save the file, depending on the browser settings. 

If you make the request through a scripting HTTP client like requests in Python, the file is not automatically saved to the user's device. Instead, the file's content is included in the response object, and it's up to the developer to save it to the filesystem. The requests library will receive the file content as a raw byte stream, which can then be written to a file as shown. This must be done programmatically, as shown in the code snippet below from the code in the "Requesting Data" section:

```python
# check if the request was successful
    if response.status_code == 200:
        # save the encrypted file content to a file
        with open('encrypted_file.txt', 'wb') as encrypted_file:
            encrypted_file.write(response.content)
        print('The encrypted file has been saved.')
    else:
        print(f'Failed to encrypt the file. Status code: {response.status_code}')
        print(response.text)
```

## UML Diagram of Data Flow

[![](https://mermaid.ink/img/pako:eNp9UmFv2jAQ_Sun-5wynCWk8QekqSvtNLGiwqcp0uTZ19ZtsDPb0DHEf5-TUA3KWn-y7t5793x-W5RWEXL09GtFRtJnLe6dWFYG4mmEC1rqRpgAF7UmE07rk1r4pzm5NTkQHirsCtBXKjwlTLV01se2llSZvt-Ln43HB2ocZjfzBXyIrtymCT_udE09-gAUKYd6HCbWPQun4LZ9j9_7_WYDgW0dHoNnzkryXpv7Y_wh6mTCZe8HJtFPpEnSa1KgTbz7xhpP78_c07U18JU28MXDp9pbuCJDTgRS_3Hwei97iTi18yCM6qRe5sPNz0eS4XRXUadfNIfrxWL2j_Csw8MbqpXBBJfklkKrGJNtq1pheKAlVcjjVQn31H7zLuLEKtj5xkjkwa0owVWj4pP2kUJ-J2ofq6R0sG7a566LX4IxGci3-Bt5ygYly8r8vCzTnH0s8zTBDXJWZoM0H7JRlo1yNixGuwT_WBtV2WCYsyItMpYWw_MsL_JO7nvXbH3s_gJq7_m8?type=png)](https://mermaid.live/edit#pako:eNp9UmFv2jAQ_Sun-5wynCWk8QekqSvtNLGiwqcp0uTZ19ZtsDPb0DHEf5-TUA3KWn-y7t5793x-W5RWEXL09GtFRtJnLe6dWFYG4mmEC1rqRpgAF7UmE07rk1r4pzm5NTkQHirsCtBXKjwlTLV01se2llSZvt-Ln43HB2ocZjfzBXyIrtymCT_udE09-gAUKYd6HCbWPQun4LZ9j9_7_WYDgW0dHoNnzkryXpv7Y_wh6mTCZe8HJtFPpEnSa1KgTbz7xhpP78_c07U18JU28MXDp9pbuCJDTgRS_3Hwei97iTi18yCM6qRe5sPNz0eS4XRXUadfNIfrxWL2j_Csw8MbqpXBBJfklkKrGJNtq1pheKAlVcjjVQn31H7zLuLEKtj5xkjkwa0owVWj4pP2kUJ-J2ofq6R0sG7a566LX4IxGci3-Bt5ygYly8r8vCzTnH0s8zTBDXJWZoM0H7JRlo1yNixGuwT_WBtV2WCYsyItMpYWw_MsL_JO7nvXbH3s_gJq7_m8)