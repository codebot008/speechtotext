from gtts import gTTS
import os

def read_text_file(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    return lines

def generate_audio_files(text_lines):
    i = 1
    for line in text_lines:
        tts = gTTS(text = line, lang='en', )
        tts.save("audio_files/audio_" + str(i) + ".mp3")
        i = i + 1

def main():
    lines = read_text_file('corpus_files/corpus2.txt')
    generate_audio_files(lines)

if __name__ == '__main__':
    main()