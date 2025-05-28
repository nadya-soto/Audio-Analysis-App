

# Audio Analysis App 

This is a Natural Language Processing (NLP) and Machine Learning (ML) powered Streamlit application that analyzes speech from uploaded audio files.

## Features

* **Speech-to-text transcription** using OpenAI Whisper
* **Text classification** into categories (e.g. housing, legal, financial)
* **Sentiment analysis** (polarity and subjectivity)
* **Keyword extraction** using TF-IDF
* **Named Entity Recognition (NER)** with spaCy
* **Part-of-Speech analysis** for extracting top nouns, verbs, and adjectives

---

## Technologies Used

* Python 3.12
* [Whisper](https://github.com/openai/whisper) (speech recognition)
* Streamlit (web app interface)
* spaCy (`en_core_web_sm`) for NLP tasks
* TextBlob for sentiment analysis
* scikit-learn for ML model (Naive Bayes classifier)
* TF-IDF for keyword extraction

---

##  How to Run It Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/audio-nlp-app.git
cd audio-nlp-app
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Launch the app

```bash
streamlit run src/main.py
```

---

## Project Structure

```
.
├── app/
│   ├── audio_utils.py         # Transcription and recording utilities
│   ├── classifier.py          # Text classification model
│   ├── keywords.py            # Keyword extraction logic
│   ├── nlp_utils.py           # POS and NER functions
│   ├── sentiment.py           # Sentiment analysis functions
│   └── ui.py                  # Streamlit interface
├── src/
│   └── main.py                # App entry point
├── requirements.txt
└── README.md
```

---

## Example Use Case

1. Upload a `.wav` or `.mp3` file with spoken content.
2. The system will:

   * Transcribe it to text
   * Classify the topic
   * Analyze sentiment
   * Highlight named entities and key words
   * Extract frequent nouns, verbs, and adjectives

---

## Notes

* Audio files must be under **10MB**.
* `ffmpeg` must be installed and added to your system PATH for audio processing.
  [Download ffmpeg here](https://ffmpeg.org/download.html).



#run in the terminal
#pip install -r requirements.txt
#python -m spacy download en_core_web_sm
#Lanza la app 
# exit
# pip install -r requirements.txt
# python -m spacy download en_core_web_sm
# y luego corre la app 
# streamlit run src\main.py