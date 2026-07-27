import ollama

sentences = [
    "Reset my password",
    "I forgot my password",
    "What's the weather today?"
]

model = "nomic-embed-text"

print("=" * 60)

for sentence in sentences:

    response = ollama.embed(
        model=model,
        input=sentence
    )

    embedding = response["embeddings"][0]

    print(f"Sentence : {sentence}")
    print(f"Vector Length : {len(embedding)}")
    print(f"First 10 Values : {embedding[:10]}")
    print("-" * 60)