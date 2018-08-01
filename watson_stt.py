from watson_developer_cloud import SpeechToTextV1
from os.path import join, dirname
import audio_recorder
import audiotools
import json

def convert(file):
    speech_to_text = SpeechToTextV1(
        username='1399815f-4149-4ec7-8d8d-6d1547cd18e2',
        password='arkTnALuWMsy')

    cust_id_file = open('cust_id.txt', 'r')
    cust_id = cust_id_file.readline()
    cust_id_file.close()

    with open(file,'rb') as audio_file:
        speech_recognition_results = speech_to_text.recognize(

            customization_id=cust_id,
            audio=audio_file,
            content_type='audio/wav',
            smart_formatting=True)
    return speech_recognition_results
    # return (speech_recognition_results['results'][0]['alternatives'][0]['transcript'])

def stt():
    aud_recorder  = audio_recorder.AudioRecorder()
    audio_file = aud_recorder.start()
    # audio_file_flac = audio_file.replace(".wav", ".flac")
    # audiotools.open(audio_file).convert(audio_file_flac, audiotools.FlacAudio)
    textfromspeech = convert(audio_file)
    print(textfromspeech)

#Run a remote registry service on server f3bd9c44dd.

def main():
    stt()

if __name__ == '__main__':
    main()