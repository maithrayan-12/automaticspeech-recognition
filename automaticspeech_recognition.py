# -*- coding: utf-8 -*-
"""automaticspeech recognition.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wE6b7yiDzmeETXa7X-H4qe16ibZCZ2R0
"""

!pip install SpeechRecognition pyttsx3 gTTS playsound pyaudio

# Install SpeechRecognition and gTTS for TTS
!pip install SpeechRecognition gTTS pydub

!pip install pyttsx3

import speech_recognition as sr
from gtts import gTTS
from IPython.display import Audio, display
import pyttsx3
import datetime
import webbrowser

!pip install gTTS

from gtts import gTTS
from IPython.display import Audio, display

# Text-to-speech function
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    display(Audio("output.mp3", autoplay=True))

speak("Hello, how can I help you today?")

recognized_text = "Set a reminder for meeting at 5 PM"  # Example recognized text
if 'reminder' in recognized_text.lower():
    speak("What would you like me to remind you about?")
elif 'weather' in recognized_text.lower():
    speak("Please check the weather on your preferred website.")
else:
    speak("I did not understand. Please try again.")

import speech_recognition as sr

# Function to recognize speech from audio file
def recognize_from_file(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)  # Read the audio file

    try:
        text = recognizer.recognize_google(audio)
        print(f"Recognized Text: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Request error from Google Speech Recognition service: {e}")
        return None

from gtts import gTTS
from IPython.display import Audio, display

# Function to generate and play speech
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    display(Audio("response.mp3", autoplay=True))

!pip install streamlit SpeechRecognition gTTS pydub

import streamlit as st
from gtts import gTTS
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

# ---------- Text-to-Speech Function ----------
def speak(text):
    tts = gTTS(text=text, lang='en')
    # Save to BytesIO buffer instead of file
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    st.audio(mp3_fp, format='audio/mp3', start_time=0)


# ---------- Speech Recognition from Audio File ----------
def recognize_from_file(uploaded_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(uploaded_file) as source:
        audio = recognizer.record(source)  # Read the audio file

    try:
        text = recognizer.recognize_google(audio)
        st.success(f"Recognized Text: {text}")
        return text
    except sr.UnknownValueError:
        st.error("Could not understand the audio.")
        return None
    except sr.RequestError as e:
        st.error(f"Request error from Google Speech Recognition service: {e}")
        return None


# ---------- Streamlit App ----------
def main():
    st.title("🗣️ Speech Recognition & Text-to-Speech App")

    st.header("🎙️ Upload Audio File for Speech Recognition")
    uploaded_file = st.file_uploader("Upload an audio file (wav format)", type=["wav"])

    if uploaded_file is not None:
        recognized_text = recognize_from_file(uploaded_file)

        if recognized_text:
            # Example simple commands
            if 'reminder' in recognized_text.lower():
                speak("What would you like me to remind you about?")
            elif 'weather' in recognized_text.lower():
                speak("Please check the weather on your preferred website.")
            else:
                speak("I did not understand. Please try again.")

    st.header("💬 Text-to-Speech")
    input_text = st.text_input("Enter text to speak:")
    if st.button("Speak"):
        if input_text:
            speak(input_text)
        else:
            st.warning("Please enter some text.")


if __name__ == "__main__":
    main()

!pip install SpeechRecognition gTTS pydub

!pip install streamlit
!pip install pyngrok

# Install required packages
!pip install streamlit pyngrok gTTS SpeechRecognition pydub

import streamlit as st
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr
import tempfile
import os

# ---- TEXT TO SPEECH FUNCTION ---- #
def speak(text):
    tts = gTTS(text=text, lang='en')
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    audio = AudioSegment.from_mp3(temp_file.name)
    play(audio)
    os.remove(temp_file.name)

# ---- SPEECH RECOGNITION FUNCTION ---- #
def recognize_from_file(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)  # Read the audio file
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError as e:
        return f"Request error from Google Speech Recognition service: {e}"

# ---- STREAMLIT APP ---- #
def main():
    st.title("🎙️ Voice Assistant (Speech to Text & Text to Speech)")
    st.markdown("Upload an audio file (WAV format), and get the recognized text. Also, type anything to hear it spoken out!")

    # --- Text to Speech Section --- #
    st.header("🔊 Text to Speech")
    user_text = st.text_input("Enter text to speak:")
    if st.button("Speak"):
        if user_text:
            speak(user_text)
        else:
            st.warning("Please enter some text.")

    # --- Speech to Text Section --- #
    st.header("🎧 Speech to Text")
    audio_file = st.file_uploader("Upload an audio file (WAV format)", type=["wav"])
    if audio_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_audio:
            tmp_audio.write(audio_file.read())
            tmp_audio_path = tmp_audio.name

        st.audio(audio_file, format='audio/wav')
        recognized_text = recognize_from_file(tmp_audio_path)
        st.success(f"Recognized Text: {recognized_text}")

        # --- Response logic based on recognized text --- #
        if 'reminder' in recognized_text.lower():
            response = "What would you like me to remind you about?"
        elif 'weather' in recognized_text.lower():
            response = "Please check the weather on your preferred website."
        else:
            response = "I did not understand. Please try again."

        st.info(response)
        speak(response)

        os.remove(tmp_audio_path)

if __name__ == "__main__":
    main()

import gradio as gr
from gtts import gTTS
import speech_recognition as sr
import tempfile
import os

# ---- TEXT TO SPEECH FUNCTION ---- #
def speak(text):
    tts = gTTS(text=text, lang='en')
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")  # Don't auto-delete
    tts.save(temp_file.name)
    return temp_file.name  # Return path for Gradio to play

# ---- SPEECH TO TEXT FUNCTION ---- #
def recognize_from_file(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)  # Read the audio file
    try:
        text = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        text = "Could not understand the audio."
    except sr.RequestError as e:
        text = f"Request error: {e}"
    return text

# ---- Main Assistant Logic ---- #
def assistant(audio, user_text):
    output_audio = None
    response = ""

    # Process audio (speech to text)
    if audio is not None:
        recognized = recognize_from_file(audio)
        response = recognized
        if 'reminder' in recognized.lower():
            response = "What would you like me to remind you about?"
        elif 'weather' in recognized.lower():
            response = "Please check the weather on your preferred website."
        else:
            response = "I did not understand. Please try again."
        output_audio = speak(response)

    # Process text (text to speech)
    if user_text:
        output_audio = speak(user_text)
        response = user_text

    return response, output_audio  # Text response, Audio response

# ---- Gradio Interface ---- #
interface = gr.Interface(
    fn=assistant,
    inputs=[
        gr.Audio(type="filepath", label="Upload Audio (WAV)"),  # Upload WAV file
        gr.Textbox(label="Enter Text to Speak"),               # Or enter text
    ],
    outputs=[
        gr.Textbox(label="Recognized / Response Text"),
        gr.Audio(label="Response Audio"),                     # Playback audio response
    ],
    title="🎙️ Voice Assistant (Speech ↔ Text)"
)

interface.launch(debug=True)