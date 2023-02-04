# menampilkan informasi statistik pada suatu dengan dengan numpy

import pandas as pd

csv_data = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/shopping_data.csv')

# menampilkan semua data, termasuk format Nan
# print(csv_data.describe(include="all"))

# filter with data numerical
print(csv_data.describe(exclude=["O"]))