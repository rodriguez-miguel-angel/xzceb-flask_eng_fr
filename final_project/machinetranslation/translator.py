"""
A python file for Watson Translation Service:
create an instance of the IBM Watson Language translator,
create a function that translates English text to French,
create a function that translates French text to English.
"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def translator_instance():
    """
    This function create an instance of the IBM Watson Language translator
    """
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
    )
    language_translator.set_service_url(url)
    return language_translator


def english_to_french(english_text):
    """
    This function takes in the englishText as a string argument.
    It uses the instance of the Language Translator created previously,
    to translate the text input in English to French and return the French text.
    """
    if english_text is None:
        return None

    language_translator = translator_instance()
    response = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    
    # print(json.dumps(response, indent=2, ensure_ascii=False))

    french_text = response.get("translations")[0].get('translation')
    return french_text



def french_to_english(french_text):
    """
    This function takes in the frenchText as a string argument.
    It uses the instance of the Language Translator created previously,
    to translate the text input in French to English and return the English text.
    """
    if french_text is None:
        return None

    language_translator = translator_instance()
    response = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

    # print(json.dumps(response, indent=2, ensure_ascii=False))

    english_text = response.get("translations")[0].get('translation')

    return english_text
