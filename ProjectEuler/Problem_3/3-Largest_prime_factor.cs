void Main()
{
	double x = 600851475143;
	for (int i = (int) Math.Sqrt(x)+1; i > 3; i -= 2) {
		if (x % i == 0 && isPrime(i)) {
			Console.WriteLine("Largest prime factor of {0} is {1}", x, i);
			break;
		}
	}
}

bool isPrime(double num)
{
	if (num < 2) return false;
	if (num == 2 || num == 3) return true;
	if (num % 2 == 0 || num % 3 == 0) return false;
	foreach (int i in Enumerable.Range(3, (int) Math.Sqrt(num) + 1))
	{
		if (num % i == 0) return false;
	}
	return true;
}
// Largest prime factor of 600851475143 is 6857