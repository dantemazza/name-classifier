from nltk.util import ngrams
from collections import Counter
import configuration as config
import const

def getCommonNgrams(words):
    groupings = [{}, {}]
    for word in words:
        for n in [2, 3]:
            seg = word[-n:]
            currgrams = [''.join(x) for x in ngrams(seg, n)]
            for gram in currgrams:
                groupings[n-2][gram] = groupings[n-2][gram] + 1 if gram in groupings[n-2] else 1

    const.digrams = [x.pop(0) for x in [list(y) for y in (Counter(groupings[0]).most_common(config.di_sufnum))]]
    const.trigrams =[x.pop(0) for x in [list(y) for y in (Counter(groupings[1]).most_common(config.tri_sufnum))]]