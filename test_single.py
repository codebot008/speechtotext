from watson_developer_cloud import SpeechToTextV1

speech_to_text = SpeechToTextV1(
        username='1399815f-4149-4ec7-8d8d-6d1547cd18e2',
        password='arkTnALuWMsy')

def main():
    text = speech_to_text.recognize(customization_id='c98e5964-574b-44f2-8022-77158863be65',
                             audio='file1.wav',
                             content_type='audio/wav',
                             smart_formatting=True)
    print(text)

if __name__ == '__main__':
    main()