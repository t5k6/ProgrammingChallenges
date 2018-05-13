# Find the sum of all the multiples of 3 or 5 below 1000.
Enum.filter(0..999, (&(rem(&1, 3) == 0 or rem(&1, 5) == 0)) ) |> Enum.sum