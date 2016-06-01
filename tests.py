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
    elif test_number == 8:
        pass
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


def parameterized_random_test(image_width = 600, image_height = 400, line_number = 20, point_number = 20):
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
    picture.display_image()

    for i in range(0, point_number):
        generate_random_start_algorythm(picture)
    picture.display_image()
    display_picture_algorythm_information()

def display_picture_algorythm_information(picture):
    print("Liczba pixeli odwiedzonych bez zamalowywania: ", picture.total_pixels_visited)
    print("Liczba pixeli zamalowanych: ", picture.total_coloured_pixels)
    print("Liczba pixeli przetworzonych (n)", picture.total_processed_pixels)
    print("Maxymalna możliwa liczba odwiedzonych i zamalowanych pixeli", 4 * picture.total_processed_pixels + 1)
    print("Rzeczywista liczba odwiedzonych i zamalowanych pixeli" , picture.total_coloured_pixels + picture.total_pixels_visited)
    print("Czas dzialania alforytmu: ", picture.total_algorythm_time)



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
