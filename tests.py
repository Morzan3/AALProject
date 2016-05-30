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


def triangle_test():
    picture = UserImage(0, 0, "specific_tests/trojkat.png")
    picture.set_base_color((0, 0, 0))
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
    picture = UserImage(0, 0, "specific_tests/romb.png")
    picture.display_image()
    picture.set_base_color((255, 0, 0))
    picture.start_algorythm(150, 50)
    picture.display_image()
    picture.display_algorythm_information()


def custom_test():
    picture = UserImage(0, 0, "specific_tests/test.jpg")
    picture.display_image()
    picture.set_base_color((255, 0, 0))
    picture.start_algorythm(250, 150)
    picture.display_image()
    picture.display_algorythm_information()


def sharp_test():
    picture = UserImage(0, 0, "specific_tests/sharp.jpg")
    picture.display_image()
    picture.set_base_color((255, 0, 0))
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
    picture = UserImage(0, 0, "specific_tests/figury-geometryczne.jpg")
    picture.display_image()
    picture.set_base_color((255, 0, 0))
    picture.start_algorythm(178, 173)
    picture.display_image()
    picture.display_algorythm_information()



