import pyaudio
import wave
from .voice2 import voice_assistant

class play_audio_assistment:
	def assistant(valor):
		arrWords=['Iniciando grabación','Grabación finalizada']

		voice = voice_assistant(arrWords[valor])
		voice.SpeakText()

		return voice


class recording_audio:

	def recording():

		duracion=3
		archivo="audio.wav"

		audio=pyaudio.PyAudio()

		stream=audio.open(format=pyaudio.paInt16,channels=2,rate=44100,input=True,frames_per_buffer=1024)
		frames=[]

		play_audio_assistment.assistant(0)

		for i in range(0,int(44100/1024*duracion)):
			data=stream.read(1024)
			frames.append(data)

		play_audio_assistment.assistant(1)			

		stream.stop_stream()
		stream.close()
		audio.terminate()

		waveFile=wave.open(archivo,'wb')
		waveFile.setnchannels(2)
		waveFile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
		waveFile.setframerate(44100)
		waveFile.writeframes(b''.join(frames))
		waveFile.close()