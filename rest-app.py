import flask
from flask import request, jsonify
import json
from watson_developer_cloud import LanguageTranslatorV3

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    iam_apikey='RHogqQ9L0vAECR7Pbi2AduMHZ0yGRHOSmh3LI0qH7ju3',
    url='https://gateway.watsonplatform.net/language-translator/api'
)

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return '''<h1>APP is Working</h1>
<p>A prototype API for Translation</p>'''


@app.route('/api/v1/resources/languages/all', methods=['GET'])
def api_all():
    languages = language_translator.list_identifiable_languages().get_result()
    #print(json.dumps(languages, indent=2))
    return json.dumps(languages, indent=4)


@app.route('/api/v1/resources/languages/', methods=['GET'])
def Id_lang():
    if 'text' in request.args:
        text = str(request.args['text'])
    else:
        return "Error: Only string is allowed"


    language = language_translator.identify(
        text).get_result()
    #print(language["languages"][0]["language"])
    return language["languages"][0]["language"]


@app.route('/api/v1/resources/translate', methods=['GET'])
def api_translate():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'text' in request.args:
        text = str(request.args['text'])
    else:
        return "Error: Only string is allowed"


    def Translate(lang, text):
        model_id = lang + "-" + "en"
        translation = language_translator.translate(
            text,
            model_id).get_result()
        # print(translation)
        print(translation["translations"][0]['translation'])
        return translation["translations"][0]['translation']

    lang = Id_lang()
    Translate(lang, text)




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
