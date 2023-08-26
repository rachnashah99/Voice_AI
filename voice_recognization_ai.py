#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser  # Import the webbrowser module

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize speech recognition
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""

def main():
    speak("Hello! How can I assist you?")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hi there!")
        elif "how are you" in command:
            speak("I'm just a computer program, but I'm here to help!")
        elif "what's the weather" in command:
            speak("The weather is sunny and warm.")
        elif "today's date" in command:
            today = datetime.datetime.now()
            date_str = today.strftime('%d %B %Y')
            speak(f"Today's date is {date_str}")
        elif "open youtube" in command:
            webbrowser.open("https://www.youtube.com/")
            speak("Opening YouTube.")
        elif "open google" in command:
            webbrowser.open("https://www.google.com/")
            speak("Opening Google.")
        elif "goodbye" in command:
            speak("Goodbye! Have a great day.")
            break
        else:
            speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




