from watson_developer_cloud import SpeechToTextV1
import json
import os, time

speech_to_text = SpeechToTextV1(
    username='1399815f-4149-4ec7-8d8d-6d1547cd18e2',
    password='arkTnALuWMsy')


def createAcousticModel():
    acoustic_model = speech_to_text.create_acoustic_model(
        'New acoustic model',
        'en-US_BroadbandModel',
        description='Custom acoustic model')
    print(json.dumps(acoustic_model, indent=2))
    return (acoustic_model["customization_id"])

def addAudio(cust_id, audio_dir):
    # speech_to_text.add_audio(customization_id=cust_id, audio_name='new_audio1', audio_resource=audio_dir, content_type='audio/wav')
    # print("In add audio")
    # i = 1
    # path = '/Users/ankitjena/PycharmProjects/Speech2Text/audio_files'
    # files = os.listdir(audio_dir)
    # for filename in files:
    #     status = speech_to_text.list_acoustic_models()["customizations"][0]["status"]
    #     f = open(os.path.join(path, filename), 'rb')
    #     while status != 'ready':
    #         status = speech_to_text.list_acoustic_models()["customizations"][0]["status"]
    #     speech_to_text.add_audio(cust_id, 'audio_' + str(i), f, 'audio/wav')
    #     f.close()
    #     print('Progress: ' + str(round(((i / len(files))) * 100, 2)) + "%")
    #     i = i + 1
    speech_to_text.add_audio(customization_id=cust_id, audio_name="new_audio_3", audio_resource=audio_dir, content_type='application/zip', contained_content_type='audio/wav', allow_overwrite=True)

def deleteAudio(cust_id):
    all_audio = speech_to_text.list_audio(cust_id)["audio"]
    for x in all_audio:
        name = x['name']
        speech_to_text.delete_audio(cust_id, name)
        print('Deleted ' + name)

def trainAcousticModel(cust_id):
    speech_to_text.train_acoustic_model(cust_id)


def trainLangModel(cust_id):
    print("In train model")
    # cust_id = '2497fdbf-b531-4eb3-bc83-8a8572f1fa81'
    speech_to_text.train_language_model(cust_id)

def customiseAcouticModel(audio_archive):
    cust_id = createAcousticModel()
    addAudio(cust_id, audio_archive)
    f = open('audio_cust_id.txt', 'w')
    f.write(cust_id)
    f.close()
    trainAcousticModel(cust_id)

def getAllAcousticModels():
    acoustic_models = speech_to_text.list_acoustic_models()
    print(acoustic_models["customizations"][0]["status"])
    return acoustic_models["customizations"][0]["status"]
    # print(json.dumps(acoustic_models, indent=2))

def main():
    # deleteAudio('26081e44-d2e8-429c-af7d-e3269caeec38')
    # with open('audio_files.zip', 'rb') as audio_file:
    #     addAudio('26081e44-d2e8-429c-af7d-e3269caeec38', audio_file)
    #     speech_to_text.add_audio(
    #         '26081e44-d2e8-429c-af7d-e3269caeec38',
    #         'audio2',
    #         audio_file,
    #         'audio/wav')
    # cust_id = createAcousticModel()
    # status = 'pending'
    # while(status == 'pending'):
    #     time.sleep(3)
    #     status = getAllAcousticModels()
    # addAudio('26081e44-d2e8-429c-af7d-e3269caeec38', 'audio_files')
    speech_to_text.train_acoustic_model('26081e44-d2e8-429c-af7d-e3269caeec38')
    # speech_to_text.add_audio('26081e44-d2e8-429c-af7d-e3269caeec38', 'audio_files/audio_1.wav')

if __name__ == '__main__':
    main()
