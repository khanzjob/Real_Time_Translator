import streamlit as st
from googletrans import Translator
import streamlit as st
import time
def translate_and_detect(query):
    translator = Translator()
    detected_language = translator.detect(query).lang
    translated_text = translator.translate(query).text
    response = f"Detected Language: {detected_language}\n Translated Text (English): {translated_text}"
    return response

def TranslateWords():
    st.title("Language Translator App")
     # Form setup
    with st.form(key="form"):
        user_input = st.text_input("Enter your message:")
        submit_button = st.form_submit_button("Send")

    if submit_button:
        st.chat_message("user").write(user_input)
        with st.chat_message("assistant"):
            result  = translate_and_detect(user_input)
        
            st.write(result)





if __name__ == "__main__":
    TranslateWords()