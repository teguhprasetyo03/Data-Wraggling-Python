# # melakukan pengecekan data untuk nilai yang null
#
# import pandas as pd
#
# # csv_data = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/shopping_data.csv')
#
# csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data_missingvalue.csv")
#
# print("Dataset yang masih terdapat nilai kosong ! :")
# print(csv_data.head(10))
#
# csv_data = csv_data.fillna(csv_data.median())
#
# print("Dataset yang sudah di proses Handling Missing Values dengan Mean  :")
# print(csv_data.head(10))

import pandas as pd

csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data_missingvalue.csv")
print("Dataset yang masih terdapat nilai kosong ! :")
print(csv_data.head(10))

csv_data=csv_data.fillna(csv_data.median())
print("Dataset yang sudah diproses Handling Missing Values dengan Median :")
print(csv_data.head(10))