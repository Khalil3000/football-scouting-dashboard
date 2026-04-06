import pandas as pd

# Load data
df = pd.read_csv("data/raw/players.csv")

# Vælg relevante kolonner
columns_to_keep = [
    "Player",
    "Team",
    "Position_Group",
    "Minutes",
    "Goals",
    "Assists",
    "Goals_Per_90",
    "Assists_Per_90",
    "Goal_Contributions_Per_90",
    "Efficiency_Rating"
]

df = df[columns_to_keep]

# Fjern spillere med få minutter (vigtigt!)
df = df[df["Minutes"] > 500]


# Reset index
df = df.reset_index(drop=True)

# Gem renset data
df.to_csv("data/processed/players_clean.csv", index=False)



print("Cleaned data saved 🚀")
print(df.head())