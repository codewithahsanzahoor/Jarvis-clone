import speech_recognition as sr
import webbrowser

# Initialize the recognizer
recognizer = sr.Recognizer()


def listen_for_wake_word():
    """
    Listens for the wake word "Jarvis".
    """
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for wake word...")
        audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=5)

        try:
            print("Recognizing wake word...")
            text = recognizer.recognize_google(audio_data).lower()
            print(f"Heard: {text}")
            if "jarvis" in text:
                return True
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

    return False


def listen_for_command():
    """
    Listens for a command after the wake word is detected.
    """
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=5)

        try:
            print("Recognizing command...")
            command = recognizer.recognize_google(audio_data).lower()
            print(f"Command: {command}")
            return command
        except sr.UnknownValueError:
            print("Could not understand the command.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

    return ""


def perform_action(command):
    """
    Performs an action based on the recognized command.
    """
    if "open google" in command:
        webbrowser.open("http://www.google.com")
        print("Opening Google...")
    if "open youtube" in command:
        webbrowser.open("http://www.youtube.com")
        print("Opening Google...")
    # Add more commands and actions as needed
    else:
        print("Command not recognized.")


if __name__ == "__main__":
    while True:
        # Continuously listen for the wake word
        if listen_for_wake_word():
            print("Wake word detected!")
            command = listen_for_command()
            perform_action(command)
