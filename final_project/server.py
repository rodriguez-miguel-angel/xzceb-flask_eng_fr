from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    '''
    This function takes the English text as input through the request parameter and return a string.
    '''
    textToTranslate = request.args.get('textToTranslate')
    # version 1: return "Translated text to French"
    return translator.english_to_french(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    '''
    This function takes the French text as input through the request parameter and return a string.
    '''
    textToTranslate = request.args.get('textToTranslate')
    # version 1: return "Translated text to English"
    return translator.french_to_english(textToTranslate)

@app.route("/")
def renderIndexPage():
    '''
    This function renders the index.html.
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

