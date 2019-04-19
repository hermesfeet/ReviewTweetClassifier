'''This script uses Python to examine the existing datasets.'''

import pandas as pd

#Create simple filepaths
filepath_dict = {'yelp': 'data/yelp_labelled.txt',
                 'amazon': 'data/amazon_cells_labelled.txt',
                 'imdb': 'data/imdb_labelled.txt'
                 }

df_list = []

#Set up simple Pandas dataframes
for source, filepath in filepath_dict.items():
    df = pd.read_csv(filepath, names = ['sentence', 'label'], sep='\t')
    df['source'] = source #Adds another column with the source name
    df_list.append(df)

#Concatanate all the data and show a slice
df = pd.concat(df_list)
#print(df.iloc[:5])

