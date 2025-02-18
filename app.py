from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def home():
    return open('index.html').read()  # Serve the frontend HTML page

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()  # Get the data sent from the frontend
    text = data.get('text')
    target_lang = data.get('lang')

    # Initialize Google Translator
    translator = Translator()
    translated = translator.translate(text, dest=target_lang)

    # Return the translated text as a JSON response
    return jsonify({'translated_text': translated.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

