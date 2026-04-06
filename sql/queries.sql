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