#Ignacy Ślusarczyk
#Nr indeksu: 261521
#islusarc@mion.elka.pw.edu.pl
#Algorytm kolorowania obszarów spójnych
from tests import *

test_number = None

while test_number != 'q':
    test_number = input(" 1 - konkretne problemy \n "
                        "2 - Dane generowane losowo z ewentualnymi parametrami \n "
                        "3 - Losowe generowanie danych z pomiarem czasu i prezentacją wyników\n "
                        "4 - Dane testowe z generacja tabeli\n"
                        "Podaj numer testu, który chcesz wykonac:\n ")

    if test_number == '1':
        while True:
            str = input(" 1 - Zamalowywanie  trojkata\n"
                        " 2 - Zamalowywanie kwadratu\n"
                        " 3 - Zamalowywanie prostokata\n"
                        " 4 - Zamalowywanie rombu\n"
                        " 5 - Zamalowywanie nieokreślonej figury\n"
                        " 6 - Zamalowywanie trojkata o dlugich ramionach\n"
                        " 7 - Pare podstawowych figur\n"
                        "Podaj numer testu, który chcesz wykonac lub 0 aby powrocic:\n")
            if specific_test(int(str)) == 0 or int(str) > 7 :
                break
    elif test_number == '2':
        try:
            print("Dla domyslnych wartosci wpisz 0")
            image_widthP = int(input("Podaj szerokosc obrazka\n"))
            image_heightP = int(input("Podaj wysokosc obrazka\n"))
            line_numberP = int(input("Podaj liczbę linii do wygenerowania\n"))
            point_numberP = int(input("Podaj liczbę punktow startowych do wygenerowania\n"))

        except ValueError:
            print("Podana wartosc nie jest liczba calkowita. Program wroci do menu")
            continue


        if image_widthP == 0:
            image_widthP = 600
        if image_heightP == 0:
            image_heightP = 400
        if line_numberP == 0:
            line_numberP = 20
        if point_numberP == 0:
            point_numberP = 20

        parameterized_random_test(image_widthP,image_heightP,line_numberP,point_numberP)

    elif test_number == '3':
        random_test_with_results()
    elif test_number == '4':
        array_results_tests()
