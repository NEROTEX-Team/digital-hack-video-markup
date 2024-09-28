import speech_recognition as sr

def speech_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language='ru-RU')
    except sr.UnknownValueError:
        text = ""
    return text