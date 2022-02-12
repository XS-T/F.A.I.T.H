#!/usr/bin/python3
import speech_recognition as sr
import platform as pl
from Windows import wmain as wm


def platform_check():
    if pl.system() == "Windows":
        wm.send_command()


def voice_cmds():
    while True:
        try:
            # GET AUDIO FROM MIC
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source, None, 3)
                outpt = r.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        return outpt


def wake_word():
    print("Say the wake word to Wake the AI")
    while True:
        try:
            ww = voice_cmds()
            if ww == "faith":
                print("You Said the wake word", ww)
                platform_check()
                break
            elif ww == "Jay":
                print("You said the wake word", ww)
                platform_check()
                break
            else:
                print("Nope", ww)
                pass
        except UnboundLocalError:
            pass


wake_word()
