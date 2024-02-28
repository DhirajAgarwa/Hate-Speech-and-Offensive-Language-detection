import spacy
from nltk.corpus import stopwords
import re
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
    return lemmatized_text