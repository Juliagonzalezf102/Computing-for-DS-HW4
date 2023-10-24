#%%
import pandas as pd
from jolibhw4.data_loader import DataLoader
from jolibhw4.cleaner import NaNRowRemover, NaNFiller
from jolibhw4.feature_transf import EthnicityEncoder, GenderEncoder
from jolibhw4.custom_model import CustomModel

load_data = DataLoader('sample_diabetes_mellitus_data.csv')
train_data, test_data = load_data.load_data()
print(train_data.shape)

clean_data1 = NaNRowRemover(['age', 'gender', 'ethnicity'])
train_data = clean_data1.preprocess(train_data)
test_data = clean_data1.preprocess(test_data)

clean_data2 = NaNFiller(['height', 'weight'])
train_data = clean_data2.preprocess(train_data)
test_data = clean_data2.preprocess(test_data)

trans_data1 = EthnicityEncoder()
trans_data2 = GenderEncoder()
train_data = trans_data1.transform(train_data)
train_data = trans_data2.transform(train_data)
test_data = trans_data1.transform(test_data)
test_data = trans_data2.transform(test_data)

print(train_data.shape)

feat_col = ['age', 'height', 'weight', 'aids', 'cirrhosis', 'hepatic_failure',
'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']
pred_col = ['diabetes_mellitus']

custom_model = CustomModel(feat_col, pred_col)

custom_model.train(train_data)

predicted_probabilities = custom_model.proba_pred(test_data)

print("Predicted Probabilities:")
print(predicted_probabilities)

custom_model.evaluate(test_data, predicted_probabilities)
full_data = pd.concat([train_data, test_data])
full_data = custom_model.predict(full_data)

full_data.head()