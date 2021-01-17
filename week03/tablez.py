SELECT DISTINCT player_id, player_name, count(*) as num 
FROM player JOIN team ON player.team_id = team.team_id 
WHERE height > 1.80 
GROUP BY player.team_id 
HAVING num > 2 
ORDER BY num DESC 
LIMIT 2
