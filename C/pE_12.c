//project euler problem 12

#include <stdio.h>
#include <time.h> 
#include <math.h>


int main()
{
	clock_t start, end;
	start = clock();

	long int answer=0;
	long int s=0;

	for (int i=1; i<100000; i++)
	{
		s += i;
		int divisor_number=0;
		
		// find half of divisors with sqrt n
		for (int j=1; j<(int)sqrt(s); j++)
		{
			if (s%j == 0)
				divisor_number += 1;
		}
		// product with 2 and find all divisors
		divisor_number *= 2;

		if (divisor_number > 500){
			printf("answer is: %ld \n", s);
			break;}
	}

	end = clock();
	double time_taken = ((double)(end - start))/CLOCKS_PER_SEC;
	printf("time: %.3f seconds to execute \n", time_taken);
	return 0;
}

