# https://www.codewars.com/kata/sum-of-two-lowest-positive-integers/train/elixir
defmodule SmallSummer do
  def sum_two_smallest_numbers(numbers) do
    Enum.sort(numbers) |> Enum.take(2) |> Enum.sum
  end
end
