import const
import data
from functions import *
from classifier.grams import *
import configuration as config
import numpy as np
from classifier.features import *

#extract the data from csv
const.M_names, const.F_names, const.name_map = data.get_data()
#extract the training/test sets
const.ngram_training_set = extract(config.data_extraction_size)
const.training_set = extract(config.training_size, labelled=True)
const.cv_set = extract(config.cv_set_size, labelled=True)
const.test_set = extract(config.test_set_size, labelled=True)
#determine most common ngrams

getCommonGrams(const.ngram_training_set)
get_suffixes(const.ngram_training_set)

const.featureCount += config.di_num + config.tri_num + config.last_letters + config.di_sufnum + config.tri_sufnum

X, y = extractFeatures(const.training_set)


print("results")