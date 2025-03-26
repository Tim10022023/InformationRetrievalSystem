import os

document_folder = "Document Collection Translated"


# load documents from data collection
documents = {}
for filename in os.listdir(document_folder):
    if filename.endswith(".txt"):
       with open(os.path.join(document_folder, filename), "r", encoding="utf-8") as file:
           documents[filename] = file.read().lower()


# boolean model
def boolean_search(query):
    query_terms = query.lower().split()
    matching_docs = []

    for doc_name, content in documents.items():
        if all(term in content for term in query_terms):
            matching_docs.append(doc_name)

    return matching_docs

query = input("\nEnter search query for boolean IR model: ")
results = boolean_search(query)

if results:
    print("Found following documents: ", results)
else:
    print("No matching documents found! Try another query")
