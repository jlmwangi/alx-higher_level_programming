-- lists number of records with the same score
SELECT t1.score, COUNT(*) AS number
FROM hbtn_0c_0.second_table AS t1
JOIN hbtn_0c_0.second_table AS t2 ON t1.score = t2.score
GROUP BY t1.score
ORDER BY number DESC;
