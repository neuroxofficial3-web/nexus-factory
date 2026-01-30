from kivy.app import App
from kivy.uix.label import Label

class NexusApp(App):
    def build(self):
        return Label(text="Nexus AI System Online")

if __name__ == "__main__":
    NexusApp().run()
