import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, mean_squared_error

class CustomModel:
    def __init__(self, feature_columns, target_column):
        # Constructor initializes feature columns, target column, and RandomForestClassifier model
        self.feature_columns = feature_columns
        self.target_column = target_column
        self.model_type = RandomForestClassifier(n_estimators=100, random_state=33)

    def train(self, train_data):
        # Train the RandomForestClassifier model on the training data
        X = train_data[self.feature_columns]
        y = train_data[self.target_column]
        self.model_type.fit(X, y)

    def proba_pred(self, data):
        # Predict probabilities using the trained model
        X = data[self.feature_columns]
        predicted_probabilities = self.model_type.predict_proba(X)
        return predicted_probabilities

    def evaluate(self, data, proba):
        # Evaluate the model using root mean squared error and ROC AUC score
        X = data[self.feature_columns]
        y = data[self.target_column]
        y_pred = self.model_type.predict(X)
        
        # Calculate Root Mean Squared Error
        rmse = np.sqrt(mean_squared_error(y, y_pred))
        print(f'Root Mean Squared Error: {rmse}')

        # Calculate ROC AUC Score
        roc_auc = roc_auc_score(y, proba[:, 1])
        print("ROC AUC Score:", roc_auc)

    def predict(self, data):
        # Make predictions using the trained model
        X = data[self.feature_columns]
        data['prediction'] = self.model_type.predict(X)
        return data