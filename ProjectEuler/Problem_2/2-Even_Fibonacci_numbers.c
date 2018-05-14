#include <stdio.h>

void main()
{
	int sum = 0;
	int x = 1;
	int y = 1;
	
	while (y < 4000000)
	{
	    x = x ^ y;
	    y = y ^ x;
	    x = (x ^ y) + y;
	    if (y % 2 == 0)
	    {
	        sum += y;
	    }
	}
	printf("%d\n", sum); // 4613732
}