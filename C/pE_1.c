//project euler problem 1

#include <stdio.h>

int main(){
	int sum_of_numbers = 0;
	for (int i=0; i<1000; i++){
		if (i%3==0 || i%5==0)
			sum_of_numbers +=i;
	}
	printf("%d\n",sum_of_numbers);


	return 0;
}

