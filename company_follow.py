import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns
import plotly.express as px
# Read the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\Sifi_world\Downloads\Complete_LinkedInDataExport_11-10-2023\Complete_LinkedInDataExport_11-10-2023\Company Follows.csv')

df['Followed On'] = pd.to_datetime(df['Followed On'])

# Extract the month and year from the 'Followed On' column
df['Month'] = df['Followed On'].dt.to_period('M')

# Count the number of follows per month
monthly_follows = df['Month'].value_counts().sort_index()

# Set a custom style
plt.style.use('seaborn-darkgrid')

# Plotting the data
plt.figure(figsize=(12, 8))
ax = sns.barplot(x=monthly_follows.index.astype(str), y=monthly_follows.values, palette='viridis')

# Adding annotations
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

# Adding a title and labels
plt.title('Monthly Trend of Follows', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Number of Follows', fontsize=14)

# Rotating x-axis labels for better readability
plt.xticks(rotation=45, ha='right', fontsize=12)

# Show the plot
plt.show()

# Convert the 'Followed On' column to datetime format
df['Followed On'] = pd.to_datetime(df['Followed On'])

# Extract day of the week and hour of the day
df['Day of Week'] = df['Followed On'].dt.day_name()
df['Hour of Day'] = df['Followed On'].dt.hour

# Create a pivot table for the heatmap
heatmap_data = df.pivot_table(index='Day of Week', columns='Hour of Day', aggfunc='size', fill_value=0)

# Plotting the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, cmap='viridis', annot=True, fmt='d', linewidths=.5)
plt.title('Day-of-Week and Time-of-Day Patterns of Follows')
plt.show()

# Convert the 'Followed On' column to datetime format
df['Followed On'] = pd.to_datetime(df['Followed On'])

# Extract the month and year from the 'Followed On' column and convert to string
df['Month'] = df['Followed On'].dt.to_period('M').astype(str)

# Count the number of follows per month for each organization
df_counts = df.groupby(['Organization', 'Month']).size().reset_index(name='Count')

# Plotting a bar chart with Plotly Express
fig = px.bar(df_counts, x='Month', y='Count', color='Organization',
             labels={'Count': 'Number of Follows', 'Month': 'Month'},
             title='Number of Follows per Month for Each Organization')

fig.show()

