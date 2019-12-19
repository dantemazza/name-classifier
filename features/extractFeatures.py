import torch
import numpy as np
import const


def extractFeatures(set):
    X = np.zeros(shape=(len(set), const.featureCount))
    y = np.zeros(len(set))

    for i, name in enumerate(set):
        fn = 0
        for letter in const.last_letters:
            X[i][fn] = 1 if name[-1] == letter else 0
            fn += 1
        for gram in const.bigrams + const.trigrams:
            X[i][fn] = 1 if gram in name else 0
            fn += 1
        for difix in const.di_suffix:
            X[i][fn] = 1 if name[-2:] == difix else 0
            fn += 1
        for trifix in const.tri_suffix:
            X[i][fn] = 1 if name[-3:] == trifix else 0
            fn += 1

        y[i] = set[name]

    return X, y





