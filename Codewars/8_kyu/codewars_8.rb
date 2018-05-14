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