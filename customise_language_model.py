from watson_developer_cloud import SpeechToTextV1
import json
import os, time

speech_to_text = SpeechToTextV1(
    username='1399815f-4149-4ec7-8d8d-6d1547cd18e2',
    password='arkTnALuWMsy')

def createLangModel():
    language_model = speech_to_text.create_language_model(
        'New language model',
        'en-US_BroadbandModel',
        description='Custom language model')
    print(language_model["customization_id"])
    return (language_model["customization_id"])

def addCorpus(cust_id, corpus_file):
    print("In add corpus")
    # cust_id = '2497fdbf-b531-4eb3-bc83-8a8572f1fa81'
    speech_to_text.add_corpus(cust_id, 'corpus_file3', corpus_file)

def trainLangModel(cust_id):
    print("In train model")
    # cust_id = '2497fdbf-b531-4eb3-bc83-8a8572f1fa81'
    speech_to_text.train_language_model(cust_id)

def customiseLangModel(corpus_file):
    cust_id = createLangModel()
    addCorpus(cust_id, corpus_file)
    print('Hi')
    f = open('cust_id.txt', 'w')
    f.write(cust_id)
    f.close()
    # trainLangModel(cust_id)

def getAllLanguageModels():
    language_models = speech_to_text.list_language_models()
    print(json.dumps(language_models, indent=2))

def main():
    # customiseLangModel('corpus1.txt')
    # print(speech_to_text.delete_language_model('75c07ea9-8089-4821-a072-e8caf6d445f6'))
    # getAllLanguageModels()
    # speech_to_text.add_corpus('c98e5964-574b-44f2-8022-77158863be65', 'new_corpus', 'corpus1.txt')
    # speech_to_text.train_language_model('c98e5964-574b-44f2-8022-77158863be65')
    while(True):
        time.sleep(3)
        getAllLanguageModels()

if __name__ == '__main__':
    main()
