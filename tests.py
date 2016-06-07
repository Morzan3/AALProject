#Ignacy Ślusarczyk
#Nr indeksu: 261521
#islusarc@mion.elka.pw.edu.pl
#Algorytm kolorowania obszarów spójnych
from UserImage import *

def specific_test(test_number):
    if test_number == 1:
        triangle_test()
    elif test_number == 2:
        square_test()
    elif test_number == 3:
        rectangle_test()
    elif test_number == 4:
        diamond_test()
    elif test_number == 5:
        custom_test()
    elif test_number == 6:
        sharp_test()
    elif test_number == 7:
        multi_test()
    else:
        return 0


def random_test():
    picture = UserImage(600, 400)

    picture.display_image()
    for i in range(0,20):
        draw_random_lines(picture)

    picture.display_image()
    for i in range(0,20):
        generate_random_start_algorythm(picture)

    picture.display_image()


def parameterized_random_test(image_width, image_height, line_number, point_number):
        picture = UserImage(image_width, image_height)
        picture.display_image()

        for i in range(0, line_number):
            draw_random_lines(picture)
        picture.display_image()

        for i in range(0, point_number):
            generate_random_start_algorythm(picture)
        picture.display_image()
        display_picture_algorythm_information(picture)

def random_test_with_results():

    picture = UserImage(800, 600)
    line_number = randint(0, 30)
    point_number = randint(0, 30)

    if point_number > line_number:
        point_number = line_number

    for i in range(0, line_number):
        draw_random_lines(picture)

    for i in range(0, point_number):
        generate_random_start_algorythm(picture)

    picture1 = UserImage(800, 600)

    line_number = randint(0, 30)
    point_number = randint(0, 30)

    if point_number > line_number:
        point_number = line_number

    for i in range(0, line_number):
        draw_random_lines(picture1)

    for i in range(0, point_number):
        generate_random_start_algorythm(picture1)

    picture2 = UserImage(800, 600)
    line_number = randint(0, 30)
    point_number = randint(0, 30)

    if point_number > line_number:
        point_number = line_number

    for i in range(0, line_number):
        draw_random_lines(picture2)

    for i in range(0, point_number):
        generate_random_start_algorythm(picture2)

    picture3 = UserImage(800, 600)

    line_number = randint(0, 30)
    point_number = randint(0, 30)

    if point_number > line_number:
        point_number = line_number

    for i in range(0, line_number):
        draw_random_lines(picture3)

    for i in range(0, point_number):
        generate_random_start_algorythm(picture3)

    picture4 = UserImage(800, 600)

    line_number = randint(0, 30)
    point_number = randint(0, 30)

    if point_number > line_number:
        point_number = line_number

    for i in range(0, line_number):
        draw_random_lines(picture4)

    for i in range(0, point_number):
        generate_random_start_algorythm(picture4)

    picture5 = UserImage(800, 600)

    line_number = randint(0, 30)
    point_number = randint(0, 30)

    if point_number > line_number:
        point_number = line_number

    for i in range(0, line_number):
        draw_random_lines(picture5)

    for i in range(0, point_number):
        generate_random_start_algorythm(picture5)

    picture6 = UserImage(800, 600)

    line_number = randint(0, 30)
    point_number = randint(0, 30)

    if point_number > line_number:
        point_number = line_number

    for i in range(0, line_number):
        draw_random_lines(picture6)

    for i in range(0, point_number):
        generate_random_start_algorythm(picture6)

    if picture3.last_algorythm_time == 0:
        return
    median = (picture3.total_coloured_pixels + picture3.total_pixels_visited)/picture3.last_algorythm_time



    if (picture.last_algorythm_time != 0):
        print(picture.total_coloured_pixels + picture.total_pixels_visited, " ", round(picture.last_algorythm_time, 10),
              "  ",
              round((picture.total_coloured_pixels + picture.total_pixels_visited) / picture.last_algorythm_time / median,
                    2))
    if (picture1.last_algorythm_time != 0):
        print(picture1.total_coloured_pixels + picture1.total_pixels_visited, " ", round(picture1.last_algorythm_time, 3),
              "  ", round(
                (picture1.total_coloured_pixels + picture1.total_pixels_visited) / picture1.last_algorythm_time / median,
                2))
    if (picture2.last_algorythm_time != 0):
        print(picture2.total_coloured_pixels + picture2.total_pixels_visited, " ", round(picture2.last_algorythm_time, 3),
              "  ", round(
                (picture2.total_coloured_pixels + picture2.total_pixels_visited) / picture2.last_algorythm_time / median,
                2))
    if (picture3.last_algorythm_time != 0):
        print(picture3.total_coloured_pixels + picture3.total_pixels_visited, " ", round(picture3.last_algorythm_time, 3),
              "  ", round(
                (picture3.total_coloured_pixels + picture3.total_pixels_visited) / picture3.last_algorythm_time / median,
                2))
    if (picture4.last_algorythm_time != 0):
        print(picture4.total_coloured_pixels + picture4.total_pixels_visited, " ", round(picture4.last_algorythm_time, 3),
              "  ", round(
                (picture4.total_coloured_pixels + picture4.total_pixels_visited) / picture4.last_algorythm_time / median,
                2))
    if (picture5.last_algorythm_time != 0):
        print(picture5.total_coloured_pixels + picture5.total_pixels_visited, " ", round(picture5.last_algorythm_time, 3),
              "  ", round(
                (picture5.total_coloured_pixels + picture5.total_pixels_visited) / picture5.last_algorythm_time / median,
                2))
    if (picture6.last_algorythm_time != 0):
        print(picture6.total_coloured_pixels + picture6.total_pixels_visited, " ", round(picture6.last_algorythm_time, 3),
              "  ", round(
                (picture6.total_coloured_pixels + picture6.total_pixels_visited) / picture6.last_algorythm_time / median,
                2))

    picture.display_image()
    picture1.display_image()
    picture2.display_image()
    picture3.display_image()
    picture4.display_image()
    picture5.display_image()
    picture6.display_image()


def array_results_tests():
    n_mediana = 0
    t_mediana = 0

    test_picture = UserImage(180,180)
    test_picture.start_algorythm(90,90)

    picture = UserImage(10, 10)
    if picture.start_algorythm(picture.image_width/2, picture.image_height/2) == 1:
        picture1 = UserImage(50, 50)

    if picture1.start_algorythm(picture1.image_width/2, picture1.image_height/2) == 1:
        picture2 = UserImage(100, 100)

    if picture2.start_algorythm(picture2.image_width/2, picture2.image_height/2) == 1:
        picture3 = UserImage(200, 200)

    if picture3.start_algorythm(picture3.image_width / 2, picture3.image_height / 2) == 1:
        picture4 = UserImage(400, 400)

    if picture4.start_algorythm(picture4.image_width / 2, picture4.image_height / 2) == 1:
        picture5 = UserImage(600, 600)

    if picture5.start_algorythm(picture5.image_width / 2, picture5.image_height / 2) == 1:
        picture6 = UserImage(800, 800)

    if picture6.start_algorythm(picture6.image_width / 2, picture6.image_height / 2) == 1:
        picture7 = UserImage(1000, 1000)

    if picture7.start_algorythm(picture7.image_width / 2, picture7.image_height / 2) == 1:
        picture8 = UserImage(1100, 1100)

    if picture8.start_algorythm(picture8.image_width / 2, picture8.image_height / 2) == 1:
        picture9 = UserImage(1200, 1200)

    if picture9.start_algorythm(picture9.image_width / 2, picture9.image_height / 2) == 1:
        picture10 = UserImage(1300, 1300)

    if picture10.start_algorythm(picture10.image_width / 2, picture10.image_height / 2) == 1:
        picture11 = UserImage(1400, 1400)

    if picture11.start_algorythm(picture11.image_width / 2, picture11.image_height / 2) == 1:
        picture12 = UserImage(1500, 1500)
        picture12.start_algorythm(picture12.image_width / 2, picture12.image_height / 2)

    median = (picture5.total_coloured_pixels + picture5.total_pixels_visited)/picture5.last_algorythm_time

    print("Liczba pixeli przetworzonych  Czas wykonania algorytmu   q(n) \n")
    print(picture.total_coloured_pixels + picture.total_pixels_visited, " ", round(picture.last_algorythm_time,10) , "  " , round((picture.total_coloured_pixels + picture.total_pixels_visited)/picture.last_algorythm_time/median,2) )
    print(picture1.total_coloured_pixels + picture1.total_pixels_visited, " ", round(picture1.last_algorythm_time,3), "  " , round((picture1.total_coloured_pixels + picture1.total_pixels_visited)/picture1.last_algorythm_time/median,2))
    print(picture2.total_coloured_pixels + picture2.total_pixels_visited, " ", round(picture2.last_algorythm_time,3), "  " , round((picture2.total_coloured_pixels + picture2.total_pixels_visited)/picture2.last_algorythm_time/median,2) )
    print(picture3.total_coloured_pixels + picture3.total_pixels_visited, " ", round(picture3.last_algorythm_time,3), "  " , round((picture3.total_coloured_pixels + picture3.total_pixels_visited)/picture3.last_algorythm_time/median,2) )
    print(picture4.total_coloured_pixels + picture4.total_pixels_visited, " ", round(picture4.last_algorythm_time,3), "  " , round((picture4.total_coloured_pixels + picture4.total_pixels_visited)/picture4.last_algorythm_time/median,2) )
    print(picture5.total_coloured_pixels + picture5.total_pixels_visited, " ", round(picture5.last_algorythm_time,3), "  " , round((picture5.total_coloured_pixels + picture5.total_pixels_visited)/picture5.last_algorythm_time/median,2) )
    print(picture6.total_coloured_pixels + picture6.total_pixels_visited, " ", round(picture6.last_algorythm_time,3), "  " , round((picture6.total_coloured_pixels + picture6.total_pixels_visited)/picture6.last_algorythm_time/median,2) )
    print(picture7.total_coloured_pixels + picture7.total_pixels_visited, " ", round(picture7.last_algorythm_time,3), "  " ,round((picture7.total_coloured_pixels + picture7.total_pixels_visited)/picture7.last_algorythm_time/median,2) )
    print(picture8.total_coloured_pixels + picture8.total_pixels_visited, " ", round(picture8.last_algorythm_time,3), "  ",  round((picture8.total_coloured_pixels + picture8.total_pixels_visited) / picture8.last_algorythm_time/median,2))
    print(picture9.total_coloured_pixels + picture9.total_pixels_visited, " ", round(picture9.last_algorythm_time,3), "  ",  round((picture9.total_coloured_pixels + picture9.total_pixels_visited) / picture9.last_algorythm_time/median,2))
    print(picture10.total_coloured_pixels + picture10.total_pixels_visited, " ", round(picture10.last_algorythm_time,3), "  ",  round((picture10.total_coloured_pixels + picture10.total_pixels_visited) / picture10.last_algorythm_time/median,2))
    print(picture11.total_coloured_pixels + picture11.total_pixels_visited, " ", round(picture11.last_algorythm_time,3), "  ",  round((picture11.total_coloured_pixels + picture11.total_pixels_visited) / picture11.last_algorythm_time/median,2))


def display_picture_algorythm_information(picture):
    print("Liczba pixeli odwiedzonych bez zamalowywania: ", picture.total_pixels_visited)
    print("Liczba pixeli zamalowanych: ", picture.total_coloured_pixels)
    print("Liczba pixeli przetworzonych (n)", picture.total_processed_pixels)
    print("Maxymalna możliwa liczba odwiedzonych i zamalowanych pixeli", 4 * picture.total_processed_pixels + 1)
    print("Rzeczywista liczba odwiedzonych i zamalowanych pixeli" , picture.total_coloured_pixels + picture.total_pixels_visited)
    print("Czas dzialania algorytmu: ", picture.total_algorythm_time)



def triangle_test():
    picture = UserImage(0, 0, "specific_tests/trojkat.bmp")
    picture.set_base_color(130)
    picture.display_image()
    picture.start_algorythm(350, 150)
    picture.display_image()
    picture.display_algorythm_information()

def square_test():
    picture = UserImage(0, 0, "specific_tests/kwadrat.png")
    picture.display_image()
    picture.set_base_color((255, 0, 0))
    picture.start_algorythm(150, 150)
    picture.display_image()
    picture.display_algorythm_information()

def rectangle_test():
    picture = UserImage(600, 400)
    for i in range(100,500):
        for j in range(100,200):
            picture.color_pixel(i,j)
    picture.display_image()
    picture.set_base_color((0, 255, 0))
    picture.start_algorythm(250, 150)
    picture.display_image()
    picture.display_algorythm_information()


def diamond_test():
    picture = UserImage(0, 0, "specific_tests/romb.bmp")
    picture.display_image()
    picture.set_base_color(130)
    picture.start_algorythm(150, 50)
    picture.display_image()
    picture.display_algorythm_information()


def custom_test():
    picture = UserImage(0, 0, "specific_tests/test.bmp")
    picture.display_image()
    picture.set_base_color(130)
    picture.start_algorythm(250, 150)
    picture.display_image()
    picture.display_algorythm_information()


def sharp_test():
    picture = UserImage(0, 0, "specific_tests/sharp.bmp")
    picture.display_image()
    picture.set_base_color(130)
    picture.start_algorythm(178, 173)
    picture.display_image()

    picture.display_algorythm_information()


def test_numberr():
    picture = UserImage(10, 10)
    for i in range(5, 7):
        for j in range(5, 7):
            picture.color_pixel(i, j)
    picture.display_image()
    picture.set_base_color((0, 255, 0))
    picture.start_algorythm(5, 5)
    picture.display_image()
    picture.display_algorythm_information()


def multi_test():
    picture = UserImage(0, 0, "specific_tests/figury-geometryczne.bmp")
    picture.display_image()
    picture.set_base_color(130)
    picture.start_algorythm(178, 173)
    picture.display_image()
    picture.set_base_color(180)
    picture.start_algorythm(278, 173)
    picture.display_image()
    picture.set_base_color(220)
    picture.start_algorythm(578, 173)
    picture.display_image()
    picture.set_base_color(200)
    picture.start_algorythm(178, 323)
    picture.display_image()
    picture.start_algorythm(278, 323)
    picture.display_image()
    picture.start_algorythm(528, 323)
    picture.display_image()
    picture.start_algorythm(178, 520)
    picture.display_image()
    picture.start_algorythm(298, 520)
    picture.display_image()
    picture.start_algorythm(528, 520)
    picture.display_image()
    picture.display_algorythm_information()

def draw_random_lines(picture):
        picture.draw_random_line()


def generate_random_start_algorythm(picture):
        picture.generate_random_algorythm_start()
