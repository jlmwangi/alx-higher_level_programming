--creates a database hbtn_0d_2 and user user_0d_2
CREATE DATABASE IF NOT EXISTS htbn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2';
