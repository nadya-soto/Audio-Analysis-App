# ui.py
import streamlit as st
import os
from pathlib import Path
import sys


sys.path.append(str(Path(__file__).parent.parent))

# Intentar importar los módulos desde diferentes ubicaciones
try:
    from app.audio_utils import transcribe_audio
    from app.nlp_utils import get_pos_tags
    #from app.classifier import train_model, predict_category
    from app.keywords import extract_keywords
    from app.sentiment import analyze_sentiment
except ImportError:
    from audio_utils import transcribe_audio
    from nlp_utils import get_pos_tags, get_named_entities
    #from classifier import train_model, predict_category
    from keywords import extract_keywords
    from sentiment import analyze_sentiment


def run_app():
    st.title("AI Assistant")

    st.markdown("### Upload audio file" )

    # Widget para subir archivo de audio
    upload_file = st.file_uploader(
        "Upload an audio file (.mp3 or .wav)", 
        type=["mp3", "wav"],
        help="Maximum file size: 10MB"
    )

    if upload_file:
        os.makedirs("temp", exist_ok=True)
        temp_path = os.path.join("temp", "uploaded_audio.wav")

        try:
            #  save the temp 
            with open(temp_path, "wb") as f:
                f.write(upload_file.getbuffer())

            with st.spinner("Processing audio..."):
                # Transcription
                text = transcribe_audio(temp_path)
                
                #Pos tagg
                pos_tag =get_pos_tags(text)
                #count Pos Freq
                from collections import Counter
                
                nouns = [word for word, pos in pos_tag if pos == "NOUN" ]
                verbs = [word for word, pos in pos_tag if pos == "VERB" ]
                adjectives = [word for word, pos in pos_tag if pos == "ADJ" ]
                
                top_nouns = Counter(nouns).most_common(3)
                top_verbs = Counter(verbs).most_common(3)
                top_adjectives = Counter(adjectives).most_common(3)
                
                #display in two columns 
                col1, col2 = st.columns(2)
                
                with col1:
                    st.text_area('Text from transcript displayed here... ', text, height = 300)
                with col2:
                    st.markdown("The most frequent 3 nouns:")
                    for word, _ in top_nouns:
                        st.write('-', word)
                    
                    st.markdown("The most frequent 3 verbs:")
                    for word, _ in top_verbs:
                        st.write('-',word)
                        
                    st.markdown("The most frequent 3 adjectives:")
                    for word, _ in top_adjectives:
                        st.write('-',word)
      

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
        
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

