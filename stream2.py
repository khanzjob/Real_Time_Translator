import streamlit as st
import speech_recognition as sr

def main():
    st.title("Real-Time Speech Recognition")

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.write("Say something:")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        recognized_text = ""
        stop_recognition = False

        while not stop_recognition:
            try:
                audio = recognizer.listen(source, phrase_time_limit=5)
                text = recognizer.recognize_google(audio, show_all=False)
                if text:
                    recognized_text += " " + text
                    st.write(f"You said: {text}")
            except sr.WaitTimeoutError:
                st.warning("Listening timed out. Say something:")
            except sr.UnknownValueError:
                st.warning("Could not understand audio. Try again:")

            stop_recognition = st.button("Stop Recognition")

        st.success("Speech recognition stopped.")
        st.subheader("Full Recognized Text:")
        st.write(recognized_text)

if __name__ == "__main__":
    main()
