import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
from gensim.models import Word2Vec
import networkx as nx
df = pd.read_csv(r'C:\Users\Sifi_world\Downloads\Complete_LinkedInDataExport_11-10-2023\Complete_LinkedInDataExport_11-10-2023\Ad_Targeting.csv')
print(df)


# Convert all columns to strings
df = df.apply(lambda col: col.astype(str))

# Apply the operation to count unique items in each column
column_item_counts = df.apply(lambda col: col.str.split(';').explode().str.strip().nunique())

# Display the counts
print(column_item_counts)
# Set up data for the bubble chart
columns = column_item_counts.index
counts = column_item_counts.values
colors = np.arange(len(columns))

# Plot the bubble chart
plt.figure(figsize=(12, 8))
plt.scatter(x=columns, y=np.ones_like(counts), s=counts * 100, c=colors, cmap='viridis', alpha=0.7)
plt.title('Count of Unique Items in Each Column (Bubble Chart)')
plt.xlabel('Columns')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.colorbar(label='Color Intensity')
plt.show()



# Generate a word cloud for member interests
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(df['Member Interests'].str.split(';').explode().str.strip().value_counts())

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud for Member Interests')
plt.show()

job_titles = df['Job Titles'].str.split(';').explode().str.strip()
common_job_titles = job_titles.value_counts()

# Convert the Series to a list of tuples (job_title, count)
job_titles_list = list(zip(common_job_titles.index, common_job_titles.values))

# Display the list
print(job_titles_list)

# Select the top 6 common job titles
top_job_titles = common_job_titles.head(6).index.tolist()

# Create a list of sentences for Word2Vec training
sentences = df['Job Titles'].apply(lambda x: [job.strip() for job in x.split(';')]).tolist()

# Train Word2Vec model
model = Word2Vec(sentences, window=5, min_count=1, workers=4)

# Create a graph using the Word2Vec model
G = nx.Graph()
for job_title in top_job_titles:
    G.add_node(job_title)
    for similar_title, score in model.wv.most_similar(job_title, topn=3):
        G.add_edge(job_title, similar_title, weight=score)

# Visualize the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_size=8, font_color='blue', node_color='skyblue', edge_color='gray', width=1.5, alpha=0.8)
plt.title('Word2Vec Similarity Graph for Top 6 Job Titles')
plt.show()


