def build_prompt(
    question,
    documents
):

    context = ""

    for document in documents:
        context += document
        context += "\n\n"

    prompt = f"""

You are an Enterprise IT Assistant.

Answer ONLY using the information below.

If the answer cannot be found,

say

"I don't have enough information."

Context

-------------------------

{context}

-------------------------

Question

{question}

Answer

"""

    return prompt
