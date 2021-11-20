
/* @BEGIN_OF_SOURCE_CODE */

#include <iostream>

using namespace std;
static int tempCount = 1;


long cycleLength (long value);
void maxLength(long, long, bool);


int main()
{
    while(true)
    {
        long start, end;
        cin  >> start >> end;
        
        if(!cin) break;
        
        if(start > end) maxLength(end, start, false);
        //else maxLength(start, end, true);
    }
}


long cycleLength (long value)
{
    if (value != 1 and value != 0)
    {
        // Get cycle length
        tempCount++;
        
        if (value%2==0)
            cycleLength(value/2);
        else
            cycleLength(value*3+1);
    }
    return tempCount;
}

void maxLength(long start, long end, bool a)
{
    long longestCycleLength = 0;
        
    for (long i=start; i<=end; i++)
    {
        long tempLength =  cycleLength(i);
        if (longestCycleLength < tempLength)
            longestCycleLength = tempLength;
        tempCount = 1;
    }
    if(a)
        cout << start << " " << end << " " << longestCycleLength << endl;
    else 
        cout << end << " " << start << " " << longestCycleLength << endl;

}

/* @END_OF_SOURCE_CODE */