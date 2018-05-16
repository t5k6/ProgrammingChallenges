// Find the largest palindrome made from the product of two 3-digit numbers.'''

void Main()
{
	int largest = 0;
	for (int i = 999; i > 900; i--)
	{
		for (int j = 999; j > 900; j--)
			{
				if (i * j % 11 == 0 && isPalindrom(i*j) && i*j > largest) {
					largest = i*j;
				}
			}
	}
	Console.WriteLine("largest palindrom from i*j is: {0}", largest);
}

bool isPalindrom (int num) => Reverse(num.ToString()) == num.ToString();

public static string Reverse( string s )
{
    char[] charArray = s.ToCharArray();
    Array.Reverse( charArray );
    return new string( charArray );
}