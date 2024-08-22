# Example with Flask
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = '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'

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_message}]
    )
    reply = response.choices[0].message['content']
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run()
app