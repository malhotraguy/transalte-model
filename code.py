import json
from watson_developer_cloud import LanguageTranslatorV3

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    iam_apikey='RHogqQ9L0vAECR7Pbi2AduMHZ0yGRHOSmh3LI0qH7ju3',
    url='https://gateway.watsonplatform.net/language-translator/api'
)
#============Translate=====================================================
def Translate(lang,ttext):
    model_id=lang+"-"+"en"
    translation = language_translator.translate(
        ttext,
        model_id).get_result()
    #print(translation)
    print(translation["translations"][0]['translation'])
    #print(json.dumps(translation, indent=2, ensure_ascii=False))
#=======================List identifiable language============================
"""languages = language_translator.list_identifiable_languages().get_result()
print(json.dumps(languages, indent=2))"""
#=========================Idetify Language=================================
def Id_lang(text):
    language = language_translator.identify(
        text).get_result()
    print(language["languages"][0]["language"])
    return language["languages"][0]["language"]
    """print(language["languages"][0]["language"])
    print(json.dumps(language, indent=2))"""
#============================LIst Models=====================================
"""models = language_translator.list_models().get_result()
print(json.dumps(models, indent=2))"""
#=================================

userinp=input("Ask your question?: ")
lang=Id_lang(userinp)
Translate(lang,userinp)



