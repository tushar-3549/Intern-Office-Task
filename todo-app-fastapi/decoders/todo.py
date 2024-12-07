
def decode_todo(doc) -> dict:
    return {
        'id': doc.id,
        'root': doc.root,
        'synonyms': doc.synonyms
    }
def decode_todos(docs) -> list:
    return [decode_todo(doc) for doc in docs]