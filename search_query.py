import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px

# Assuming the CSV file is named 'search_data.csv'
df = pd.read_csv(r'C:\Users\Sifi_world\Downloads\Complete_LinkedInDataExport_11-10-2023\Complete_LinkedInDataExport_11-10-2023\SearchQueries.csv')

# Convert 'Time' column to datetime format
df['Time'] = pd.to_datetime(df['Time'])

# Extract month and year from the 'Time' column
df['Month'] = df['Time'].dt.to_period('M')

# Group by month and count the number of searches
monthly_counts = df.groupby('Month').size()

# Plotting the timeline
plt.figure(figsize=(12, 6))
monthly_counts.plot(marker='o', linestyle='-', color='orange')
plt.title('Search Query Timeline')
plt.xlabel('Month')
plt.ylabel('Number of Searches')
plt.grid(True)
plt.show()

# Take only the first 30 rows
df_subset = df.head(60)

# Create a hierarchical structure for the sunburst chart
fig = px.sunburst(df_subset, path=['Search Query'], title='hierarchical structur of Search Queries ')

# Show the plot
fig.show()