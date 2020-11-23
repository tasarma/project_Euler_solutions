//euler project problem 9

#include <stdio.h>
#include <math.h>

int main(){
	for (int i=1; i<1000; i++)
	{
	       for (int j=1; j<1000; j++)
	       {
		       long double c = sqrt(i*i + j*j);
		       if (i+c+j == 1000)
		       {
			       printf("%.0Lf \n", i*j*c);
			       break;
		       }
	       }
	}
}	

