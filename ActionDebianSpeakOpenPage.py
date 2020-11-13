import webbrowser
import pyttsx3 as pyttsx3

from Action import Action


class ActionDebianSpeakOpenPage(Action):
    @staticmethod
    def act(item):
        webbrowser.open(item.url)

        engine = pyttsx3.init()
        engine.say("It's there!")
        engine.runAndWait()
