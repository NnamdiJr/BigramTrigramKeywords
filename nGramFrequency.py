#__author__ = 'User'
#!/usr/bin/env python

#  Author: Nnamdi Offor
#  Date: 5/14/2014
#
#  Script using NLTK to find unigram, bigram, and trigram keywords
#  from group of texts files existing in directory. Minimum frequency adjustable.
# *************************************** #

import nltk, os
from nltk.tokenize import RegexpTokenizer
from nltk.collocations import *

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

BiTriList = []

keywordList = []
conj = ["at", "an", "on", "and", "but", "or", "a", "the", "of", "in", "by", "to", "is", "it", "if", "so", "be", "can",
        "are", "will", "for", "as", "do", "which", "were", "with", "who", "also", "may", "not", "edit", "than", "that",
        "then", "they", "this"]

resultsFile = open("results.txt", 'w')

#returns list of n top bigrams containing keyword from array
def unigramFilter(stuff):
    fdist = nltk.FreqDist(stuff)
    for token in fdist.items():
        if token[1] >= 3 and token[0] not in conj and len(token[0]) > 1:
            keywordList.append(token[0])
        else:
            continue

#returns list of n top bigrams containing keyword from array
def bigramFilter(stuff):
    for word in stuff:
        finder = BigramCollocationFinder.from_words(tokens)
        finder.apply_ngram_filter(lambda w1, w2: word not in (w1, w2))
        result = finder.above_score(bigram_measures.pmi, 3)
        for item in result:
            if item[0] in conj or item[1] in conj:
                continue
            else:
                BiTriList.append(item)

#returns list of n top trigrams containing keyword from array
def trigramFilter(stuff):
    for word in stuff:
        finder = TrigramCollocationFinder.from_words(tokens)
        finder.apply_ngram_filter(lambda w1, w2, w3: word not in (w1, w2, w3))
        result = finder.above_score(trigram_measures.pmi, 3)
    for item in result:
        if item[0] in conj or item[1] in conj or item[2] in conj:
            continue
        else:
            BiTriList.append(item)

path = "C:\Users\..." #your directory path

for filename in os.listdir(path):
    textFile = path + filename
    n = open(textFile)
    text = n.read().decode('ascii', 'ignore').encode('ascii')
    tokenizer = RegexpTokenizer('[A-Za-z]+')
    tokens = tokenizer.tokenize(text.lower())
    unigramFilter(tokens)
    bigramFilter(keywordList)
    trigramFilter(keywordList)

for element in keywordList:
    resultsFile.write(element + "\n")

for element in BiTriList:
    s = list(element)
    if not element:
        continue
    elif len(s) is 3:
        resultsFile.write(s[0] + " " + s[1] + " " + s[2] + "\n")
    else:
        resultsFile.write(s[0] + " " + s[1] + "\n")