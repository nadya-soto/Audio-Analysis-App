# audio_utils.py
import os
import whisper
import sounddevice as sd
import scipy.io.wavfile as wav

# Configuración de ffmpeg (asegúrate que la ruta es correcta)
os.environ["PATH"] += os.pathsep + r"C:\Users\ethel\Downloads\ffmpeg\bin"

def transcribe_audio(file_path):
    """Convierte audio a texto usando Whisper"""
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result['text']

def record_audio(duration=5, fs=44100, output_file="temp_audio.wav"):
    """Graba audio desde el micrófono"""
    print("Grabando...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
    sd.wait()
    wav.write(output_file, fs, audio_data)
    return output_file