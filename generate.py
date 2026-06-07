import ollama
import chromadb
from sentence_transformers import SentenceTransformer

# 1. Setup
model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(name="housing_docs")

def ask(question):
    # 2. Retrieve
    query_vector = model.encode(question).tolist()
    results = collection.query(query_embeddings=[query_vector], n_results=4)
    
    context_text = "\n\n".join(results['documents'][0])
    sources = list(set([m['source'] for m in results['metadatas'][0]]))

    # 3. Generate (Grounded)
    # 3. Generate (Grounded and Resilient)
    # 3. Generate (Grounded and Synthesized)
    # 3. Generate (Grounded, Chain-of-Thought Structure)
    prompt = f"""
    You are a helpful assistant answering questions based on a provided text corpus.
    
    Instructions:
    1. First, scan the text corpus for any mentions, rules, general guidance, or behavioral responsibilities related to the setting in the question (e.g., off-campus).
    2. Synthesize an answer based on those findings. If the text provides guidelines or behavioral expectations (such as lease rules, party hosting responsibilities, or conduct consequences) rather than a formal policy document, use that information to construct your response.
    3. Clearly distinguish between on-campus and off-campus rules if both are present in the text.
    4. If the text does not contain any relevant information, rules, or guidance on the topic at all, reply with exactly: "I don't have enough information."
    
    Context:
    {context_text}
    
    Question: {question}
    """
    
    response = ollama.chat(model='llama3.1', messages=[
        {'role': 'user', 'content': prompt}
    ])
    
    return {
        "answer": response['message']['content'],
        "sources": sources
    }

if __name__ == "__main__":
    q = "What is the policy for off-campus guests?"
    result = ask(q)
    print(f"\nAnswer: {result['answer']}")
    print(f"\nSources: {', '.join(result['sources'])}")