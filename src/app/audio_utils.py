# audio_utils.py
import speech_recognition as sr
from pydub import AudioSegment
import tempfile

def transcribe_audio(file):
    recognizer = sr.Recognizer()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        sound = AudioSegment.from_file(file)
        sound.export(temp_audio.name, format="wav")

        with sr.AudioFile(temp_audio.name) as source:
            audio = recognizer.record(source)

        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "No se pudo entender el audio."
        except sr.RequestError as e:
            return f"Error del servicio de reconocimiento: {e}"
