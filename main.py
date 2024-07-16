import speech_recognition as sr
import webbrowser
import pyttsx3
import requests

# Initialize the recognizer
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# news api
NEWS_API_KEY = "209981397982442497a8d87bbfa5363f"


def speak(text):
    """
    Converts text to speech.
    """
    engine.say(text)
    engine.runAndWait()


# Initialize the music dictionary for jarvis to play.
music = {
    "workout": "https://www.youtube.com/watch?v=LVbUNRwpXzw&t=900s",

}


def listen_for_wake_word():
    """
    Listens for the wake word "Jarvis".
    """
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")

        try:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for wake word...")
            audio_data = recognizer.listen(
                source, timeout=10, phrase_time_limit=5)
            print("Recognizing wake word...")
            text = recognizer.recognize_google(audio_data).lower()
            print(f"Heard: {text}")
            if "jarvis" in text:

                return True
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    return False


def listen_for_command():
    """
    Listens for a command after the wake word is detected.
    """
    with sr.Microphone() as source:
        print("Listening for a command...")

        try:
            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.listen(
                source, timeout=10, phrase_time_limit=5)
            print("Recognizing command...")
            command = recognizer.recognize_google(audio_data).lower()
            print(f"Command: {command}")
            return command
        except sr.UnknownValueError:
            print("Could not understand the command.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    return ""


def get_latest_news():
    """
    Fetches the latest news using the News API.
    """
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={
        NEWS_API_KEY}"
    response = requests.get(url)
    news_data = response.json()

    if news_data['status'] == 'ok':
        articles = news_data['articles'][:5]  # Get the top 5 news articles
        news_list = [article['title'] for article in articles]
        return news_list
    else:
        return ["Failed to fetch news"]


def perform_action(command):
    """
    Performs an action based on the recognized command.
    """
    if "open google" in command:
        webbrowser.open("http://www.google.com")
        print("Opening Google...")
        speak("opening google")
    elif "open youtube" in command:
        webbrowser.open("http://www.youtube.com")
        print("Opening Google...")
        speak("opening youtube")
    elif command.lower().split(" ")[0] == "play":
        song = command.lower().split(" ")[1]
        webbrowser.open(music[song])
        speak(f"playing {song}")
    elif "news" in command:
        news_list = get_latest_news()
        for news in news_list:
            speak(news)
            # print(news)
    else:
        print("Command not recognized.")


if __name__ == "__main__":
    while True:
        # Continuously listen for the wake word
        if listen_for_wake_word():
            print("Wake word detected!")
            speak("Yes Master, how can i help you?")
            command = listen_for_command()
            perform_action(command)
