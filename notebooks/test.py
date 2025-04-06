import os
import pandas as pd
print("Current directory:", os.getcwd())
df = pd.read_csv('./Notebooks/IMDB.csv')
print(df.shape)