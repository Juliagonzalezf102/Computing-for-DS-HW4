from abc import ABC, abstractmethod

# FeatureTransformer abstract class for defining feature transformation
class FeatureTransformer(ABC):
    @abstractmethod
    def transform(self, df):
        pass  # Abstract method to be implemented by subclasses

# EthnicityEncoder class for encoding 'ethnicity' column based on mean diabetes_mellitus
class EthnicityEncoder(FeatureTransformer):
    def transform(self, df):
        # Calculate mean diabetes_mellitus for each ethnicity
        mean = df.groupby('ethnicity')['diabetes_mellitus'].mean()
        
        # Map 'ethnicity' column to mean values
        df['ethnicity'] = df['ethnicity'].map(mean)
        return df

# GenderEncoder class for encoding 'gender' column as binary (0 for Male, 1 for Female)
class GenderEncoder(FeatureTransformer):
    def transform(self, df):
        # Map 'gender' column using predefined mapping
        gender_map = {'F': 1, 'M': 0}
        df['gender'] = df['gender'].map(gender_map)
        return df