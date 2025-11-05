import re

def extract_features(url):
    # Example lexical features used in most malicious URL detection research
    features = {}
    features['url_length'] = len(url)
    features['num_dots'] = url.count('.')
    features['num_hyphens'] = url.count('-')
    features['num_at'] = url.count('@')
    features['has_ip'] = int(bool(re.search(r'http[s]?://(?:[0-9]{1,3}\.){3}[0-9]{1,3}', url)))
    keywords = ['login', 'admin', 'verify', 'update', 'bank', 'free', 'secure', 'account']
    for kw in keywords:
        features[f'kw_{kw}'] = int(kw in url.lower())
    return features

def preprocess_url(url):
    # Remove whitespaces and normalize
    return url.strip()
