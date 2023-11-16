import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from datetime import datetime
import seaborn as sns

# Read the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\Sifi_world\Downloads\Complete_LinkedInDataExport_11-10-2023\Complete_LinkedInDataExport_11-10-2023\Hashtag_Follows.csv')  # Replace 'your_filename.csv' with your actual filename


# Convert 'CreatedTime' to datetime
df['CreatedTime'] = pd.to_datetime(df['CreatedTime'])

# Word Cloud for Hashtags
all_hashtags = ' '.join(df['HashTag'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_hashtags)

plt.figure(figsize=(12, 6))

# Subplot 1: Word Cloud
plt.subplot(1, 2, 1)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud - Hashtags')

# Subplot 2: Timeline-based Heatmap
plt.subplot(1, 2, 2)
heatmap_data = df.groupby([df['CreatedTime'].dt.date, df['CreatedTime'].dt.hour])['HashTag'].count().unstack().fillna(0)
sns.heatmap(heatmap_data, cmap='YlGnBu', linewidths=0.5)
plt.title('Hashtag Timeline Heatmap')
plt.xlabel('Hour of Day')
plt.ylabel('Date')

plt.tight_layout()
plt.show()