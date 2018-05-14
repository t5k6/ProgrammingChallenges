-- https://www.codewars.com/kata/1-find-all-active-students/train/sql
SELECT * FROM students WHERE isActive;

-- https://www.codewars.com/kata/adults-only-sql-for-beginners-number-1/train/sql
SELECT name, age FROM users WHERE age > 17;

-- https://www.codewars.com/kata/best-selling-books-sql-for-beginners-number-5/train/sql
SELECT name, author, copies_sold FROM books ORDER BY copies_sold DESC LIMIT 5;

-- https://www.codewars.com/kata/collect-tuition-sql-for-beginners-number-4/train/sql
SELECT * FROM students WHERE tuition_received = false;

-- https://www.codewars.com/kata/easy-sql-convert-to-hexadecimal/train/sql
SELECT to_hex(arms) as arms, to_hex(legs) as legs FROM monsters;

-- https://www.codewars.com/kata/easy-sql-lowercase/train/sql
SELECT id, name, birthday, LOWER(race) as race FROM demographics;

-- https://www.codewars.com/kata/easy-sql-ordering/train/sql
SELECT * FROM companies GROUP BY id ORDER BY employees DESC

-- https://www.codewars.com/kata/easy-sql-squre-root-and-log/train/sql
SELECT sqrt(number1) as root, log(number2) FROM decimals

-- https://www.codewars.com/kata/even-or-odd/train/sql
SELECT
   CASE WHEN number % 2 = 0 THEN 'Even'
        ELSE 'Odd'
   END as is_even
FROM numbers;

-- https://www.codewars.com/kata/keep-hydrated-1/train/sql
SELECT id, hours, floor(hours/2) as liters FROM cycling

-- https://www.codewars.com/kata/on-the-canadian-border-sql-for-beginners-number-2/train/sql
SELECT name, country FROM travelers WHERE country not in ('USA', 'Canada', 'Mexico');

-- https://www.codewars.com/kata/register-for-the-party-sql-for-beginners-number-3/train/sql
INSERT INTO participants (name, age, attending)
VALUES ('John', 35, true);
SELECT * FROM participants;

-- https://www.codewars.com/kata/sql-basics-simple-distinct/train/sql
SELECT DISTINCT(age) FROM people

-- https://www.codewars.com/kata/sql-basics-simple-min-slash-max/train/sql
SELECT min(age) as age_min, max(age) as age_max FROM people;

-- https://www.codewars.com/kata/sql-basics-simple-sum/train/sql
SELECT sum(age) as age_sum FROM people;

-- https://www.codewars.com/kata/sql-basics-simple-where-and-order-by/train/sql
SELECT * FROM people WHERE age > 50 ORDER BY age DESC
