from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from stt import  speech_to_text



import os
 
app = Flask(__name__)
 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!  <a href='/logout'>Logout</a>"
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route("/stt", methods=['POST'])
def stt():
    print('Inside stt()')
    print(request.values)
    audio_file=request.files['file']
    if audio_file is None:
        print('Yay')
    transcription=speech_to_text(audio_file)
    print(transcription)
    return transcription

def show_files(request):
    for x in request:
        print(x)

 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000)
