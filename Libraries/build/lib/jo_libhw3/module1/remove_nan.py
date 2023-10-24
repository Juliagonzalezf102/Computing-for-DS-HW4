import pandas as pd

def remove_nan(df, columns):
    """
    Remove rows with NaN values in any of the specified columns.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.
    - columns (list): List of column names to check for NaN values.

    Returns:
    - pd.DataFrame: DataFrame with rows removed.
    """
    return df.dropna(subset=columns)