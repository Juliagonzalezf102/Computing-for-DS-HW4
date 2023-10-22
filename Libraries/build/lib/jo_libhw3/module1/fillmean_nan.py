import pandas as pd

def fillmean_nan(df, columns):
    """
    Fill NaN values in the specified columns with the mean of each column.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.
    - columns (list): List of column names to fill NaN values.

    Returns:
    - pd.DataFrame: DataFrame with NaN values filled with mean.
    """
    return df.fillna(df[columns].mean())