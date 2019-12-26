# name-classifier
This supervised learning model predicts the gender of American baby names from kaggle dataset. Features used were common ngrams and suffixes(including last letters), extracted using **nltk**. The mentioned morphological features are assmebled into a design matrix with a vector of outputs in **NumPy**. The data is then loaded into **PyTorch** tensors to so it can be used to train a Perceptron (single-layered neural network for binary classification). The model will make predictions on CV/Test sets, then on any custom dataset in the test_cases directory. 

## Setup
If you wish to run this project yourself, here are instructions:

### Installations
The main obstacle is to download torch on your machine. It is highly recommended you use [Anaconda] https://anaconda.org/pytorch/pytorch) as your package manager as it will manage all related dependencies (**NumPy**, **SciPy**, etc.). You will also need to install nltk:
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
### Running the Project
The model program flow is dictated in launch.py. Run this file to train the model. 



### Acnowledgements
* The pytorch model is loosely based off of [this](https://www.deeplearningwizard.com/deep_learning/practical_pytorch/pytorch_logistic_regression/) logistic regression classifier from Deep Learning Wizard

* Training, CV and test sets all extracted randomly from [this dataset](https://www.kaggle.com/kaggle/us-baby-names)

