from pymouse import *
from pykeyboard import *
from tests import *




while True:
    str = input("Podaj numer testu, który chcesz wykonac :\n")
    if specific_test(int(str)) == 0:
        break


#Pytania :
# -Problem z podobnymi kolorami, czy przyjąć jakiś margines błędu czy tylko dokładnie ten kolor ma być zamalowywany.
#Jak dokładnie ma wyglądać drugi i trzeci z tryb z automatycznie generowanymi danymi. Czy parametryzowanie prostych figur czy coś więcej.



# specific_test(7)



# picture = UserImage(300,100)
# picture.display_image()
# picture.start_algorythm(50,50)
# picture.display_image()
# picture.display_algorythm_information()

def draw_image():
    pass
    # left_screen_width = 1360
    # picture = UserImage(300, 300)
    # while True:
    #     x,y = mouse.position()
    #     print(str(x) + "\n")
    #     print(str(y) + "\n")
    #
    #     picture.color_pixel(x - left_screen_width, y)
    #     picture.display_image()



