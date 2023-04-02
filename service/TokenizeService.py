import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

from service.cityNameService import *

stop =stopwords.words('english')
pun = list(string.punctuation)
stop = stop+pun


#sentence= input()


def tokenize(sentence):
    words =word_tokenize(sentence)
    clean = [w for w in words if not w in stop]
    refine_words= [f for f in clean if f in knowledge_test]
    return refine_words



