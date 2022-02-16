# import the Flask class from the flask module
from flask import Flask
from flask import send_file

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/firmware')
def get_firmware():
    result = ''
    with open('blink.bin', 'rb') as firm:
        b = firm.read(1)
        while b:
            result += f'{bytes(b).hex()}'.upper()+' '
            b = firm.read(1)    
    return result

@app.route('/firmware_file')
def get_firmware_file():
    try:
        return send_file('blink.bin')
    except Exception as Ex:
        return str(Ex)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)