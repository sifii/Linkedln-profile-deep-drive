import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv(r'Complete_LinkedInDataExport_11-10-2023/Connections.csv')
top_10_connections = sorted(data, key=lambda connection: connection["connected_on"], reverse=True)[:10]

print("Top 10 Most Connected With")
print("----------------------------------------------------------")
print("| Name | Company | Position | Connected On |")
print("----------------------------------------------------------")
for connection in top_10_connections:
    name = connection["name"]
    company = connection["company"]
    position = connection["position"]
    connected_on = connection["connected_on"]
    print(f"| {name} | {company} | {position} | {connected_on} |")

