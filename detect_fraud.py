import sys
import joblib
import pandas as pd

# Load the pre-trained model
model = joblib.load('utils/model.pkl')


def classify(samples):
    pred = model.predict(samples)
    return pred


def preprocess(df):
    df = df.drop(['Time', 'Amount', 'id'], axis=1)

    return df


if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) != 1:
        raise ValueError("Expected 1 argument")

    try:
        ## read csv file
        path = args[0]
        to_predict = pd.read_csv(path)

        ids = to_predict['id'].values
    except FileNotFoundError as e:
        raise FileNotFoundError(f"No such file or directory: {e.filename}")

    # preprocess
    to_predict = preprocess(to_predict)

    # classify
    predictions = pd.DataFrame(ids, columns=['id'])
    predictions['Class'] = classify(to_predict)

    # write to file
    predictions.to_csv('predictions.csv', index=False)
