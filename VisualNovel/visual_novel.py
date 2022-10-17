from settings import text_display

def test():
    text_display('Otwierasz oczy, widzisz zadymione pole walki.\n\n')

    print('Główny bohater')
    text_display('Ugh, co się stało?\n\n')

    print('Brat')
    text_display('Dostales kamieniem w leb, co gorsze nasz ojciec nie zyje...\n\n')

    print('Główny bohater')
    text_display('Co?! Jak to nie zyje?\n\n')

    print('Brat')
    text_display('Nie wiem co sie stalo, musiał to zrobić ten zdradziecki Mag!\n\n')

    text_display('Spoglądasz na Maga, który wychowywał Cię przez całe zycie\n')
    text_display('Siedzi ledwo zywy przy kamieniu próbując uleczyć swoje rany\n\n')

    print('Główny bohater')
    text_display('Magu? Ty? Jak mogłeś to uczynić? Ojciec ufał Ci całym swoim zyciem!!!\n\n')

    print('Mag')
    text_display('Ja... Przepraszam ...\n\n')

    print('Wybór:\n1.Zabij Maga\n2.Wysłuchaj Maga\n')
    choice = input()

    match(choice):
        case '1':
            print('Główny Bohater\n')
            text_display('Zabije Cię! Rozumiesz Zabi....\n\n')

            print('Czujesz nagły ból przeszywający całe Twoje ciało, nie mozesz się ruszyć. Mdlejesz')    
        case '2':
            print('Główny Bohater\n')
            text_display('Jak mozesz przeraszać? Zabiłeś mojego ojca!\n\n')

            print('Mag\n')
            text_display('Przepraszam, ze go nie urotowałem przed Twoim bratem\n\n')

            print('Czarodziej odpływa a Ty nagle czujesz nagły ból przeszywający całe Twoje ciało\n')
            print('Nie mozesz się ruszyć. Mdlejesz\n\n')
        case _:
            print('Umierasz!\n')
            exit(0)

    print('Nieznajoma')
    text_display('Obudził się, obudził się!')
test()