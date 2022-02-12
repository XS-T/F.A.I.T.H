#!/usr/bin/python3
import speech_recognition as sr
from Windows.commands import commands as cmds
import Windows.commands.wakeword as wk
import os

def voice_cmds():
    try:
        #GET AUDIO FROM MIC
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say Command")
            audio = r.listen(source,None,4)
            outpt = r.recognize_google(audio)
    except sr.UnknownValueError:
        wk.wake_word()
    except sr.RequestError:
        pass
    return outpt

def send_command():
    while True:
        try:
            outpt = voice_cmds()
            outpt2 = outpt.split(' ')
            print(outpt2)
            #cmds.cmds1(outpt=outpt)
            #cmds.cmds2(o=outpt)
            if "email" in outpt2:
                cmds.cmds1(outpt=outpt)
            elif "type" in outpt2:
                cmds.type(typ=outpt)
            elif "search" in outpt:
                cmds.search(url=outpt2)
            else:
                print("Nope ", + outpt)
        except UnboundLocalError:
            pass