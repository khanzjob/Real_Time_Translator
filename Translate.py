import streamlit as st
import time
from pydub import AudioSegment
from pydub.playback import play
import numpy as np
import speech_recognition as sr
from googletrans import Translator
import requests
import base64
import os
import io
from dotenv import load_dotenv
import sounddevice as sd
import easyocr
from datetime import datetime



from CodeRunner import ENGLISH_TO_ALL_LOCAL

def AllToEnglish(text):
    translator = Translator()
    translated_text = translator.translate(text, src='auto', dest='en').text
    response = translated_text
    return response

def AudioTranslate(recognized_text, target_language):
    if recognized_text:
        text_in_english = AllToEnglish(recognized_text)
        translation_result = ENGLISH_TO_ALL_LOCAL(target_language, text_in_english)
        return translation_result
    return ""

def tts_translate(translation_result, access_token):
    url = 'https://sunbird-ai-api-5bq6okiwgq-ew.a.run.app'
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "text": translation_result
    }
    response = requests.post(f"{url}/tasks/tts", headers=headers, json=payload)

    if response.status_code == 200:
        base64_string = response.json()["base64_string"]
        return base64_string
    else:
        return None

def speak_translation(translation_result, access_token):
    if translation_result:
        base64_audio = tts_translate(translation_result, access_token)
        if base64_audio:
            audio_data = base64.b64decode(base64_audio)
            with io.BytesIO(audio_data) as audio_stream:
                st.audio(audio_stream)

def stream_recognized_speech(target_language, access_token):
    r = sr.Recognizer()
    st.write("Initializing microphone for use")
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        r.energy_threshold = 200
        r.pause_threshold = 4

        while True:
            st.write("Listening for new input")
            try:
                audio = r.listen(source)
                st.write("Recognizing")
                text = r.recognize_google(audio)
                st.write(f"Recognized Text: {text}")
                translation_result = AudioTranslate(text, target_language)
                st.write(f"Translation to {target_language}: {translation_result}")
                speak_translation(translation_result, access_token)
                
            except sr.WaitTimeoutError:
                st.write("Timeout error: the speech recognition operation timed out")
                continue
            except sr.UnknownValueError:
                st.write("Could not understand the audio")
                continue
            except sr.RequestError as e:
                st.write(f"Could not request results from the speech recognition service; check your internet connection: {e}")
                continue
            except Exception as e:
                st.write(f"An error occurred: {e}")
                continue
            finally:
                st.write("\n")  # Add a new line to separate recognized speech entries

def TranslateWords():
    st.title("Language Translator Chat")

    input_type = st.radio("Select input type:", ("Text", "Audio"))
    
    supported_languages = ["Luganda", "Runyankole", "Acholi", "Lugbara", "Ateso"]
    target_language = st.selectbox("Select target language:", supported_languages)
    access_token = os.getenv("SUNBIRD_ACCESSTOKEN")

    if input_type == "Audio":
        st.write("Streamed Speech:")
        streamed_speech_placeholder = st.empty()  # Create a placeholder for displaying streamed speech
        if st.button("Start Listening"):
            stream_recognized_speech(target_language, access_token)
    else:
        prompt = st.text_area("Enter your message or translation query:")
        if st.button("Translate"):
            translation_result = AudioTranslate(prompt, target_language)
            st.write(f"Translation to {target_language}: {translation_result}")
            speak_translation(translation_result, access_token)




    
 
if __name__ == "__main__":
    TranslateWords()
