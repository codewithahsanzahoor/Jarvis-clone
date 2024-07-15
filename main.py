import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to capture and recognize speech


def recognize_speech_from_mic():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio_data = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio_data)
            print(f"Recognized Text: {text}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")


if __name__ == "__main__":
    while True:
        recognize_speech_from_mic()
