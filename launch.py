import const
import data
from functions import *
from classifier.ngrams import *
import configuration as config

#extract the data from csv
const.M_names, const.F_names, const.name_map = data.get_data()
#extract the training sets we are getting our ngrams from
const.ngram_training_set = extract(config.data_extraction_size)
#determine most common ngrams
getCommonNgrams(const.ngram_training_set)


print("results")