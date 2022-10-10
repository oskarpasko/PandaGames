#include <iostream>

#include "game.cpp"
#include "rules.cpp"

using namespace std;

int main()
{

    int choice = 0;

    cout << " ----- Witamy w NumberGuess! ----- " << endl << endl;

    cout << "Wybierz akcje:" << endl;
    cout << "1. Graj (latwy)" << endl;
    cout << "2. Graj (sredni)" << endl;
    cout << "3. Graj (trudny)" << endl;
    cout << "4. Zasady" << endl;
    cout << "5. Wyjdz" << endl;


    cin >> choice;

    switch(choice)
    {
        case 1:
            play(0, 10, 5);
            break;
        case 2:
            play(0, 100, 10);
            break;
        case 3:
            play(0, 1000, 20);
        case 4:
            rules();
            break;
        case 5:
            exit(1);
        default:
            cout << "Error 890";
            break;
    }

    return 0;
}