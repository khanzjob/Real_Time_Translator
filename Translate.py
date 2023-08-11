import streamlit as st
import time
import sounddevice as sd
import numpy as np
import speech_recognition as sr
from googletrans import Translator
from CodeRunner import ENGLISH_TO_ALL_LOCAL

def AllToEnglish(text):
    translator = Translator()
    translated_text = translator.translate(text).text
    response = translated_text
    return response
def streamData(translation_result):

    with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                assistant_response = f"GENERAL LANGUAGE: {translation_result}"

                for chunk in assistant_response.split():
                    full_response += chunk + " "
                    time.sleep(0.05)
                    message_placeholder.markdown(full_response + "▌")
                    message_placeholder.markdown(full_response)

                st.session_state.messages.append({"role": "assistant", "content": full_response})

def AudioTranslate(recognized_text,target_language):
    if recognized_text:
            text_in_english = AllToEnglish(recognized_text)
            translation_result = ENGLISH_TO_ALL_LOCAL(target_language, text_in_english)
        
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                assistant_response = f"Translation to {target_language}: {translation_result}"

                for chunk in assistant_response.split():
                    full_response += chunk + " "
                    time.sleep(0.05)
                    message_placeholder.markdown(full_response + "▌")
                    message_placeholder.markdown(full_response)

                st.session_state.messages.append({"role": "assistant", "content": full_response})

def listen(target_language):
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.write("Initializing microphone for use...")
            r.adjust_for_ambient_noise(source, duration=5)
            r.energy_threshold = 200
            r.pause_threshold = 4

            while True:
                text = ""
                st.write("Listening for new input. now...")
                try:
                    audio = r.listen(source, timeout=90, phrase_time_limit=90)  # Updated to 90 seconds
                    st.write("Recognizing...")
                    text = r.recognize_google(audio)
                    streamData(text)
                    AudioTranslate(text,target_language)
                    
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

                # engine.runAndWait()
    except Exception as e:
        st.write(f"An error occurred: {e}")



def TranslateWords():
    st.title("Language Translator Chat")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    input_type = st.radio("Select input type:", ("Text", "Audio"))

    if input_type == "Audio":
        st.write("")  # Empty space for better layout

        if st.button("Start Listening"):
            try:
                supported_languages = ["Luganda", "Runyankole", "Acholi", "Lugbara", "Ateso"]
                target_language = st.selectbox("Select target language:", supported_languages)
                listen(target_language)
                  
            except sr.UnknownValueError:
                st.write("Speech Recognition could not understand audio")
            except sr.RequestError as e:
                st.write("Could not request results from Speech Recognition service; {0}".format(e))

    else:
        prompt = st.chat_input("Enter your message or translation query:")

        supported_languages = ["Luganda", "Runyankole", "Acholi", "Lugbara", "Ateso"]
        target_language = st.selectbox("Select target language:", supported_languages)

        if prompt:
            text_in_english = AllToEnglish(prompt)
            translation_result = ENGLISH_TO_ALL_LOCAL(target_language, text_in_english)

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                assistant_response = f"Translation to {target_language}: {translation_result}"

                for chunk in assistant_response.split():
                    full_response += chunk + " "
                    time.sleep(0.05)
                    message_placeholder.markdown(full_response + "▌")
                    message_placeholder.markdown(full_response)

                st.session_state.messages.append({"role": "assistant", "content": full_response})


if __name__ == "__main__":
    TranslateWords()
