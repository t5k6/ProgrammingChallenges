-- https://www.codewars.com/kata/easy-sql-absolute-value-and-log-to-base
select abs(number1), log(64, number2) from decimals;

-- https://www.codewars.com/kata/easy-sql-bit-length/train/sql
SELECT 
  id, bit_length(name) AS name, birthday, bit_length(race) AS race
FROM demographics;

-- https://www.codewars.com/kata/easy-sql-counting-and-grouping/train/sql
SELECT race, COUNT(race) FROM demographics 
GROUP BY race ORDER BY count(race) DESC;

-- https://www.codewars.com/kata/hello-sql-world/train/sql
SELECT 'hello world!' as Greeting

-- https://www.codewars.com/kata/sql-basics-create-a-function/train/sql
CREATE FUNCTION increment(i integer) RETURNS integer AS $$
  BEGIN
          RETURN i + 1;
  END;
$$ LANGUAGE plpgsql;
-- alternative: 
CREATE FUNCTION increment1(i integer) RETURNS integer
AS 'select $1 + 1;'
LANGUAGE sql;

-- https://www.codewars.com/kata/sql-basics-position/train/sql
SELECT id, name, POSITION(',' in characteristics) as comma
FROM monsters
ORDER BY comma

-- https://www.codewars.com/kata/sql-basics-repeat-and-reverse-1/train/sql
SELECT 
  repeat(name, 3) as name, reverse(characteristics) as characteristics
FROM monsters

-- https://www.codewars.com/kata/sql-basics-simple-group-by/train/sql
SELECT age, count(id) as people_count FROM people GROUP BY age

-- https://www.codewars.com/kata/sql-basics-simple-join/train/sql
SELECT 
  p.id, p.name, p.isbn, p.company_id, p.price, c.name as company_name
  -- alternative: products.*, c.name AS company_name
FROM
  products p
  JOIN companies c on p.company_id = c.id

-- https://www.codewars.com/kata/sql-basics-simple-join-with-count/train/sql
SELECT 
  people.*, count(toys.id) as toy_count
FROM 
  people JOIN toys on people.id = toys.people_id
GROUP BY people.id

-- https://www.codewars.com/kata/sql-basics-trimming-the-field/train/sql
SELECT id, name, 
  split_part(characteristics, ',', 1) AS characteristic
FROM monsters ORDER BY id

-- https://www.codewars.com/kata/sql-concatenating-columns/train/sql
SELECT concat_ws(' ', prefix, first, last, suffix) as title FROM names 

-- https://www.codewars.com/kata/sql-right-and-left/train/sql
SELECT LEFT(project, commits) as project, RIGHT(address, contributors) as address FROM repositories 