# import streamlit as st
# from googletrans import Translator
# import streamlit as st
# import time

# from CodeRunner import ENGLISH_TO_ALL_LOCAL
# # def translate_and_detect(query):
# #     translator = Translator()
# #     detected_language = translator.detect(query).lang
# #     translated_text = translator.translate(query).text
# #     response = f"Detected Language: {detected_language}\n Translated Text (English): {translated_text}"
# #     return response

# def AllToEnglish(text):
#     translator=Translator()
#     translated_text = translator.translate(text).text
#     response = translated_text
#     return response 

# def TranslateWords():
#     st.title("Language Translator App")
#      # Form setup
#     with st.form(key="form"):
#         user_input = st.text_input("Enter your message:")
#         submit_button = st.form_submit_button("Send")

#     if submit_button:
#         st.chat_message("user").write(user_input)
#         with st.chat_message("assistant"):
#             # result  = translate_and_detect(user_input)
#             text = AllToEnglish(user_input)
#             language = "Luganda"
#             res = ENGLISH_TO_ALL_LOCAL(language,text )
#             st.write(res)

# if __name__ == "__main__":
#     TranslateWords()
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
    st.title("Language Translator App")
    # List of supported languages for translation
    supported_languages = ["Luganda", "Runyankole", "Acholi", "Lugbara", "Ateso"]

    # Form setup
    with st.form(key="form"):
        user_input = st.text_input("Enter your message:")
        target_language = st.selectbox("Select target language:", supported_languages)
        submit_button = st.form_submit_button("Send")

    if submit_button:
        st.chat_message("user").write(user_input)
        with st.chat_message("assistant"):
            # Translate user input to English
            text = AllToEnglish(user_input)

            # Translate English text to the selected target language
            res = ENGLISH_TO_ALL_LOCAL(target_language, text)
            st.write(f"Translated text to {target_language}:")
            st.write(res)

if __name__ == "__main__":
    TranslateWords()
