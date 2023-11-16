import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming the CSV file is named 'login_data.csv'
df = pd.read_csv(r'C:\Users\Sifi_world\Downloads\Complete_LinkedInDataExport_11-10-2023\Complete_LinkedInDataExport_11-10-2023\Logins.csv')
# Convert 'Login Date' to datetime format
df['Login Date'] = pd.to_datetime(df['Login Date'])

# Visualize login frequency over time
plt.figure(figsize=(12, 6))
sns.histplot(df['Login Date'], bins=20, kde=True, color='skyblue')
plt.title('Login Frequency Over Time')
plt.xlabel('Login Date')
plt.ylabel('Frequency')
plt.show()

# Visualize login types
plt.figure(figsize=(8, 6))
sns.countplot(x='Login Type', data=df, palette='pastel')
plt.title('Distribution of Login Types')
plt.xlabel('Login Type')
plt.ylabel('Count')
plt.show()

# Visualize the distribution of IP addresses
plt.figure(figsize=(14, 6))
sns.countplot(x='IP Address', data=df, palette='viridis', order=df['IP Address'].value_counts().index)
plt.title('Distribution of Login IP Addresses')
plt.xlabel('IP Address')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.show()

# Visualize the distribution of user agents
plt.figure(figsize=(14, 6))
sns.countplot(x='User Agent', data=df, palette='muted', order=df['User Agent'].value_counts().index)
plt.title('Distribution of User Agents')
plt.xlabel('User Agent')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.show()

# Take only the first 30 rows
df_subset = df.head(40)

# Create a 3D scatter plot
fig = px.scatter_3d(df_subset, x='Login Date', y='IP Address', z='User Agent',
                    color='Login Type', title='3D Scatter Plot of Login Data (First 30 Rows)')

# Show the plot
fig.show()
# Create a parallel coordinates plot
fig = px.parallel_coordinates(df_subset, color='Login Type', labels={'Login Date': 'Date', 'IP Address': 'IP', 'User Agent': 'Agent'},
                              title='Parallel Coordinates Plot of Login Data (First 30 Rows)')

# Show the plot
fig.show()