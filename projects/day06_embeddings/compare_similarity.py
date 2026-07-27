import ollama
import numpy as np

model = "nomic-embed-text"

sentences = [
    "Reset my password",
    "I forgot my password",
    "What's the weather today?"
]


def embedding(text):
    response = ollama.embed(
        model=model,
        input=text
    )

    return response["embeddings"][0]


def cosine_similarity(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)

    return np.dot(v1, v2) / (
        np.linalg.norm(v1) * np.linalg.norm(v2)
    )


vectors = []

for sentence in sentences:
    vectors.append(embedding(sentence))


print()

print("Similarity Results")

print("=" * 50)

for i in range(len(sentences)):

    for j in range(i + 1, len(sentences)):

        score = cosine_similarity(
            vectors[i],
            vectors[j]
        )

        print(f"{sentences[i]}")
        print(f"{sentences[j]}")
        print(f"Similarity : {score:.4f}")
        print()
