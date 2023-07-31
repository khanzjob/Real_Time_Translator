import requests
import os
from dotenv import find_dotenv, load_dotenv
# import torchaudio
# from speechbrain.pretrained import Tacotron2, HIFIGAN

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
SUNBIRD_MUL_EN_URL = os.getenv("SUNBIRD_MUL_EN_URL")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
SUNBIRD_EN_LUGA_URL = os.getenv("SUNBIRD_EN_LUGA_URL")
SUNBIRD_ALL_LOCAL_TO_ENG = os.getenv("SUNBIRD_ALL_LOCAL_TO_ENG")
SUNBIRD_ACCESSTOKEN = os.getenv("SUNBIRD_ACCESSTOKEN")

def LocaLToEnglish(query):
    API_URL = SUNBIRD_MUL_EN_URL
    headers = {"Authorization": HUGGINGFACE_API_KEY}

    payload = {"inputs": query}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def EnglishToLuganda(query):
    API_URL = SUNBIRD_EN_LUGA_URL
    headers = {"Authorization": HUGGINGFACE_API_KEY}

    payload = {"inputs": query}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()



# def LugandaTTS(input_text, output_file="example_TTS.wav"):
#     # Intialize TTS (Tacotron2) and Vocoder (HiFIGAN)
#     tacotron2 = Tacotron2.from_hparams(source="/Sunbird/sunbird-lug-tts", savedir="tmpdir_tts")
#     hifi_gan = HIFIGAN.from_hparams(source="speechbrain/tts-hifigan-ljspeech", savedir="tmpdir_vocoder")

#     # Running the TTS
#     mel_output, mel_length, alignment = tacotron2.encode_text(input_text)

#     # Running Vocoder (spectrogram-to-waveform)
#     waveforms = hifi_gan.decode_batch(mel_output)

#     # Save the waveform as a WAV file
#     torchaudio.save(output_file, waveforms.squeeze(1), 22050)

# # Example usage:
# input_text = "Mbagaliza Christmass Enungi Nomwaka Omugya Gubaberere Gwamirembe"
# LugandaTTS(input_text, output_file="example_TTS.wav")


def ALL_LOCAL_TO_ENG(input_text):
    
    API_URL = SUNBIRD_ALL_LOCAL_TO_ENG
    headers = {"Authorization": HUGGINGFACE_API_KEY}

    payload = {"inputs": input_text}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# luga = "Yagobwa ku mulimu mu kifo kye ne bazzaawo omuwandiisi we.Buli omu alina okusasula omusolo."
# output = ALL_LOCAL_TO_ENG(luga)
# print(output)

# runyankole= "Omukazi we n'omucureezi. Eka niyo ntandikwa y'ekyaro."
# output = ALL_LOCAL_TO_ENG(runyankole)
# print(output)
# lugbara= "Le ama ma esu geri e'yo aza kozu 'diyi ra. Le ama ma esu geri e'yo aza kozu 'diyi ra."
# output = ALL_LOCAL_TO_ENG(lugbara)
# print(output)
# ateso= "Mam aokot nuka itunga eraasi nueminasi isiru bon Etopolorit aiwo ke aipuc ka amina nejaas itunga lu atutubet."
# output = ALL_LOCAL_TO_ENG(ateso)
# print(output)
# acholi = "Dano weng myero ocul mucoro.Anyira mapol gi onyo ic i wii alii"
# output = ALL_LOCAL_TO_ENG(acholi)
# print(output)


def translate_text(target_language, text):
    
    access_token = SUNBIRD_ACCESSTOKEN
    url = 'https://sunbird-ai-api-5bq6okiwgq-ew.a.run.app'

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
en = "This page describes how to use the Sunbird AI API and includes code samples in Python."
resp = translate_text("Runyankole", en)
print(resp)

