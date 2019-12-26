# name-classifier
This supervised learning model predicts the gender of American baby names from kaggle dataset. Features used were common ngrams and suffixes(including last letters), extracted using **nltk**. The mentioned morphological features are assmebled into a design matrix with a vector of outputs in **NumPy**. The data is then loaded into **PyTorch** tensors to so it can be used to train a Perceptron (single-layered neural network for binary classification). The model will make predictions on CV/Test sets, then on any custom dataset in the test_cases directory. 

## Setup:
If you wish to run this project yourself, here are instructions.

### Prerequisites: 
The main obstacle is to download torch on your machine. I used **Anaconda** as my package manager and highly recommend it as it will download all of the associated dependencies for you. 





* The pytorch model is loosely based off of this logistic regression classifier from Deep Learning Wizard: https://www.deeplearningwizard.com/deep_learning/practical_pytorch/pytorch_logistic_regression/

* Training, CV and test sets all extracted randomly from this dataset: https://www.kaggle.com/kaggle/us-baby-names

