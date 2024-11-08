import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

if __name__ == '__main__':
    print("Welcome to Robospeaker 1.1 created by Yash")
    while True:
        x = input("Enter what you want me to speak: ")
        if x.lower() == "q":
            # Make the engine say goodbye and exit
            engine.say("Bye bye my dear friend")
            engine.runAndWait()
            break
        # Make the engine say the entered text
        engine.say(x)
        engine.runAndWait()
