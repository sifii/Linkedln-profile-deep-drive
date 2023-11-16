
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\Sifi_world\Downloads\Complete_LinkedInDataExport_11-10-2023\Complete_LinkedInDataExport_11-10-2023\Member_Follows.csv', parse_dates=['Date'])

df = df.head(500)
# Filter data for active status
active_data = df[df['Status'] == 'Active']

# Create an animated bar chart
fig, ax = plt.subplots(figsize=(10, 6))
plt.xticks(rotation=45, ha='right')
plt.title('Active Users Over Time')

def update(frame):
    plt.cla()
    current_data = active_data[active_data['Date'] <= active_data['Date'].min() + pd.to_timedelta(frame, unit='D')]
    daily_counts = current_data.groupby('Date').size()
    plt.bar(daily_counts.index, daily_counts.values, color='blue')
    plt.title('Active Users Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Active Users')

ani = FuncAnimation(fig, update, frames=(active_data['Date'].max() - active_data['Date'].min()).days + 1, interval=200)
ani.save('active_users.gif', writer='imagemagick')
