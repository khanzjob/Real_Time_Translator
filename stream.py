# import speech_recognition as sr

# # Initialize the recognizer
# recognizer = sr.Recognizer()

# # Use the microphone as the audio source
# with sr.Microphone() as source:
#     print("Say something:")
#     recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise

#     while True:
#         try:
#             audio = recognizer.listen(source, phrase_time_limit=7)  # Listen for up to 5 seconds of speech
#             text = recognizer.recognize_google(audio, show_all=False)  # Use Google Web Speech API
#             if text:
#                 print("You said:", text)
#         except sr.WaitTimeoutError:
#             print("Listening timed out. Say something:")
#         except sr.UnknownValueError:
#             print("Could not understand audio. Try again:")

# # This code captures and recognizes speech in real-time until you manually stop the script.

import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Say something:")
    recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise with a 1-second sample

    recognized_text = ""
    while True:
        try:
            audio = recognizer.listen(source, phrase_time_limit=5)  # Listen for up to 5 seconds of speech
            text = recognizer.recognize_google(audio, show_all=False)  # Use Google Web Speech API
            if text:
                recognized_text += " " + text  # Append the recognized text
                print("You said:", text)
        except sr.WaitTimeoutError:
            print("Listening timed out. Say something:")
        except sr.UnknownValueError:
            print("Could not understand audio. Try again:")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

# After you stop speaking, you can access the full recognized text.
print("Full Recognized Text:", recognized_text)

