from tests import *

test_number = None

while test_number != 'q':
    test_number = input("Podaj numer testu, który chcesz wykonac :\n 1 - konkretne problemy \n 2 - Dane generowane losowo z ewentualnymi parametrami \n 3 - Losowe generowanie danych z pomiarem czasu i prezentacją wyników\n ")

    if test_number == '1':
        while True:
            str = input("Podaj numer testu, który chcesz wykonac :\n")
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

        print(image_heightP)

        parameters = [1,1,1,1]

        if image_widthP == 0:
            parameters[0] = 0
        if image_heightP == 0:
            parameters[1] = 0
        if line_numberP == 0:
            parameters[2] = 0
        if point_numberP == 0:
            parameters[3] = 0

        if parameters[0] == 1:
            if parameters[1] == 1:
                if parameters[2] == 1:
                    if parameters[3] == 1:
                        parameterized_random_test(image_width=image_widthP, image_height=image_heightP, line_number=line_numberP,point_number=point_numberP)
                    else:
                        parameterized_random_test(image_width=image_widthP, image_height=image_heightP, line_number=line_numberP)
                else:
                    if parameters[3] == 1:
                        parameterized_random_test(image_width=image_widthP, image_height=image_heightP,  point_number=point_numberP)
                    else:
                        parameterized_random_test(image_width=image_widthP, image_height=image_heightP)
            else:
                if parameters[2] == 1:
                    if parameters[3] == 1:
                        parameterized_random_test(image_width=image_widthP, line_number=line_numberP, point_number=point_numberP)
                    else:
                        parameterized_random_test(image_width=image_widthP, line_number=line_numberP)
                else:
                    if parameters[3] == 1:
                        parameterized_random_test(image_width=image_widthP, point_number=point_numberP)
                    else:
                        parameterized_random_test(image_width=image_widthP)
        else:
            if parameters[1] == 1:
                if parameters[2] == 1:
                    if parameters[3] == 1:
                        parameterized_random_test( image_height=image_heightP, line_number=line_numberP, point_number= point_numberP)
                    else:
                        parameterized_random_test( image_height=image_heightP, line_number=line_numberP)
                else:
                    if parameters[3] == 1:
                        parameterized_random_test( image_height=image_heightP, point_number=point_numberP)
                    else:
                        parameterized_random_test(image_height=image_heightP)
            else:
                if parameters[2] == 1:
                    if parameters[3] == 1:
                        parameterized_random_test( line_number=line_numberP, point_number=point_numberP)
                    else:
                        parameterized_random_test( line_number=line_numberP)
                else:
                    if parameters[3] == 1:
                        parameterized_random_test(point_number=point_numberP)
                    else:
                        parameterized_random_test()

    elif test_number == '3':
        random_test_with_results()
