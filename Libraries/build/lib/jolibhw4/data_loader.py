import pandas as pd
from sklearn.model_selection import train_test_split

# DataLoader class for loading and splitting data
class DataLoader:
    def __init__(self, file_path):
        # Constructor initializes the file path
        self.file_path = file_path

    def load_data(self):
        # Load data from CSV file using pandas
        data = pd.read_csv(self.file_path)

        # Split the data into training and testing sets
        train_df, test_df = train_test_split(data, test_size=0.2, random_state=42)

        # Return the training and testing DataFrames
        return train_df, test_df