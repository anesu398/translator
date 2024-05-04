from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

# Create a translator object
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    src_lang = request.form['src_lang']
    dest_lang = request.form['dest_lang']

    translated_text = translate_text(text, src_lang, dest_lang)

    return render_template('index.html', translated_text=translated_text)

def translate_text(text, src_lang='auto', dest_lang='en'):
    """
    Translates the given text from source language to destination language.

    Parameters:
        text (str): The text to be translated.
        src_lang (str): The source language of the text. Defaults to 'auto'.
        dest_lang (str): The destination language for translation. Defaults to 'en'.

    Returns:
        str: The translated text.
    """
    translated_text = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated_text.text

if __name__ == '__main__':
    app.run(debug=True)
