import nltk
import string
from config import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer

from model.knowledgebase import Knowledge
from service.similarWordsService import *

nltk.download('punkt')
nltk.download('stopwords')

knowledgeWords = Knowledge()

allWords = knowledgeWords.getKnowledgeBaseWords();


stop = stopwords.words('english')
pun = list(string.punctuation)
stop = stop + pun

lancaster = LancasterStemmer()



def stemming(words):
    outputWords = []
    for w in words:
        outputWords.append(lancaster.stem(w))
    return outputWords

def similerCheck(words):
    words = stemming(words)
    ans = []
    for i in words:
        max = 0
        temp = i
        for j in allWords:
            ratio = ratioOfSimilarity(i,j)
            if(ratio>max):
                temp = j
                max = ratio
        if(max>80):
            # ans.append({temp,str(max)})
            ans.append(temp)
    return ans

def tokenize(sentence):
    words = word_tokenize(sentence)
    clean = [w for w in words if not w in stop]
    refine_words = similerCheck(clean)
    return refine_words

