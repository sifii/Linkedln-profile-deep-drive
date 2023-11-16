import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np
from wordcloud import WordCloud
import networkx as nx
from matplotlib.animation import FuncAnimation
file_path = r'Complete_LinkedInDataExport_11-10-2023/Connections.csv'
df = pd.read_csv(file_path, parse_dates=['Connected On'])


# Filter for the top 20 companies
top_companies = df['Company'].value_counts().nlargest(20).index
df_top20 = df[df['Company'].isin(top_companies)]

# Create a network graph
G = nx.from_pandas_edgelist(df_top20, 'First Name', 'Last Name')

# Get positions of nodes
pos = nx.spring_layout(G)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Set up the initial plot with no edges
nx.draw_networkx_nodes(G, pos, node_size=50, node_color='red', alpha=0.7)
edges = nx.draw_networkx_edges(G, pos, width=0.5, alpha=0)

# Function to update the plot for each frame
def update(frame):
    edges.set_alpha(frame / 50)  # Gradually increase edge transparency
    return edges,


plt.title('Network Graph of Persons in the Same Company')

# Create an animation
ani = FuncAnimation(fig, update, frames=50, interval=100)

# Save the animation as a GIF
ani.save('dynamic_network.gif', writer='imagemagick', fps=10)
plt.show()


# Extract month and year from the 'Connected On' column
df['Month'] = df['Connected On'].dt.strftime('%b %Y')

# Use XKCD style
with plt.xkcd():
    # Visualization 1: Number of connections per month
    plt.figure(figsize=(12, 6))
    ax = sns.countplot(x='Month', data=df, palette='viridis')
    plt.title('Number of Connections per Month')
    plt.xticks(rotation=45)

    # Add count values on top of each bar
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 10), textcoords='offset points')

    plt.show()
# Visualization 2: Companies with the most connections (top 20)
top_companies = df['Company'].value_counts().nlargest(20).index

# Use XKCD style with shadows
with plt.xkcd():
    plt.figure(figsize=(12, 8))
    ax = sns.countplot(y='Company', data=df, order=top_companies, palette='muted', edgecolor='black')
    plt.title('Top 20 Companies with the Most Connections')

    # Add count values on top of each bar
    for p in ax.patches:
        ax.annotate(f'{p.get_width()}', (p.get_width(), p.get_y() + p.get_height() / 2.),
                    ha='center', va='center', xytext=(10, 0), textcoords='offset points')

    plt.show()



# Extract the first letter of each person's first name
df['First Letter'] = df['First Name'].str[0]

# Filter only letters from 'A' to 'Z'
filtered_df = df[df['First Letter'].str.isalpha() & df['First Letter'].str.isupper()]

# Count the number of persons for each first letter
letter_counts = filtered_df['First Letter'].value_counts().sort_index()

# Generate a gradient color scheme
colors = plt.cm.viridis(np.linspace(0, 1, len(letter_counts)))

# Explode a few slices for emphasis
explode = np.full(len(letter_counts), 0.1)  # Set the same explode value for all slices

# Plot the results using a pie chart with improved styling
plt.figure(figsize=(12, 12))
plt.pie(letter_counts, labels=letter_counts.index, startangle=90, colors=colors, wedgeprops=dict(width=0.4, edgecolor='w'), explode=explode)
plt.title('Distribution of Persons by First Letter of First Name (A to Z) in my connection')
plt.show()


# Extract the date from the 'Connected On' column
df['Date'] = df['Connected On'].dt.date

# Count the number of connections for each date
connection_counts = df['Date'].value_counts().sort_index()


# Drop rows with missing company names
df = df.dropna(subset=['Company'])

# Count the number of connections for each company
company_counts = df['Company'].value_counts().head(20)  # Top 20 companies

# Plot the distribution using a bubble chart
plt.figure(figsize=(12, 8))
plt.scatter(company_counts.index, company_counts.values, s=company_counts.values * 20, color='skyblue', alpha=0.7)
plt.title('Distribution of LinkedIn Connections by Company')
plt.xlabel('Company')
plt.ylabel('Number of Connections')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()




# Drop rows with missing positions
df = df.dropna(subset=['Position'])

# Analyze the distribution of positions
position_counts = df['Position'].value_counts().head(10)

# Use a creative style - 'seaborn-dark-palette'
plt.style.use('seaborn-dark-palette')

# Use XKCD style for the plot
with plt.xkcd():
    plt.figure(figsize=(12, 6))
    ax = position_counts.plot(kind='bar', color='black', edgecolor='black')

    # Add XKCD-style annotations
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 10), textcoords='offset points', fontsize=10)

    plt.title('Top 10 Positions Among LinkedIn Connections')
    plt.xlabel('Position')
    plt.ylabel('Number of Connections')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Drop rows with missing positions
df = df.dropna(subset=['Position'])

# Concatenate all positions into a single string
positions_text = ' '.join(df['Position'].astype(str).tolist())

# Generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(positions_text)

# Plot the word cloud
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of LinkedIn Connection Positions')
plt.show()
