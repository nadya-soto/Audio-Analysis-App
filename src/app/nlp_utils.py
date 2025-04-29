#nlp_utils.py

import spacy

#load spacy
nlp = spacy.load("en_core_web_sm")

def get_pos_tags(text): 
    # process the text with the model 
    doc = nlp(text)
    return [(token.text, token.pos_) for token in doc]

def get_named_entities(text):
    # Procesar el texto con el modelo cargado
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]
