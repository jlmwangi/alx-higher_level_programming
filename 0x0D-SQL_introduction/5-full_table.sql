-- prints full description of the table
SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, CHRACTER_MAXIMUM_LENGTH
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';