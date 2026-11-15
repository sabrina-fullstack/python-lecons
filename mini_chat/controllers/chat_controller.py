from flask import jsonify, request
from services.llm_service import ask_llm

class ChatController:
    @staticmethod
    def chat():
        data = request.get_json(silent=True) or {}
        message = data.get('message')
        if not message:
            return jsonify({'error': 'Message is required'}), 400
        return jsonify({'answer': ask_llm(message)})