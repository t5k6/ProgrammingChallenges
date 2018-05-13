//Find the sum of all the multiples of 3 or 5 below 1000.

using System;

namespace Euler_1
{
    class Program
    {
        static void Main(string[] args)
        {
            int sum = 0;
            for (int i = 0; i < 1000; i++) {
                if ((i % 3 == 0) || (i % 5 == 0)) {
                sum += i;
                }
            }
            Console.WriteLine(sum);
        }
    }
}