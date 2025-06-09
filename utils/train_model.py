import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

from dataset_load import path as dataset_path


df = pd.read_csv(dataset_path + "/data/creditcard_csv.csv")
df['Class'] = df['Class'].apply(lambda s: int(s.replace("'", "")))

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, shuffle=True, stratify=y)

X_train = X_train.drop(['Time', 'Amount'], axis=1)

neg, pos = np.bincount(y)
scale_pos_weight = neg / pos


model = VotingClassifier(
    estimators=[
        ('rf', RandomForestClassifier(n_jobs=-1,
                                      n_estimators=500,
                                      criterion='entropy',
                                      class_weight='balanced',
                                      max_features='sqrt',)),

        ('lr', LogisticRegression(class_weight='balanced',
                                  n_jobs=-1,
                                  max_iter=1000)),

        ('xgb', XGBClassifier(scale_pos_weight=scale_pos_weight,
                              n_jobs=-1,
                              n_estimators=500,
                              use_label_encoder=True,
                              eval_metric='logloss')),
    ],
    voting='soft',
)

model.fit(X_train, y_train)

joblib.dump(model, 'model.pkl')

## write the remaining test as a csv
test_csv = X_test
# test_csv['Class'] = y_test
test_csv.to_csv('test.csv', index=True, index_label='id')
y_test.to_csv('test_results.csv', index=True, index_label='id')

