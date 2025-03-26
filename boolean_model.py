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

# check for every document content if it contains search term
    for doc_name, content in documents.items():
        if all(term in content for term in query_terms):
            matching_docs.append(doc_name)

    return matching_docs

while True:
    query = input("\nEnter search query for boolean IR model (or type 'exit' to quit): ").strip()
    
    if query.lower() == "exit" or query == "":
        print("Exiting Boolean Search. Goodbye!")
        break  # Beende die Schleife

    results = boolean_search(query)

    if results:
        print("Found following documents: ", results)
    else:
        print("No matching documents found! Try another query.")
