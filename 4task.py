# Install first: pip install SpeechRecognition PyAudio pyttsx3

import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
speaker = pyttsx3.init()

def speak(text):
    print("Bot:", text)
    speaker.say(text)
    speaker.runAndWait()

def chatbot():
    speak("Hello! I am your chatbot.")
    speak("You can talk to me. Say bye to exit.")

    while True:
        try:
            with sr.Microphone() as source:
                print("\nListening...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source)

            message = recognizer.recognize_google(audio).lower()
            print("You:", message)

            if message == "hello" or message == "hi":
                speak("Hello! Nice to meet you.")

            elif message == "how are you":
                speak("I am fine, thank you.")

            elif "your name" in message:
                speak("My name is PyBot.")

            elif "what can you do" in message:
                speak("I can have a simple conversation with you.")

            elif "good morning" in message:
                speak("Good morning!")

            elif "thank" in message:
                speak("You are welcome!")

            elif message == "bye":
                speak("Goodbye!")
                break

            else:
                speak("Sorry, I don't understand that.")

        except sr.UnknownValueError:
            speak("I could not understand your voice.")

        except sr.RequestError:
            speak("There is a problem with the speech service.")

        except Exception as e:
            print("Error:", e)

chatbot()