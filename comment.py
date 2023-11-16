import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from wordcloud import WordCloud
# Read the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\Sifi_world\Downloads\Complete_LinkedInDataExport_11-10-2023\Complete_LinkedInDataExport_11-10-2023\Comments.csv')

# Perform sentiment analysis on the 'Message' column
df['Sentiment'] = df['Message'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

# Set the figure size
plt.figure(figsize=(12, 6))

# Create a scatter plot with color-coded sentiment
sns.scatterplot(x='Date', y='Sentiment', hue='Sentiment', palette='coolwarm', size='Sentiment', sizes=(50, 200), data=df)

# Format the x-axis to show date nicely
plt.xticks(rotation=45, ha='right')

# Set y-axis labels
plt.yticks([-1, -0.5, 0, 0.5, 1], ['Negative', 'Slightly Negative', 'Neutral', 'Slightly Positive', 'Positive'])

# Add a title
plt.title('Sentiment Analysis of Messages Over Time on my comment')

# Show the plot
plt.show()
all_messages = " ".join(df['Message'].astype(str))

# Generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_messages)

# Set the figure size
plt.figure(figsize=(12, 6))

# Display the word cloud using imshow
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Turn off axis labels

# Add a title
plt.title('Word Cloud of Messages of my comment')

# Show the plot
plt.show()

