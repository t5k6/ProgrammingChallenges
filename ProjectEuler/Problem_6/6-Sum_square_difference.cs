// Find the difference between the sum of the squares of the first one hundred natural numbers 
// and the square of the sum.

// Brute force method
void Main()
{
	double squareOfSum = Math.Pow(Enumerable.Range(1, 100).Sum(), 2);
	double sumOfSquares = Enumerable.Range(1, 100).Select(x => x*x).Sum();
	Console.WriteLine("Sum of squares ({0}) - Square of sums ({1}) is {2}", 
		squareOfSum, sumOfSquares, (squareOfSum - sumOfSquares));
}

// Mathematical method
// (a + b + .. + n)^2     = n^2 * (n+1)^2 * 1/4
// (a^2 + b^2 + .. + n^2) = n * (n+1) * (2n+1) * 1/6
// Sum of squares (25502500) - Square of sums (338350) is 25164150