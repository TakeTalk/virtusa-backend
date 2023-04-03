import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer

from model.knowledgebase import Knowledge

nltk.download('punkt')
nltk.download('stopwords')

knowledgeWords = Knowledge()

allWords = knowledgeWords.getKnowledgeBaseWords();

stop = stopwords.words('english')
pun = list(string.punctuation)
stop = stop + pun

lancaster = LancasterStemmer()


# sentence= input()

def stemming(words):
    outputWords = []
    for w in words:
        outputWords.append(lancaster.stem(w))
    return outputWords


def tokenize(sentence):
    words = word_tokenize(sentence)
    # stemmingWords=stemming(words)
    clean = [w for w in words if not w in stop]
    refine_words = [f for f in clean if f in allWords]
    return refine_words
