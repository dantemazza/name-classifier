import const
import data
from functions import *
import configuration as config

const.M_names, const.F_names, const.name_map = data.get_data()
const.ngram_training_set = extract(config.data_extraction_size)
print("results")