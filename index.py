import pyttsx3

def speak(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

if __name__ == '__main__':
    print("Welcome to RoboSpeaker")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "q":
            speak("bye bye friend")
            break
        speak(x)
