from sentence_transformers import SentenceTransformer
from rapidfuzz import process
import random

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_distractors(question, correct_answer):

    # simple candidate pool
    candidate_pool = [
        "London","Berlin","Rome","Madrid","Tokyo","Delhi",
        "Mercury","Venus","Mars","Jupiter",
        "Oxygen","Hydrogen","Nitrogen",
        "CPU","GPU","RAM","Motherboard"
    ]

    embeddings = model.encode([correct_answer] + candidate_pool)

    correct_embedding = embeddings[0]
    candidate_embeddings = embeddings[1:]

    similarities = []

    for i, emb in enumerate(candidate_embeddings):
        score = (correct_embedding @ emb)
        similarities.append((candidate_pool[i], score))

    similarities.sort(key=lambda x: x[1], reverse=True)

    distractors = [x[0] for x in similarities[:3]]

    return distractors
