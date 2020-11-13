import webbrowser

from Action import Action


class ActionOpenPage(Action):
    @staticmethod
    def act(item):
        webbrowser.open(item.url)
