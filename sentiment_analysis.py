import spacy
import pandas as pd
from spacytextblob.spacytextblob import SpacyTextBlob

dataframe = pd.read_csv('amazon_product_reviews.csv')
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

clean_data = dataframe.dropna(subset=['reviews.text']) # removing all missing values
reviews_data = clean_data['reviews.text']

def process_review(review): # we remove punctuation, spaces and stop words
    doc = nlp(review)
    token_list =    filtered_tokens = [token.orth_ for token in doc if not token.is_punct and not token.is_space and not token.is_stop]
    new_string = " ".join(token_list) # join the remaining tokens together to create a string
    return new_string

def review_sentiment(review): # returns polarity
    doc = nlp(process_review(review))
    polarity = doc._.blob.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

for review in reviews_data.sample(10): # testing on some sample reviews
    print(f"Review : {review}")
    print(f"Sentiment: {review_sentiment(review)}")