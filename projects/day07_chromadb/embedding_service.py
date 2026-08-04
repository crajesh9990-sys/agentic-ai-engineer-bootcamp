import ollama

model = "nomic-embed-text"

def get_embeddings(text: str):
    embeddings_response = ollama.embed(
        model=model,
        input=text
    )
    return embeddings_response["embeddings"][0]
