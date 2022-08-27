import os
from youtubesearchpython import VideosSearch
from django.shortcuts import render
from .search import searching_google
from .voice2 import voice_assistant
from .recordAudio import recording_audio
from .speech_recognition import api_conection


class list_url:

    def home(request):

        return render(request, 'index.html',)

    def trigger_onclick(request):
        # proceso de reconocimiento
        voice_command = virtual_assistant.init_command()
        print(voice_command)

        # return the match object
        if (voice_command != None):
            obj = searching_google()
            matchlist = obj.search(voice_command)
            return render(request, 'search_index.html', {'match_list': enumerate(matchlist)})

        return render(request, 'search_index.html', {'match_list': 'None'})

    def view_youtube(request):

        # proceso de reconocimiento
        voice_command = virtual_assistant.init_command()
        print(voice_command)

        if (voice_command != None):
            # return the match object
            videosSearch = VideosSearch(voice_command, limit=10)
            videoList = []
            valor = videosSearch.result()

            for i in valor['result']:
                videoList.append(i['id'])

            return render(request, 'view_youtube.html', {'match_list': videoList})

        # por defecto
        return render(request, 'view_youtube.html', {'match_list': 'None'})

    def view_list_of_files(request):
        files_match = os.listdir('/Users/Juan David Ruiz/OneDrive/Desktop')
        return render(request, 'files.html', {'match_list': enumerate(files_match)})


class virtual_assistant:

    def init_command():

        try:
            # llamo al asistente de voz y le paso los comandos que va a decir
            init_bot = assistant(
                ['Por favor diga en voz alta la busqueda que desea realizar'])
            init_bot.start_assistant()

            # grabo el audio que voy a procesar
            recording_audio.recording()

            try:

                respond = api_conection.speech_to_text()
                if respond != '':
                    return respond
                else:
                    init_bot = assistant(['Por Favor inténtalo de nuevo'])
                    init_bot.start_assistant()

            except IndexError:

                init_bot = assistant(['Por Favor inténtalo de nuevo'])
                init_bot.start_assistant()

        except:
            init_bot = assistant(
                ['Los auriculares y su micrófono no son compatibles con mi sistema, inténtalo nuevamente'])
            init_bot.start_assistant()

        # llamo la api de google
        # y valido que haya escuchado el evento

    def command_two():
        # llamo al asistente de voz y le paso los comandos que va a decir
        init_bot = assistant(
            ['Ahora te enseñaremos los primeros pasos para que logres controlar tu computadora de manera eficaz'])
        init_bot.start_assistant()


class assistant:

    command = ''

    def __init__(self, command):
        self.voice = command

    def start_assistant(self):
        for val in self.voice:
            speaking = voice_assistant(val)
            speaking.SpeakText()
