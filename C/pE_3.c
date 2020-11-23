//project euler problem 3


#include <stdio.h>
#define SIZE 10000


int *prime_factor();


int main(){

        int *ptr =  prime_factor();
	
	int result = 0;
	for (int i=0; i < SIZE; i++){
		if (ptr[i] == 0)
			break;
		else if (600851475143 % ptr[i] == 0 && ptr[i] >result)
			result =  ptr[i];
	}
	
	printf("%d \n", result);
	printf("\n");
	
}

int * prime_factor() {

	static int prime[SIZE];
	int index=0;
		
	for (int i=2; i < 10000; i++){
		int a = 0;
		for (int j=2; j < 10000; j++){
			if (i%j ==0 && i != j){
				a += 1;
				break;
			}
		}
		if (a == 0)
			prime[index++] = i;
	}
	
	return prime;
}


