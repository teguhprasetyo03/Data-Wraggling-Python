# melakukan pengecekan data untuk nilai yang null

import pandas as pd

# csv_data = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/shopping_data.csv')

csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data_missingvalue.csv")

print(csv_data.isnull().values.any())
