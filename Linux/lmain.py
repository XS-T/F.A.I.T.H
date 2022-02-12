#!/usr/bin/python3
import speech_recognition as sr

def voice_cmds():
    #GET AUDIO FROM MIC
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Command: ")
        audio = r.listen(source)
        outpt = r.recognize_google(audio)

    #RECOGNIZE SPEECH
    try:
        print("F.A.I.T.H Thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("F.A.I.T.H Could Not Understand your audio")
    except sr.RequestError as e:
        print("Could not request Results; {0}".format(e))
    return outpt