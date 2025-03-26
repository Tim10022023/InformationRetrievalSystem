import os
import math
from collections import Counter

document_folder = "Document Collection Translated"

# Load documents from data collection
documents = {}
for filename in os.listdir(document_folder):
    if filename.endswith(".txt"):
       with open(os.path.join(document_folder, filename), "r", encoding="utf-8") as file:
           documents[filename] = file.read().lower()

print("\nLoaded Documents:", list(documents.keys()))

# Calculating Term Frequency (TF)
def compute_tf(doc):
    words = doc.split()
    word_counts = Counter(words)
    tf = {word: word_counts[word] / len(words) for word in word_counts}
    return tf

# Calculating Inverse Document Frequency (IDF)
def compute_idf(docs):
    num_docs = len(docs)
    idf = {}
    all_words = set(word for doc in docs.values() for word in doc.split())

    for word in all_words:
        containing_docs = sum(1 for doc in docs.values() if word in doc.split())
        idf[word] = math.log(num_docs / (1 + containing_docs)) 

    return idf

# Calculate TF and IDF for every document
tf_values = {doc: compute_tf(content) for doc, content in documents.items()}
idf_values = compute_idf(documents)

# Calculating TF-IDF
tfidf_docs = {}
for doc, tf in tf_values.items():
    tfidf_docs[doc] = {word: tf[word] * idf_values[word] for word in tf}

# Calculating Cosine similarity
def cosine_similarity(query_vec, doc_vec):
    dot_product = sum(query_vec[word] * doc_vec.get(word, 0) for word in query_vec)
    query_norm = math.sqrt(sum(val ** 2 for val in query_vec.values()))
    doc_norm = math.sqrt(sum(val ** 2 for val in doc_vec.values()))
    
    return dot_product / (query_norm * doc_norm) if query_norm * doc_norm != 0 else 0

# vector space model search
def vector_search(query):
    query_words = query.lower().split()
    query_tf = Counter(query_words)
    query_tfidf = {word: (query_tf[word] / len(query_words)) * idf_values.get(word, 0) for word in query_tf}

    print("\nQuery TF-IDF Vector:")
    print(query_tfidf)  # print Query TF-IDF

    scores = {doc: cosine_similarity(query_tfidf, tfidf_docs[doc]) for doc in documents}
    
    print("\nCosine Similarity Scores:")
    print(scores)  # print cosine similarity to every document

    ranked_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [(doc, score) for doc, score in ranked_docs if score > 0]

while True:
    query = input("\nEnter search query for vector space IR model (or type 'exit' to quit): ").strip()

    if query.lower() == "exit" or query == "":
        print("Exiting Vector Space Search. Goodbye!")
        break  # Exit while loop

    results = vector_search(query)

    if results:
        print("\nTop matching documents:")
        for doc, score in results:
            print(f"{doc} - Score: {score:.4f}")
    else:
        print("\nNo relevant documents found! Try another query.")
