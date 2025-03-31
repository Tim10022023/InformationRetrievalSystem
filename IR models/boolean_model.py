import os
import re

document_folder = "Data Collection/Document Collection Translated"

# Load documents from data collection
documents = {}
for filename in os.listdir(document_folder):
    if filename.endswith(".txt"):
        with open(os.path.join(document_folder, filename), "r", encoding="utf-8") as file:
            documents[filename] = file.read().lower()

# Boolean model with AND, OR, NOT with support for parentheses
def boolean_search(query):
    query = query.lower()

    # Function to evaluate individual terms or grouped expressions
    def evaluate_expression(expression):
        # Split the expression into terms and operations
        terms = expression.split()
        
        included_docs = None
        excluded_docs = set()
        mode = "AND"  # Default mode is AND
        
        for term in terms:
            # Process logical operators
            if term == "and":
                mode = "AND"
            elif term == "or":
                mode = "OR"
            elif term == "not":
                mode = "NOT"
            else:
                # Process normal terms
                term_docs = {doc_name for doc_name, content in documents.items() if term in content}
                
                if included_docs is None:
                    included_docs = term_docs
                elif mode == "AND":
                    included_docs &= term_docs
                elif mode == "OR":
                    included_docs |= term_docs
                elif mode == "NOT":
                    excluded_docs |= term_docs
        
        return included_docs - excluded_docs if included_docs else set()

    # Function to parse and evaluate a query with parentheses
    def parse_query(query):
        # Remove extra spaces and split based on parentheses
        query = query.strip()
        if '(' in query or ')' in query:
            # Find the most inner parenthesis and evaluate the expression
            pattern = r'\(([^()]+)\)'
            while '(' in query:
                # Process the most inner expression first
                query = re.sub(pattern, lambda m: str(evaluate_expression(m.group(1))), query)
        
        return evaluate_expression(query)

    return list(parse_query(query))

while True:
    query = input("\nEnter search query for boolean IR model (use AND, OR, NOT, parentheses) or type 'exit' to quit: ").strip()
    
    if query.lower() == "exit" or query == "":
        print("Exiting Boolean Search. Goodbye!")
        break  # End while loop

    results = boolean_search(query)

    if results:
        print("Found following documents: ", results)
    else:
        print("No matching documents found! Try another query.")
