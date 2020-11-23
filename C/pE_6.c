// project euler problem 6

#include <stdio.h>

int main(){
	int sum1 = 0;
	int sum2 = 0;
	for (int i=1; i<101; i++){
		sum1 += i;
		sum2 += i*i;
	}
	printf("%d \n", sum1*sum1 - sum2);

}

