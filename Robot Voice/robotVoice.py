import speech_recognition as sr
from gtts import gTTS
import os
voice = ""
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)
            if text == "chup":
                break
            text = r.recognize_google(audio)
            voice = voice+str(text)
        except:
            print("Bujina")
hr = gTTS(text=voice, lang="en", slow=False)
hr.save("1.mp3")
