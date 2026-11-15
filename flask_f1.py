from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/')
def home():
    return jsonify({'message': 'Hello from Flask'})

if __name__ == '__main__':
    app.run(port=5002, debug=True)