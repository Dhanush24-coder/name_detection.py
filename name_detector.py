import speech_recognition as sr

def detect_name(target_name="John"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for name...")
        audio = recognizer.listen(source)
    try:
        speech = recognizer.recognize_google(audio)
        print(f"Heard: {speech}")
        if target_name.lower() in speech.lower():
            print(f"{target_name} detected!")
            # Trigger vibration feedback here
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError:
        print("Could not request results")

detect_name()
