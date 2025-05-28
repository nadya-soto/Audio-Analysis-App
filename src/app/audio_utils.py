# audio_utils.py
import os
import whisper
import tempfile

# Asegúrate de que ffmpeg esté instalado si usas formatos distintos a WAV
# En Streamlit Cloud suele estar preinstalado

# Carga el modelo una vez
model = whisper.load_model("base")

def transcribe_audio(file):
    """Convierte audio subido a texto usando Whisper"""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(file.read())
        tmp_path = tmp.name

    result = model.transcribe(tmp_path)
    os.remove(tmp_path)
    return result['text']
