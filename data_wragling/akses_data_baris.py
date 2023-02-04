# melakukan akses data kolom

import pandas as pd

csv_data = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/shopping_data.csv')

# print(csv_data.columns)

print(csv_data.iloc[5])