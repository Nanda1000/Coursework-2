import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

def fit_preprocess(data_path)

data = pd.read_csv(data_path)
X    = data['XMEAS(1)'].to_numpy()
mean = X.mean()
std = X.std()
cov = X.cov()
preprocess_params = { 'mean': mean, 'std':std, 'cov':cov}
return preprocess_params

def load
