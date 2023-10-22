# module1.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import roc_auc_score

def fillmean_nan(df:pd.DataFrame, columns:list):
    """
    Fill NaN values in the specified columns with the mean of each column.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.
    - columns (list): List of column names to fill NaN values.

    Returns:
    - pd.DataFrame: DataFrame with NaN values filled with mean.
    """
    return df.fillna(df[columns].mean())

def remove_nan(df:pd.DataFrame, columns:list):
    """
    Remove rows with NaN values in any of the specified columns.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.
    - columns (list): List of column names to check for NaN values.

    Returns:
    - pd.DataFrame: DataFrame with rows removed.
    """
    return df.dropna(subset=columns)

def mapping(df:pd.DataFrame, column:str, map:dict):
    """
    Map the values of a DataFrame feature according to a map given.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.
    - columns (list): String with name of the column to map.
    - map (dict): Dictionary where keys are original values and values are new ones.

    Returns:
    - pd.DataFrame: DataFrame with new mapped values on given column.
    """
    df[column] = df[column].map(map)
    return df

def mean_encoding(df:pd.DataFrame, encode_column: list, value_column:str):
    """
    Encode a categorical feature using the mean values of a value feature.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.
    - encode_column (list): String with name of the column to encode.
    - value_column (dict): String with name of the column with the values to use for the mean.

    Returns:
    - pd.DataFrame: DataFrame with new mapped values on given column.
    """

    mean = df.groupby(encode_column)[value_column].mean()
    df[encode_column] = df[encode_column].map(mean)
    return df


def predict_model(df:pd.DataFrame, feature_columns: list, predict_column:str):
    """
    Predcit values on a dataset giving the columns to use to predict and the target column to predict.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.
    - feature_columns (list): List of column names to use on the model to predict.
    - predict_column (list): String with name of the column to predict.

    Returns:
    - pd.DataFrame: DataFrame with new column "prediction" with the predict values.
    """
    X = df[feature_columns]
    y = df[predict_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=77)

    # Train a Linear Regression Model
    model = RandomForestClassifier(n_estimators=100, random_state=33)
    model.fit(X_train, y_train)
    probability = model.predict_proba(X)
    print(f'Probability of {probability}')

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f'Root Mean Squared Error: {rmse}')

    roc_auc = roc_auc_score(y, probability[:, 1])  # Assuming binary classification
    print("ROC AUC Score:", roc_auc)

    # Make Predictions on the Test Set
    df['prediction'] = model.predict(X)
    return df