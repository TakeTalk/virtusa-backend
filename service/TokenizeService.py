import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

stop =stopwords.words('english')
pun = list(string.punctuation)
stop = stop+pun
my_prefe =['hospital', 'area','nearby','cardiology','suggest','doctor']

#sentence= input()


def tokenize(sentence):
    words =word_tokenize(sentence)
    clean = [w for w in words if not w in stop]
    refine_words= [f for f in clean if f in my_prefe]
    return refine_words
#print(tokenize(sentence))



