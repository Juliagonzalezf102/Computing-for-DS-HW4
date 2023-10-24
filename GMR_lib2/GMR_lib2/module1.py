'''
The function below removes rows with NaN values in the specified subset of columns.
'''

def nan_remover(data, columns):
    return data.dropna(axis = 0, subset = columns)

'''
import pandas as pd
import numpy as np
from IPython.display import display

test_df = pd.DataFrame({'a': [np.nan, 2, np.nan], 'b': [4, 5, np.nan], 'c': [7, 8, 9]}, index = ['first row', 'second row', 'third row'])
#test_df = nan_remover(test_df, ['a', 'c'])

print(test_df)
'''

'''
The function below fills NaN values of the mean of their column in the specificed subset of columns.
'''

def nan_filler(data, columns):
    return data.fillna(data[columns].mean())

'''
The function below generates dummy variables for the specified subset of columns.
'''

def one_hot(data, columns):
    import pandas as pd
    from sklearn.preprocessing import OneHotEncoder
    enc = OneHotEncoder(handle_unknown = 'ignore')
    encoded_data = enc.fit_transform(data[[columns]]).toarray()
    encoded_df = pd.DataFrame(encoded_data, columns = enc.get_feature_names_out ([columns]), index = data.index)
    encoded_df = pd.concat([data, encoded_df], axis = 1)
    
    return encoded_df

'''
The function below adds to the dataframe with an additional column for the dummy variable.
'''

def dummy_gen(data, columns):
    unique_values = data[columns].unique()
    mapping = {unique_values[0]: 0, unique_values[1]: 1}
    data[f'{columns}_dummy'] = data[columns].map(mapping)
    return data

'''

'''