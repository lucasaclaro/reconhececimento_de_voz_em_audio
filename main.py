import speech_recognition as sr

rec = sr.Recognizer()



arquivo_audio =  r"audio_teste.wav"

r = sr.Recognizer()
with sr.AudioFile(arquivo_audio) as source:
    audio = r.record(source)
    print(r.recognize_google(audio, language="pt-BR"))
