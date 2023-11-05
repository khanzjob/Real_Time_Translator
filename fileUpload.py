import streamlit as st
import os
import easyocr
from datetime import datetime

from Translate import AudioTranslate


def uploadFile():
    supported_languages = ["Luganda", "Runyankole", "Acholi", "Lugbara", "Ateso"]
    st.write("Select image to transalte preferably A document Image")
    target_language = st.selectbox("Select target language:", supported_languages)

    uploaded_file = st.file_uploader("Choose File to transalte", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded document image .", use_column_width=True)
        st.write("Recognizing text from the image...")
        recognized_text, response = process_uploaded_image(uploaded_file,target_language)
        
        if response:
            st.chat_message("user").write(recognized_text)
            
            with st.chat_message("assistant"):
                        st.write(response)

def process_uploaded_image(uploaded_file,target_language):
    try:
        # Convert the uploaded file to bytes
        image_bytes = uploaded_file.read()
        reader = easyocr.Reader(['en'],gpu=True)
        result = reader.readtext(image_bytes, detail=0, paragraph=True)
        if not result:
            return "No text recognized. Please upload another image.", None
        
        result_str = ' '.join(result)
       
        transaltedLang =  AudioTranslate(result_str,target_language)

     # Saving the output to a .txt file
        now = datetime.now()
        filename = now.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
        directory = './output/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        output_path = os.path.join(directory, filename)
        
        with open(output_path, 'w') as file:
            file.write("Recognized Text:\n")
            file.write(result_str)
            file.write("\n\nResponse Text:\n")
            file.write(transaltedLang)
        
        print(f"Output saved in {output_path}")
        
        return result_str, transaltedLang
    except Exception as e:
        return f"An error occurred: {str(e)}", None