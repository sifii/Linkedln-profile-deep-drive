import pandas as pd
from gensim.models import Word2Vec
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import distance
from jellyfish import jaro_winkler_similarity
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine
# Load CSV file into a DataFrame
csv_file_path = r'C:\Users\Sifi_world\Downloads\Complete_LinkedInDataExport_11-10-2023\Complete_LinkedInDataExport_11-10-2023\Skills.csv'  # Replace with your actual file path
df = pd.read_csv(csv_file_path)

# Tokenize the text into words
tokenized_text = [str(sentence).lower().split() for sentence in df['Name']]

# Train a Word2Vec model
model = Word2Vec(sentences=tokenized_text, vector_size=100, window=5, min_count=1, workers=4)

# Function to calculate word similarity
def calculate_word_similarity(word1, word2):
    try:
        similarity = model.wv.similarity(word1, word2)
        return similarity
    except KeyError:
        return 0.0  # Return 0 similarity if one or both words are not in the vocabulary

# Create a matrix of word similarities
word_similarity_matrix = pd.DataFrame(index=df['Name'], columns=df['Name'])
for word1 in word_similarity_matrix.index:
    for word2 in word_similarity_matrix.columns:
        similarity = calculate_word_similarity(word1, word2)
        word_similarity_matrix.loc[word1, word2] = similarity

# Plot a heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(word_similarity_matrix.astype(float), annot=True, cmap='coolwarm', vmin=0, vmax=1)
plt.title('Word Similarity Heatmap using Word2vec')
plt.show()

# Tokenize the text into words
tokenized_text = [str(sentence).lower().split() for sentence in df['Name']]

# Convert the tokenized text to strings
preprocessed_text = [' '.join(tokens) for tokens in tokenized_text]

# Use TF-IDF vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(preprocessed_text)

# Calculate cosine similarity between words
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Create a DataFrame with similarity scores
word_similarity_matrix = pd.DataFrame(cosine_sim, index=df['Name'], columns=df['Name'])

# Plot a heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(word_similarity_matrix, annot=True, cmap='coolwarm', vmin=0, vmax=1)
plt.title('Word Similarity Heatmap (cosine similarity Similarity)')
plt.show()

# Function to calculate word similarity using Levenshtein distance
def calculate_word_similarity(word1, word2):
    return 1 - distance.nlevenshtein(word1, word2) / max(len(word1), len(word2))

# Create a matrix of word similarities
word_similarity_matrix = pd.DataFrame(index=df['Name'], columns=df['Name'])
for word1 in word_similarity_matrix.index:
    for word2 in word_similarity_matrix.columns:
        similarity = calculate_word_similarity(word1, word2)
        word_similarity_matrix.loc[word1, word2] = similarity

# Plot a heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(word_similarity_matrix.astype(float), annot=True, cmap='coolwarm', vmin=0, vmax=1)
plt.title('Word Similarity Heatmap (Levenshtein Distance)')
plt.show()
# Load a pre-trained BERT model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Function to calculate similarity between two words using BERT embeddings
def calculate_word_similarity(word1, word2):
    embeddings = model.encode([word1, word2])
    return 1 - cosine(embeddings[0], embeddings[1])

# Create a matrix of word similarities
word_similarity_matrix = pd.DataFrame(index=df['Name'], columns=df['Name'])
for word1 in word_similarity_matrix.index:
    for word2 in word_similarity_matrix.columns:
        similarity = calculate_word_similarity(word1, word2)
        word_similarity_matrix.loc[word1, word2] = similarity

# Plot a heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(word_similarity_matrix.astype(float), annot=True, cmap='coolwarm', vmin=0, vmax=1)
plt.title('Word Similarity Heatmap (BERT Embeddings)')
plt.show()