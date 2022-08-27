# asistente de voz
import pyttsx3


class voice_assistant:
    voice = ''
    lenguage = ''

    def __init__(self, command):
        self.voice = command
        self.lenguage = "sp_CO"

    def SpeakText(self):
        engine = pyttsx3.init()
        # getting details of current speaking rate
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 40)     # setting up new voice rate
        # getting details of current voice
        voices = engine.getProperty('voices')
        # changing index, changes voices. 1 for female
        engine.setProperty('voice', voices[2].id)
        engine.say(self.voice)
        engine.runAndWait()
        engine.stop()
