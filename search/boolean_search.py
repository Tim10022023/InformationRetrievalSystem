from .preprocessing import preprocess

def boolean_search(query, documents):
    query = preprocess(query)

    def evaluate_expression(expression):
        terms = expression.split()
        included_docs = None
        excluded_docs = set()
        mode = "AND"

        for term in terms:
            if term == "and":
                mode = "AND"
            elif term == "or":
                mode = "OR"
            elif term == "not":
                mode = "NOT"
            else:
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

    def parse_query(query):
        import re
        query = query.strip()
        if '(' in query or ')' in query:
            pattern = r'\(([^()]+)\)'
            while '(' in query:
                query = re.sub(pattern, lambda m: str(evaluate_expression(m.group(1))), query)
        return evaluate_expression(query)

    return list(parse_query(query))
