// What is the 10001st prime number?

void Main()
{
    int n = 1;
    double i = 3;

    while (n != 10000)
    {
        if (isPrime(i))
        {
            n += 1;
        }
        i += 2;
    }
    Console.WriteLine(i - 2);
}

// Define other methods and classes here
bool isPrime(double num)
{
    if (num < 2) return false;
    if (num == 2 || num == 3) return true;
    if (num % 2 == 0 || num % 3 == 0) return false;
    foreach (int i in Enumerable.Range(3, (int)Math.Sqrt(num) + 1))
    {
        if (num % i == 0) return false;
    }
    return true;
}
// 10001 prime is 104743