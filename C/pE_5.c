//project euler problem 5


#include <stdio.h>
#include <math.h>

int main(){
	int s = 1;
	for (int i=1; i<21; i++){
		for (int j=1; j<5; j++){
			int square = pow(i,j);
			if (square < 21 && s%square != 0)
				s *= i;
			
		}
	}
        printf("%d\n", s);
	return 0;
}

