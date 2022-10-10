#include <iostream>

#include "game.cpp"
#include "rules.cpp"

using namespace std;

int main()
{

    int choice = 0;

    cout << " ----- Welcome in NumberGuess! ----- " << endl << endl;

    cout << "Choose Your Action:" << endl;
    cout << "1. PLay (Easy)" << endl;
    cout << "2. Play (Middle)" << endl;
    cout << "3. Play (Hard)" << endl;
    cout << "4. Rules!" << endl;
    cout << "5. Exit" << endl;


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
            cout << "Error 890!";
            break;
    }

    return 0;
}