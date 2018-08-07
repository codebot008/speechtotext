import io
import os
from google.cloud import speech
from google.cloud.speech import types
from google.cloud.speech import enums

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

def speech_to_text(audio_file):
	client = speech.SpeechClient()

	content = audio_file.read()
	audio = types.RecognitionAudio(content=content)

	config = types.RecognitionConfig(encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,language_code='en-US')

	response = client.recognize(config, audio)
	response_text = ''

	for result in response.results:
		response_text = response_text + result.alternatives[0].transcript

	print(response_text)
	return response_text