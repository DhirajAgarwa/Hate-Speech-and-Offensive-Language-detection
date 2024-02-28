import pandas as pd
import numpy as np
import spacy
from nltk.corpus import stopwords
import re

# to remve empty data
def delete_dat():
    df=pd.read_csv('dataset_hate_speech.csv')
    df=df.dropna(subset=['tweet'],how='any')

# to shuffle the data 
def shuffling():
    X=pd.read_csv('dataset_hate_speech.csv')
    X=X.sample(frac=1).reset_index(drop=True)
    X.to_csv('dataset_hate_speech.csv',index=False)

# to remove extra spaces and lowering some words
def extra_spaces_lower():
    X=pd.read_csv('dataset_hate_speech.csv')
    X['tweet']=X['tweet'].str.replace(r'^\s+','',regex=True)
    X['tweet']=X['tweet'].str.lower()
    X.to_csv('create.csv')

# program to clean data 
def words_lemm(text):

    text = re.sub(r'@\w+|http\S+|RT|\d+|[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    
    # Load spacy English models
    nlp = spacy.load('en_core_web_sm')
    
    # Tokenize and lemmatize using spaCy
    doc = nlp(text)
    lemmatized_tokens = [token.lemma_ for token in doc if token.text.lower() not in stopwords.words('english')]
    
    # Join the lemmatized tokens into a string
    lemmatized_text = ' '.join(lemmatized_tokens)
    print(lemmatized_text)
    return lemmatized_text


def data_reduce():
    x=pd.read_csv("dataset_hate_speech")# if editing labeled data put labeled data as file please
    df_c1=x[x['class']==1].head(8000)
    x.drop(index=np.where(x['class']==1)[0],axis=0,inplace=True) # type: ignore
    X=pd.concat([df_c1,x], axis=0, ignore_index=True)
    X['tweet']=X['tweet'].apply(lambda y: words_lemm(y))
    X.to_csv('dataset_hate_speech')


