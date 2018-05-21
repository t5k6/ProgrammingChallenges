# https://www.codewars.com/kata/even-or-odd/train/elixir
def even_or_odd(number) do
  if rem(number, 2) == 0, do: "Even", else: "Odd"
end

# http://www.codewars.com/kata/thinkful-number-drills-pixelart-planning/train/elixir
def is_divisible(wall_length, pixel_size) do
  rem(wall_length, pixel_size) == 0
end