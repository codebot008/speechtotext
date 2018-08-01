from gtts import gTTS
from watson_developer_cloud import TextToSpeechV1
import os

text_to_speech = TextToSpeechV1(
    username='c94a5f2a-ba8c-4ad7-9ddf-494b6e407644',
    password='jVat5C8dlfev')


def read_text_file(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    return lines


def generate_audio_files(text_lines):
    i = 1
    for line in text_lines:
        # tts = gTTS(line)
        # tts.save('audio_files/audio_' + str(i) + '.wav')
        with open('audio_files/audio_' + str(i) + '.wav', 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                    line, 'audio/wav', 'en-US_AllisonVoice').content)
        i = i + 1


def main():
    lines = read_text_file('corpus_files/corpus2.txt')
    generate_audio_files(lines)


if __name__ == '__main__':
    main()