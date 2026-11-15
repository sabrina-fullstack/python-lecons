from flask import Flask, jsonify, request

app = Flask(__name__)

@app.post('/chat')
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get('message')
    if not message:
        return jsonify({'error': 'Message is required'}), 400
    return jsonify({'answer': f"Tu as dit : {message}"})

if __name__ == '__main__':
    app.run(port=5002, debug=True)