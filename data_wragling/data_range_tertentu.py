# melakukan akses data dalam range tertentu

import pandas as pd

csv_data = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/shopping_data.csv')


print('Menampilkan data ke 5 sampai kurang dari 10 dalam satu baris ')

# sort/filter by age
print(csv_data['Age'].iloc[5:10])

# sort/filter by row
print(csv_data.iloc[5:10])
