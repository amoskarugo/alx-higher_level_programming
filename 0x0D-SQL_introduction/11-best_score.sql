-- list all records with score >= 10 in the table second_table
-- Of database hbtn_0c_0 in MYSQL server.

SELECT score, name 
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
