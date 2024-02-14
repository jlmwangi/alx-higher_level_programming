-- lists all privileges of 2 mysql users on my serevr
SELECT
    CONCAT('SHOW GRANTS FOR ', QUOTE(user), '@', QUOTE(host), ';') AS query
FROM
    mysql.user
WHERE
    user IN ('user_0d_1', 'user_0d_2');
