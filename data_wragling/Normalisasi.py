import pandas as pd
import numpy as np
from sklearn import preprocessing

csv_data = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/shopping_data.csv')

array = csv_data.values