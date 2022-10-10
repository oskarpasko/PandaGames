#include <iostream>
#include <cstdlib>

using namespace std;

void play(int minNumber, int maxNumber, int attempt)
{
    // Providing a seed value
    srand((unsigned) time(NULL));

    //rownanie, ktore losuje liczbe z przedzialu minNum - maxNum
    int random = minNumber + (rand() % maxNumber);
    int choice = 0;

    cout << "Choose number from " << minNumber << " to " << maxNumber << endl << endl;

    for(int i = 0 ; i < attempt ; i++)
    {
        if(i == (attempt - 1)) cout << "This is Your last chance!" << endl;
        cout << "Choose Youe number: " ;
        cin >> choice;

        if(choice == random)
        {
            cout << endl << "Bravo, You got this!"<<endl;
            cout << "That was Your " << i+1 << " shoot!" << endl;
            break;
        } else if(choice > random){
            cout << "Too much!" << endl << endl;
        } else if(choice < random){
            cout << "Too few!" << endl << endl;
        }

    }

}