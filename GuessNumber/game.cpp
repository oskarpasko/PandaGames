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

    cout << "Zgadnij liczbe z przedzialu od " << minNumber << " do " << maxNumber << endl << endl;

    for(int i = 0 ; i < attempt ; i++)
    {
        if(i == (attempt - 1)) cout << "To Twoj ostatni strzal!" << endl;
        cout << "Wybierz liczbe: " ;
        cin >> choice;

        if(choice == random)
        {
            cout << endl << "Brawo, to ta liczba ktora wylosowalismy!"<<endl;
            cout << "To byl Twoj " << i+1 << " strzal!" << endl;
            break;
        } else if(choice > random){
            cout << "Za duzo!" << endl << endl;
        } else if(choice < random){
            cout << "Za malo!" << endl << endl;
        }

    }

}