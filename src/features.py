import pandas as pd
import re

# Load data
df = pd.read_csv("data/processed/players_clean.csv")

def normalize_name(name):
    name = str(name).lower().strip()
    name = name.replace("-", " ")
    name = re.sub(r"[^a-z\s]", "", name)
    parts = name.split()
    parts.sort()
    return " ".join(parts)

# Lav standardiseret navn
df["Player_clean"] = df["Player"].apply(normalize_name)

# Debug: se hvordan Son-navnene bliver standardiseret
print("\nName check:")
print(df[df["Player"].str.contains("Son|Heung", case=False, na=False)][["Player", "Player_clean"]])

# Fjern dubletter på standardiseret navn
df = df.drop_duplicates(subset=["Player_clean"])

# Fokus på forwards
forwards = df[df["Position_Group"] == "FWD"].copy()

# Scouting score
forwards["scouting_score"] = (
    0.5 * forwards["Goals_Per_90"] +
    0.3 * forwards["Goal_Contributions_Per_90"] +
    0.2 * forwards["Efficiency_Rating"]
)

# Sortér
forwards = forwards.sort_values(by="scouting_score", ascending=False)

# Top 10
top_players = forwards.head(10)

print("\nTop Forward Candidates:")
print(top_players[["Player", "Team", "scouting_score"]])