import socket
import os
import speech_recognition as sr
import string
from pynput.keyboard import Key, Controller
from time import sleep as sl
import pyautogui as pyg
import webbrowser as web

def cmds1(outpt):
    if outpt == outpt:
        L = outpt.lower().split("email")
        S = L.pop(1)
        D = S.replace(" ", '')
        print(D)
    else:
        pass


def cmds2(o):
    if o == "reverse shell":
        print("Hi")


def email(eml):
    ale = ["xavierrichardson"]
    if eml in ale:
        L = eml.lower().split("email")
        S = L.pop(1)
        D = S.replace(" ", '')
        print(D)


def type(typ):
    if "type" in typ:
        T = typ.lower().split("type")
        T.append('/g')
        print(T)
        Y = T.pop(2)
        print(T)
        S = T.pop(1)
        keyboard = Controller()
        sl(2)
        pyg.typewrite(Y + S + "A.I Known as F.A.I.T.H", interval=0.25)
        keyboard.press(Key.enter)


def search(url):
    print(url)