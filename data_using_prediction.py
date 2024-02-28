import joblib
import pandas as pd
from text_cleaning import words_lemm
def trial(text):
    text[0]=words_lemm(text[0])
    loaded=joblib.load('hate_speech_model.joblib')
    pred=loaded.predict(text)
    return pred[0]