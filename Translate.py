
import streamlit as st
from googletrans import Translator
import streamlit as st
import time

from CodeRunner import ENGLISH_TO_ALL_LOCAL


def AllToEnglish(text):
    translator = Translator()
    translated_text = translator.translate(text).text
    response = translated_text
    return response


def TranslateWords():
    st.title("Language Translator Chat")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

   
    
    # Accept user input
    prompt = st.chat_input("Enter your message or translation query:")
     # Supported languages
    supported_languages = ["Luganda", "Runyankole", "Acholi", "Lugbara", "Ateso"]
    
    # Dropdown for language selection
    target_language = st.selectbox("Select target language:", supported_languages)

    if prompt:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.spinner("Translating..."):

                # Translate user input to English
            text_in_english = AllToEnglish(prompt)

            # Translate English text to the selected target language
            translation_result = ENGLISH_TO_ALL_LOCAL(target_language, text_in_english)

            # Display assistant response in chat message container
            with st.chat_message("assistant"):

                message_placeholder = st.empty()
                full_response = ""
                assistant_response = f"Translation to {target_language}: {translation_result}"

                    # Simulate stream of response with milliseconds delay
                for chunk in assistant_response.split():
                    full_response += chunk + " "
                    time.sleep(0.05)
                        # Add a blinking cursor to simulate typing
                    message_placeholder.markdown(full_response + "▌")
                    message_placeholder.markdown(full_response)

                    # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            

if __name__ == "__main__":
    TranslateWords()
