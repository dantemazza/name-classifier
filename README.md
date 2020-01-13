# name-classifier

## Introduction
This supervised learning model predicts the sex of baby names using a kaggle dataset. The objective of this project was to see if we could make an accurate prediction on the sex associated with a name using a limited range of morphological features. This includes:
* n-gram combinations (i.e. "an", "ine", "hew")
* suffixes (including last-letters)<br />
For example, if a name has the suffix "ine", this usually points to female(Josephine, Caroline, etc.). The goal was to get the model to recognize this and perhaps more subtle features that humans would not consciously think about(perhaps a name containing the bigram "lo" is more closely associated with male names, as an example). 


## Program flow
The data is first processed and mapped in dataParser.py. Features used are common ngrams and suffixes(including last letters), extracted using the **nltk** library in features/grams.py. These morphological features are assembled into a **NumPy** design matrix in features/extractFeatures.py. The data is then loaded into **PyTorch** tensors in launch.py to train a Perceptron (single-layered neural network for binary classification). The model will make predictions on CV/Test sets and on any custom dataset in the test_cases directory. 

## Setup
Here is how to get started with running the project:

### Installations
The main obstacle downloading torch on your machine. It is highly recommended you use [Anaconda](https://anaconda.org/pytorch/pytorch) as your package manager as it will handle all dependencies (**NumPy**, **SciPy**, etc.). You will also need to install nltk:
```
conda install -c anaconda nltk
```
### Configuration
Most important settings can be toggled in configuration.py. For example, we can alter the set sizes: 
```python3
training_set_size = 10000
cv_set_size = 2000
test_set_size = 2000
```
Or how the model learns:
```python3
iterations = 20000
learning_rate = 0.001
minibatch = 100
```
And so on.

### Running the Project
The program flow is dictated in launch.py. Run this file to train the model. 


### Acnowledgements
* The pytorch model is loosely based off of [this](https://www.deeplearningwizard.com/deep_learning/practical_pytorch/pytorch_logistic_regression/) logistic regression classifier from Deep Learning Wizard
* Training, CV, and test sets all extracted randomly from [this dataset](https://www.kaggle.com/kaggle/us-baby-names)

