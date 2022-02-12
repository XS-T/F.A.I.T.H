import speech_recognition as sr
from Windows import wmain as wm
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
    print("Say the wake worddddd")
    while True:
        try:
            ww = voice_cmds()
            if ww == "faith":
                print("You Said the wake word")
                wm.send_command()
                break
            else:
                print("Nope")
                pass
        except UnboundLocalError:
            pass