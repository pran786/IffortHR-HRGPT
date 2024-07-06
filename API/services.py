import os
import requests
from bs4 import BeautifulSoup
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import openai
from dotenv import load_dotenv
from openai import OpenAI
import numpy as np
load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)
vectorizer = TfidfVectorizer()

def read_text_from_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."
    except Exception as e:
        return f"Error: An exception occurred - {str(e)}"

def preprocess_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower()

def create_embeddings(texts):
    global vectorizer
    return vectorizer.fit_transform(texts)

def get_embedding(text, model="text-embedding-3-small"):
#    text = text.replace("\n", " ")
   return client.embeddings.create(input = text, model=model).data[0].embedding

def cosine_similarityOpenAi(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def find_most_relevant(query, embeddings, texts):
    query_embedding = get_embedding(query)
    similarities = [cosine_similarityOpenAi(query_embedding, emb) for emb in embeddings]
    most_similar_idx = np.argmax(similarities)
    return texts[most_similar_idx], similarities[most_similar_idx]


def find_most_relevantO(query, embeddings, texts):
    global vectorizer
    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, embeddings)
    most_similar_idx = similarities.argmax()
    return texts[most_similar_idx], similarities[0][most_similar_idx]

def generate_response(prompt, context):
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful HR assistant. please respond to the questions which is relevent to the context"},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {prompt}"}
        ]
    )
    return response.choices[0].message.content

def is_relevant(similarity_score, threshold=0.2):
    return similarity_score >= threshold

class HRAssistant:
    def __init__(self, url):
        raw_text = read_text_from_file(url)
        processed_text = preprocess_text(raw_text)
        self.texts = [processed_text[i:i+1000] for i in range(0, len(processed_text), 1000)]
        # self.embeddings = create_embeddings(self.texts)
        self.embeddings = [get_embedding(text) for text in self.texts]


    def get_response(self, query):
        relevant_context, similarity_score = find_most_relevant(query, self.embeddings, self.texts)
        
        if is_relevant(similarity_score):
            return generate_response(query, relevant_context)
        else:
            return "I'm sorry, but that question doesn't seem to be related to our company's HR policies or information. Is there anything specific about our company or HR practices you'd like to know?"