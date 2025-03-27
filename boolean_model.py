import os

document_folder = "Data Collection/Document Collection Translated"

# Load documents from data collection
documents = {}
for filename in os.listdir(document_folder):
    if filename.endswith(".txt"):
        with open(os.path.join(document_folder, filename), "r", encoding="utf-8") as file:
            documents[filename] = file.read().lower()

# Boolean model with AND, OR, NOT
def boolean_search(query):
    query = query.lower()
    
    # split query in terms and operations
    terms = query.split()
    
    included_docs = None  # empty set, because no term of the query is checked yet
    excluded_docs = set()
    
    mode = "AND"  # default mode is AND
    
    for term in terms:

        # found AND operation
        if term == "and":
            mode = "AND"

        # found OR operation
        elif term == "or":
            mode = "OR"

        # found NOT operation
        elif term == "not":
            mode = "NOT"

        # found any normal query term like "tree" or "waterfall"
        else:
            term_docs = {doc_name for doc_name, content in documents.items() if term in content}

            if included_docs is None:
                included_docs = term_docs  # For first term of query just copy content in result docs
            elif mode == "AND":
                included_docs &= term_docs  # AND mode: intersection of previous result and current term docs
            elif mode == "OR":
                included_docs |= term_docs  # OR mode: union of previous result and current term docs
            elif mode == "NOT":
                excluded_docs |= term_docs  # NOT mode: save docs with not allowed term to exclude them before the final output

    # If there is no OR / AND operation, NOT should not exclude every document
    if included_docs is None:
        included_docs = set(documents.keys())

    # Exclude Documents with NOT
    result_docs = included_docs - excluded_docs

    return list(result_docs)

while True:
    query = input("\nEnter search query for boolean IR model (use AND, OR, NOT) or type 'exit' to quit: ").strip()
    
    if query.lower() == "exit" or query == "":
        print("Exiting Boolean Search. Goodbye!")
        break  # End while loop

    results = boolean_search(query)

    if results:
        print("Found following documents: ", results)
    else:
        print("No matching documents found! Try another query.")
