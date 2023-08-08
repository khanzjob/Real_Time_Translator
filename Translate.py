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
            st.write("Listening... Speak something!")

            audio = sd.rec(int(5 * 44100), samplerate=44100, channels=1, dtype=np.int16)
            sd.wait()

            recognizer = sr.Recognizer()
            recognized_text = ""

            try:
                audio_data = audio.tobytes()  # Convert numpy array to bytes
                audio_data = sr.AudioData(audio_data, 44100, 2)  # Create AudioData object
                recognized_text = recognizer.recognize_google(audio_data, language="en")
                st.write("Recognized Text:", recognized_text)
            except sr.UnknownValueError:
                st.write("Speech Recognition could not understand audio")
            except sr.RequestError as e:
                st.write("Could not request results from Speech Recognition service; {0}".format(e))

        supported_languages = ["Luganda", "Runyankole", "Acholi", "Lugbara", "Ateso"]
        target_language = st.selectbox("Select target language:", supported_languages)

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
