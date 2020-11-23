//projecy euler problem 2

#include <stdio.h>

int a,b= 1;
int c;
int s = 0;

int main(){

	while(a <= 4000000){
		c=a;
		a=b;
		b = a+c;		
		if (b%2==0){
			s +=b;
		}
	}
	printf("%d \n", s);

}

