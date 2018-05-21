# https://www.codewars.com/kata/century-from-year/train/ruby/5ad8c3cf32d79e88770000b2
def century(year)
    if (year % 100 == 0)
      year / 100 
    else
      year / 100 + 1
    end
  end

# https://www.codewars.com/kata/duck-duck-goose/
def duck_duck_goose(players, goose)
    players[(goose - 1) % players.length].name
end

# https://www.codewars.com/kata/even-or-odd/train/ruby
def even_or_odd(number)
  if number % 2 == 0 then 'Even' else 'Odd' end
end

# https://www.codewars.com/kata/grader/train/ruby
def grader(score)
  if    (score < 0.6) then 'F'
  elsif (score < 0.7) then 'D'
  elsif (score < 0.8) then 'C'
  elsif (score < 0.9) then 'B'
  elsif (score <= 1)  then 'A'
  else 'F'
  end
end

# https://www.codewars.com/kata/welcome-to-the-city/train/ruby
def say_hello(name, city, state)
  "Hello, #{name.join(' ')}! Welcome to #{city}, #{state}!"
end