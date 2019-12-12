import torch
from nltk.util import ngrams
from collections import Counter
import configuration as config
import const

def getCommonGrams(words):
    groupings = [{}] * 3
    for word in words:
        for n in [1, 2, 3]:
            seg = word[-n:]
            currgrams = [''.join(x) for x in ngrams(seg, n)]
            for gram in currgrams:
                groupings[n-1][gram] = groupings[n-1][gram] + 1 if gram in groupings[n-1] else 1

    const.letters = [x.pop(0) for x in [list(y) for y in (Counter(groupings[0]).most_common(config.mono_sufnum))]]
    const.digrams = [x.pop(0) for x in [list(y) for y in (Counter(groupings[1]).most_common(config.di_sufnum))]]
    const.trigrams =[x.pop(0) for x in [list(y) for y in (Counter(groupings[2]).most_common(config.tri_sufnum))]]