class NaNFiller:
    def __init__(self, columns):
        # Constructor initializes the columns to fill NaN values
        self.columns = columns

    def preprocess(self, df):
        # Create a copy of the DataFrame to avoid modifying the original
        filled_df = df.copy()
        
        # Iterate over specified columns and fill NaN values with column means
        for column in self.columns:
            mean_value = df[column].mean()
            filled_df[column].fillna(mean_value, inplace=True)
        
        # Return the DataFrame with filled NaN values
        return filled_df
    
class NaNRowRemover:
    def __init__(self, columns):
        # Constructor initializes the columns to check for NaN values
        self.columns = columns

    def preprocess(self, df):
        # Remove rows with NaN values in specified columns
        cleaned_df = df.dropna(subset=self.columns)
        return cleaned_df