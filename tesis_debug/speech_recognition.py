import os
# Imports the Google Cloud client library
from google.cloud import speech


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './tesis_debug/amiable-catfish-334518-706669a3a2c9.json'

client = speech.SpeechClient()


class api_conection:
    def speech_to_text():

        # Instantiates a client

        # The name of the audio file to transcribe
        media_file_name_wav = './audio.wav'

        with open(media_file_name_wav, 'rb') as f1:
            byte_data_wav = f1.read()
        audio_wav = speech.RecognitionAudio(content=byte_data_wav)

        # configure media files output
        config_wav = speech.RecognitionConfig(
            sample_rate_hertz=44100,
            enable_automatic_punctuation=True,
            language_code='es-ES',
            audio_channel_count=2
        )

        response_standard_wav = client.recognize(
            config=config_wav,
            audio=audio_wav
        )

        command = response_standard_wav.results[0].alternatives[0].transcript

        return command
