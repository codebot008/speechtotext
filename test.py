from watson_developer_cloud import SpeechToTextV1
import json

speech_to_text = SpeechToTextV1(
    username='1399815f-4149-4ec7-8d8d-6d1547cd18e2',
    password='arkTnALuWMsy')


# acoustic_model = speech_to_text.create_acoustic_model(
#     'First example acoustic model',
#     'en-US_BroadbandModel',
#     description='First custom acoustic model example')
# print(json.dumps(acoustic_model, indent=2))


# speech_to_text.delete_audio('26081e44-d2e8-429c-af7d-e3269caeec38', 'audio_2')
# print(json.dumps(speech_to_text.list_acoustic_models(), indent = 2))
print(json.dumps(speech_to_text.list_audio('26081e44-d2e8-429c-af7d-e3269caeec38'), indent = 2))
# acoustic_models = speech_to_text.list_acoustic_models()
# print(acoustic_models["customizations"][0]["status"])