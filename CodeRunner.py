import requests
import os
from dotenv import find_dotenv, load_dotenv
# import torchaudio
# from speechbrain.pretrained import Tacotron2, HIFIGAN
import streamlit as st
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
# SUNBIRD_MUL_EN_URL = os.getenv("SUNBIRD_MUL_EN_URL")
# HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
# SUNBIRD_EN_LUGA_URL = os.getenv("SUNBIRD_EN_LUGA_URL")
# SUNBIRD_ALL_LOCAL_TO_ENG = os.getenv("SUNBIRD_ALL_LOCAL_TO_ENG")
# SUNBIRD_ACCESSTOKEN = os.getenv("SUNBIRD_ACCESSTOKEN")

SUNBIRD_MUL_EN_URL = st.secrets("SUNBIRD_MUL_EN_URL")
HUGGINGFACE_API_KEY = st.secrets("HUGGINGFACE_API_KEY")
SUNBIRD_EN_LUGA_URL = st.secrets("SUNBIRD_EN_LUGA_URL")
SUNBIRD_ALL_LOCAL_TO_ENG = st.secrets("SUNBIRD_ALL_LOCAL_TO_ENG")
SUNBIRD_ACCESSTOKEN = st.secrets("SUNBIRD_ACCESSTOKEN")
ENGLISH_TO_ALL_LOCAL_URL = st.secrets("ENGLISH_TO_ALL_LOCAL_URL")

def LocaLToEnglish(query):
    API_URL = SUNBIRD_MUL_EN_URL
    headers = {"Authorization": HUGGINGFACE_API_KEY}

    payload = {"inputs": query}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# def EnglishToLuganda(query):
#     API_URL = SUNBIRD_EN_LUGA_URL
#     headers = {"Authorization": HUGGINGFACE_API_KEY}

#     payload = {"inputs": query}
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()

def ALL_LOCAL_TO_ENG(input_text):
    
    API_URL = SUNBIRD_ALL_LOCAL_TO_ENG
    headers = {"Authorization": HUGGINGFACE_API_KEY}

    payload = {"inputs": input_text}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def ENGLISH_TO_ALL_LOCAL(target_language, text):
    
    access_token = SUNBIRD_ACCESSTOKEN
    url = ENGLISH_TO_ALL_LOCAL_URL

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "source_language": "English",
        "target_language": target_language,
        "text": text
    }

    response = requests.post(f"{url}/tasks/translate", headers=headers, json=payload)

    if response.status_code == 200:
        translated_text = response.json()["text"]
        return translated_text
    else:
        return f"Error: {response.status_code}, {response.text}"
# en = "This page describes how to use the Sunbird AI API and includes code samples in Python."
# resp = translate_text("Runyankole", en)
# print(resp)

