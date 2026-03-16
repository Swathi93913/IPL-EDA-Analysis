import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
matches = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\IPL_EDA_Project\matches.csv.csv")
deliveries = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\IPL_EDA_Project\deliveries.csv.csv")

print("Matches Dataset Preview:")
print(matches.head())

# 1️⃣ Most Winning Teams
wins = matches['winner'].value_counts()

plt.figure(figsize=(10,6))
wins.plot(kind='bar')
plt.title("Most Winning IPL Teams")
plt.xlabel("Teams")
plt.ylabel("Number of Wins")
plt.show()

# 2️⃣ Top Run Scorers
top_scorers = deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
top_scorers.plot(kind='bar', color='orange')
plt.title("Top 10 IPL Run Scorers")
plt.xlabel("Players")
plt.ylabel("Total Runs")
plt.show()

# 3️⃣ Matches Played in Each Stadium
stadiums = matches['venue'].value_counts().head(10)

plt.figure(figsize=(10,6))
stadiums.plot(kind='bar', color='green')
plt.title("Top IPL Stadiums by Matches Played")
plt.xlabel("Stadium")
plt.ylabel("Number of Matches")
plt.show()
