//euler project problem 10

//https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

#include <stdio.h>
#include <time.h> 
#include <stdbool.h> 

int main()
{
	clock_t start, end;
	start = clock();

	long int sum = 0, no = 2000000;
	long int i, j;
	bool sieve[no];
	
	for (i=0; i<no; i++)
		sieve[i] = true;

	for (i=2; i<no; i++)
	{
		if (sieve[i])
		{
			sum += i;
			for (j=i*i; j<no; j += i)
				sieve[j] = false;
		}
	}
	printf("answer %ld \n", sum);


	end = clock();
	double time_taken = ((double)(end - start))/CLOCKS_PER_SEC;
	printf("time: %.3f seconds to execute \n", time_taken);
	return 0;
}


