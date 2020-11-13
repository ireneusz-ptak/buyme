import webbrowser
import pyttsx3 as pyttsx3
from pushover import Client

from Action import Action


class ActionDebianSpeakOpenPagePushover(Action):
    @staticmethod
    def act(item):
        webbrowser.open(item.url)

        engine = pyttsx3.init()
        engine.say("It's there!")
        engine.runAndWait()

        client = Client("<PUSHOVER CLIENT API>", api_token="<API TOKEN>")
        client.send_message(item.url, title=item.name + ": " + item.price)
