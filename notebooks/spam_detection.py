import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
data = pd.read_csv("../dataset/train.csv")
print(data.head())
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = word_tokenize(text)
    words = [word for word in words if word not in stopwords.words('english')]  
    return words
data["clean_sms"] = data["sms"].apply(clean_text)
print("\nCleaned Messages:")
print(data[["sms", "clean_sms"]].head())