from sklearn.feature_extraction.text import CountVectorizer

def extract_keywords(text: str):
    vectorizer = CountVectorizer(stop_words='english', max_features=5)
    X = vectorizer.fit_transform([text])
    return vectorizer.get_feature_names_out().tolist()