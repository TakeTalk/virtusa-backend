from difflib import SequenceMatcher


def ratioOfSimilarity(word, target):
    ratio= SequenceMatcher(None, word, target).ratio()
    return ratio*100

