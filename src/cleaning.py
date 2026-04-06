import pandas as pd
import re

# Load raw data
df = pd.read_csv("data/raw/players.csv")

# Keep only relevant columns
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

# Filter out players with low minutes
df = df[df["Minutes"] >= 500].copy()

# Normalize player names for deduplication
def normalize_name(name):
    name = str(name).lower().strip()
    name = name.replace("-", " ")
    name = re.sub(r"[^a-z\s]", "", name)
    parts = name.split()
    parts.sort()
    return " ".join(parts)

df["Player_clean"] = df["Player"].apply(normalize_name)

# Sort so we keep the best version if duplicates exist
df = df.sort_values(by="Minutes", ascending=False)

# Remove duplicates using normalized name
df = df.drop_duplicates(subset=["Player_clean"])

# Drop helper column
df = df.drop(columns=["Player_clean"])

# Reset index
df = df.reset_index(drop=True)

# Save cleaned file
df.to_csv("data/processed/players_clean.csv", index=False)

print("Cleaned data saved 🚀")
print(df.to_string(index=False))