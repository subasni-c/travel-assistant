from src.embeddings import get_embeddings
from src.config import COLLECTION_NAME
from src.vectorstores import get_qdrant_client

def retrieve_docs(query: str, top_k=5):
    # Get the Qdrant client
    client = get_qdrant_client()

    query_vector = get_embeddings([query])[0]

    # ✅ FIXED: Changed client.search() → client.query_points()
    search_result = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,       # Changed: query_vector= → query=
        limit=top_k,
        with_payload=True         # Added: needed to get text back
    )

    print("Retriever module loaded successfully.")
    # ✅ FIXED: Changed search_result → search_result.points
    return [hit.payload["text"] for hit in search_result.points]

# from src.embeddings import get_embeddings
# from src.config import COLLECTION_NAME
# from src.vectorstores import get_qdrant_client

# def retrieve_docs(query: str, top_k=5):
#     # Get the Qdrant client
#     client = get_qdrant_client()

#     query_vector = get_embeddings([query])[0]

#     search_result = client.query_points(
#         collection_name=COLLECTION_NAME,
#         query=query_vector,       # Changed: query_vector= → query=
#         limit=top_k,
#         with_payload=True 
#     )

#     print("Retriever module loaded successfully.")
#     return [hit.payload["text"] for hit in search_result]
    
    
