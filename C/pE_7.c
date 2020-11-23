//project euler problem 7

#include <stdio.h>

int main(){
	int s = 0;
	for (int i=2; i<1000000000; i++){
		int a = 0;
		for (int j=2; j<i; j++){
			if (i%j == 0){
				a += 1;
				break;}
		}
		if (a == 0)
			s += 1;
		
		if (s== 10001){
			printf("%d \n", i);
			break;
		}
	}
}

