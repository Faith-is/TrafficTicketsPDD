from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class TrafficTicketsPDD(MDApp):
    def build(self):
        return MDLabel(text="Привет, мой первый пользователь", halign="center")


TrafficTicketsPDD().run()