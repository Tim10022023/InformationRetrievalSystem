import math
from collections import Counter
from .preprocessing import preprocess

def compute_tf(doc):
    words = doc.split()
    word_counts = Counter(words)
    return {word: word_counts[word] / len(words) for word in word_counts}

def compute_idf(docs):
    num_docs = len(docs)
    idf = {}
    all_words = set(word for doc in docs.values() for word in doc.split())

    for word in all_words:
        containing_docs = sum(1 for doc in docs.values() if word in doc.split())
        idf[word] = math.log(num_docs / (1 + containing_docs))
    return idf

def cosine_similarity(query_vec, doc_vec):
    dot_product = sum(query_vec[word] * doc_vec.get(word, 0) for word in query_vec)
    query_norm = math.sqrt(sum(val ** 2 for val in query_vec.values()))
    doc_norm = math.sqrt(sum(val ** 2 for val in doc_vec.values()))
    return dot_product / (query_norm * doc_norm) if query_norm * doc_norm != 0 else 0

class RankedSearch:
    def __init__(self, documents):
        self.documents = {doc: preprocess(content) for doc, content in documents.items()}
        self.tf_values = {doc: compute_tf(content) for doc, content in self.documents.items()}
        self.idf_values = compute_idf(self.documents)
        self.tfidf_docs = {doc: {word: tf[word] * self.idf_values[word] for word in tf} for doc, tf in self.tf_values.items()}

    def search(self, query, docs_subset=None):
        query_words = preprocess(query).split()
        query_tf = Counter(query_words)
        query_tfidf = {word: (query_tf[word] / len(query_words)) * self.idf_values.get(word, 0) for word in query_tf}

        subset = docs_subset if docs_subset else self.documents.keys()
        scores = {doc: cosine_similarity(query_tfidf, self.tfidf_docs[doc]) for doc in subset}

        ranked_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return [(doc, score) for doc, score in ranked_docs if score > 0]
