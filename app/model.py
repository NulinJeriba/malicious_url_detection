import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
from lightgbm import LGBMClassifier

MODEL_PATH = "app/model.pkl"
LABEL_MAP = {"benign": 0, "phishing": 1, "defacement": 2, "malware": 3}

# Custom transformer for engineered URL features
class URLFeatureExtractor(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, urls):
        features = pd.DataFrame()
        features['length'] = urls.apply(len)
        features['num_digits'] = urls.apply(lambda x: sum(c.isdigit() for c in x))
        features['num_special'] = urls.apply(lambda x: sum(not c.isalnum() for c in x))
        features['has_http'] = urls.apply(lambda x: 1 if 'http' in x else 0)
        features['num_dots'] = urls.apply(lambda x: x.count('.'))
        return features.values

def prepare_dataset(csv_path):
    df = pd.read_csv(csv_path)
    df = df.dropna()
    X = df['url']
    y = df['type'].map(LABEL_MAP)
    return X, y

def train_and_save(csv_path):
    X, y = prepare_dataset(csv_path)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    feature_union = FeatureUnion([
        ('tfidf', TfidfVectorizer(analyzer='char_wb', ngram_range=(3,7), max_features=2000)),
        ('url_features', URLFeatureExtractor()),
    ])

    pipeline = Pipeline([
        ('features', feature_union),
        ('lgbm', LGBMClassifier(n_estimators=100, n_jobs=-1, random_state=42,force_col_wise=True,
    verbose=10))
    ])

    pipeline.fit(X_train, y_train)
    preds = pipeline.predict(X_test)
    acc = accuracy_score(y_test, preds)
    f1 = f1_score(y_test, preds, average="weighted")

    joblib.dump(pipeline, MODEL_PATH)
    print(f"Saved model to {MODEL_PATH}, Accuracy: {acc:.3f}, F1: {f1:.3f}")

def load_model():
    return joblib.load(MODEL_PATH)

def predict_url(url, model):
    import pandas as pd
    # Ensure the input is a pandas Series for pipeline consistency
    input_series = pd.Series([url])
    pred = model.predict(input_series)
    rev_label_map = {v: k for k, v in LABEL_MAP.items()}
    return rev_label_map.get(pred[0], "unknown")
