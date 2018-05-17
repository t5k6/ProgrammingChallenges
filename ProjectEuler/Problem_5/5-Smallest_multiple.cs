// Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

// Mathematical shortcut / multiplying primes < 20
void Main()
{
    int x = 19 * 17 * 13 * 11 * 7 * 5 * 3 * 2; //9699690
    bool found = false;
    while (!found)
    {
        for (int j = 1; j < 21; j++)
        {
            if (x % j > 0) break;
            else if (j == 20 && x % j == 0)
            {
                Console.WriteLine("Smallest multiple number is: {0}", x);
                found = true;
            }
        }
        x += 9699690;
    }
}
// Smallest multiple number is: 232792560
