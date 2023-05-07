import nltk
import string
from config import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer

from model.knowledgebase import Knowledge
from service.similarWordsService import *
from service.LocationService import *

nltk.download('punkt')
nltk.download('stopwords')

knowledgeWords = Knowledge()

allWords = knowledgeWords.getKnowledgeBaseWords();
allCity = knowledgeWords.ct()

stop = stopwords.words('english')
stop.pop(1)
stop.pop(1)
pun = list(string.punctuation)
stop = stop + pun

lancaster = LancasterStemmer()


def stemming(words):
    outputWords = []
    for w in words:
        outputWords.append(lancaster.stem(w))
    return outputWords


def similerCheck(words):
    # words = stemming(words)
    count = 0
    ans = []
    for i in words:
        maxRatio = 0
        temp = i
        for j in allWords:
            ratio = ratioOfSimilarity(i, j)
            if ratio > maxRatio:
                temp = j
                maxRatio = ratio
        if maxRatio >= 80:
            ans.append(temp)
            # count+=1
            # ans.append({temp,str(max)})
            # if temp in allCity:
            #     place = temp
            #     ans["place"] = fetch(place)

    return ans


def tokenize(sentence):
    words = word_tokenize(sentence)
    clean = [w for w in words if not w in stop]
    refine_words = similerCheck(clean)
    return refine_words
