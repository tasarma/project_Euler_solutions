
/* @BEGIN_OF_SOURCE_CODE */

#include <iostream>
#include <string>
#include <sstream>

using namespace std;


// void get_inputs (int *arr, unsigned int size);
void minesweeper( int arr [], int size);

int main()
{
    while(true)
    {
        // Get dimension of matrix
        int row, column;
        cin >> row >> column;
        
        char mines[4];

        for (int i=0; i<4; i++){
            cin >> mines[i];
        }
        for (int i=0; i<4 ; i++)
            cout << mines[i] << endl;
        
        // Break if inputs are not proper
        if(!cin) break;

        // Store variables in a array
        int arr[row][column];
        for (int i=0; i < row; i++)
        {
            for (int j=0; j < column; j++)
            {
                
            }

        }
        //minesweeper()
    }

    cout << endl;
}



/* @END_OF_SOURCE_CODE */