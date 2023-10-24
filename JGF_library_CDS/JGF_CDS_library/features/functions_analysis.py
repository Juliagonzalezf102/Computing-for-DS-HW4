# %%
import numpy as np
from abc import ABC, abstractmethod
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv(
    r'C:\Users\julia\OneDrive\Documentos\DSDM\Computing for Data Science\Fourth Lecture\sample_diabetes_mellitus_data.csv')
df.head()


# %%
class Primary:
    def __init__(self):
        self.load_data()
        self.split_data()

    def load_data(self):
        df = pd.read_csv(
            r'C:\Users\julia\OneDrive\Documentos\DSDM\Computing for Data Science\Fourth Lecture\sample_diabetes_mellitus_data.csv')
        self.X = df[['age', 'bmi', 'ethnicity', 'gender',
                     'height', 'hospital_admit_source']]
        self.y = df['diabetes_mellitus']

    def split_data(self):
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=77)
        self.train_df = pd.concat([X_train, y_train], axis=1)
        self.test_df = pd.concat([X_test, y_test], axis=1)


class Remove_NaN(Primary):
    def __init__(self, columns):
        super().__init__()
        self.columns = columns
        self.remove_NaN()

    def remove_NaN(self):
        self.train_df = self.train_df.dropna(subset=self.columns)
        self.test_df = self.test_df.dropna(subset=self.columns)


class Fill_mean(Primary):
    def __init__(self, columns):
        super().__init__()
        self.columns = columns
        self.fill_mean()

    def fill_mean(self):
        self.train_df = self.train_df.fillna(
            self.train_df[self.columns].mean())
        self.test_df = self.test_df.fillna(self.test_df[self.columns].mean())


data1 = Primary()
data2 = Remove_NaN(['age', 'gender', 'ethnicity'])
data3 = Fill_mean(['height'])

# CORREGIDO HASTA AQUI

# %%


class Feature(ABC):
    def __init__(self, name):
        self.name = name
        # abstractmethod

    def transform_data(self):
        pass


class Encoding_height(Feature):
    def transform_data(self):
        mean_height_ethnicity = train_df.groupby['ethnicity']('height').mean()
        train_df['ethnicity_encoded'] = train_df['ethnicity'].map(
            mean_height_ethnicity)
        test_df['ethnicity_encoded'] = test_df['ethnicity'].map(
            mean_height_ethnicity)
        return train_df & test_df


class Encoding_age(Feature):
    def transform_data(self):
        mean_age_ethnicity = train_df.groupby['ethnicity']('age').mean()
        train_df['ethnicity_encoded'] = train_df['ethnicity'].map(
            mean_age_ethnicity)
        test_df['ethnicity_encoded'] = test_df['ethnicity'].map(
            mean_age_ethnicity)
        return train_df & test_df

# %%


class MachineLearning(Primary):
    def __init__(self, feature, target, hyperparameter, model):
        self.feature = feature
        self.target = target
        self.hyperparameter = hyperparameter
        self.model = model

    def training_data(self, train_df):
        self.train_df = train_df
        X = df['age', 'bmi', 'ethnicity', 'gender',
               'height', 'hospital_admit_source']
        y = df['diabetes_mellitus']
        model = RandomForestClassifier(n_estimators=100, random_state=33)
        model.fit(X_train, y_train)
        probability = model.predict_proba(X)
        print(f'Probability of {probability}')

    def predict_data(self, y_pred, model):
        self.pred = y_pred
        y_pred = model.predict_proba(X_test)
