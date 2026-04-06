import pandas as pd
import sqlite3

# Load cleaned player data
df = pd.read_csv("data/processed/players_clean.csv")

# Connect to SQLite database
conn = sqlite3.connect("scouting.db")

# Save base table
df.to_sql("players", conn, if_exists="replace", index=False)

# SQL query
query = """
SELECT
    Player,
    Team,
    Position_Group,
    Minutes,
    Goals,
    Assists,
    Goals_Per_90,
    Assists_Per_90,
    Goal_Contributions_Per_90,
    Efficiency_Rating,
    (
        0.5 * Goals_Per_90 +
        0.3 * Goal_Contributions_Per_90 +
        0.2 * Efficiency_Rating
    ) AS scouting_score
FROM players
WHERE Position_Group = 'FWD'
  AND Minutes >= 500
ORDER BY scouting_score DESC
LIMIT 10;
"""

# Run SQL query
result = pd.read_sql(query, conn)

result.to_csv("data/processed/top_forward_candidates.csv", index=False)

# Save SQL result as its own table
result.to_sql("top_forward_candidates", conn, if_exists="replace", index=False)

# Show tables in database
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("\nTables in database:")
print(tables.to_string(index=False))

# Show SQL result
print("\nTop forward candidates from SQL 🚀")
print(result.to_string(index=False))

conn.close()