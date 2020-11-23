// project euler problem 4

#include <stdio.h>

int reversed(char no[6]){
	if (no[0] == no[5] && no[1] == no[4] && no[2] == no[3]){
		return 1; }
	return 0; }

int main(){

	int answer = 1;
	for ( int i=1; i < 1000; i++){
		for (int j=1; j<1000; j++){
			int a = i*j;
			char b[6];
		       	sprintf(b,"%d",a);
			if (reversed(b) && a%11==0){
				if (a>answer)
					answer=a;
			}
		}
	}
	printf("answer is : %d \n", answer);
	return 0;
}



