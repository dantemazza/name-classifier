import dataParser as data


starting_year = 1960
data_extraction_size = 5000
training_size = 1800
cv_set_size = 600
test_set_size = 600


#---gram features---#

di_num = 100
tri_num = 100


#---suffixes---#

last_letters = 8
di_sufnum = 50
tri_sufnum = 50


#---optim variables---#
iterations = 3000
learning_rate = 0.01
minibatch = 50