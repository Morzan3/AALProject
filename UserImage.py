#Ignacy Ślusarczyk
#Nr indeksu: 261521
#islusarc@mion.elka.pw.edu.pl
#Algorytm kolorowania obszarów spójnych
from PIL import Image, ImageDraw
from random import randint
import time

class UserImage:
    def __init__(self, image_width = 0, image_height = 0, file_path =""):
        if file_path == "":
            self.image_width = image_width
            self.image_height = image_height
            self.default_color = (0,0,0)
            self.base_color = (255,255,255)
            self.image = Image.new('RGB', (self.image_width, self.image_height), self.default_color)  # create a new black image
            self.pixelMap = self.image.load()
            self.visited_pixels = 0
            self.coloured_pixels = 0
            self.processed_pixels = 0
            self.last_algorythm_time = 0
            self.total_coloured_pixels = 0
            self.total_pixels_visited = 0
            self.total_processed_pixels = 0
            self.total_algorythm_time = 0


        else:
            self.image = Image.open(file_path)
            self.image_width = self.image.size[0]
            self.image_height = self.image.size[1]
            self.default_color = (0,0,0)
            self.base_color = (255,255,255)
            self.pixelMap = self.image.load()
            self.visited_pixels = 0
            self.coloured_pixels = 0
            self.processed_pixels = 0
            self.last_algorythm_time = 0
            self.total_coloured_pixels = 0
            self.total_pixels_visited = 0
            self.total_processed_pixels = 0
            self.total_algorythm_time = 0

    def start_algorythm(self, x_coordinate, y_cordinate):

        if self.pixelMap[x_coordinate, y_cordinate] != self.base_color:
            area_color = self.pixelMap[x_coordinate, y_cordinate]
            self.pixelMap[x_coordinate, y_cordinate] = self.base_color
            self.coloured_pixels = 1
            self.visited_pixels = 0
            self.processed_pixels = 0
        else:
            return None

        coordinate_list = [(x_coordinate, y_cordinate)]


        while True:

            try:
                coordinates = coordinate_list.pop()
                self.processed_pixels += 1
            except IndexError:
                break

            (x_value, y_value) = coordinates

            t0 = time.clock()
            if x_value < self.image_width - 1:
                if self.pixelMap[x_value + 1, y_value] == area_color:
                    self.pixelMap[x_value + 1, y_value] = self.base_color
                    coordinate_list.append((x_value + 1, y_value))
                    self.coloured_pixels += 1
                else:
                    self.visited_pixels += 1
            else:
                self.visited_pixels += 1


            if x_value > 0:
                if self.pixelMap[x_value - 1, y_value] == area_color:
                    self.pixelMap[x_value - 1, y_value] = self.base_color
                    coordinate_list.append((x_value - 1, y_value))
                    self.coloured_pixels += 1
                else:
                    self.visited_pixels += 1
            else:
                self.visited_pixels += 1


            if y_value < self.image_height - 1:
                if self.pixelMap[x_value, y_value + 1] == area_color:
                    self.pixelMap[x_value, y_value + 1] = self.base_color
                    coordinate_list.append((x_value, y_value + 1))
                    self.coloured_pixels += 1
                else:
                    self.visited_pixels += 1
            else:
                self.visited_pixels += 1

            if y_value > 0:
                if self.pixelMap[x_value, y_value - 1] == area_color:
                    self.pixelMap[x_value, y_value - 1] = self.base_color
                    coordinate_list.append((x_value, y_value - 1))
                    self.coloured_pixels += 1
                else:
                    self.visited_pixels += 1
            else:
                self.visited_pixels += 1

            self.last_algorythm_time += time.clock() - t0


        self.total_algorythm_time += self.last_algorythm_time
        self.total_coloured_pixels += self.coloured_pixels
        self.total_pixels_visited += self.visited_pixels
        self.total_processed_pixels += self.processed_pixels
        self.total_pixels_visited -= 1
        return 1

    def display_image(self):
        self.image.show()


    def display_algorythm_information(self):
        print("Liczba pixeli odwiedzonych bez zamalowywania: ", self.visited_pixels)
        print("Liczba pixeli zamalowanych: ", self.coloured_pixels)
        print("Liczba pixeli przetworzonych (n)", self.processed_pixels)
        print("Maxymalna możliwa liczba odwiedzonych i zamalowanych pixeli", 4*self.processed_pixels + 1)
        print("Czas dzialania algorytmu: ", self.last_algorythm_time)

    def set_base_color(self, new_base_color):
        self.base_color = new_base_color


    def color_pixel(self,x_coordinate, y_coordinate):
        if x_coordinate < self.image_width and y_coordinate < self.image_height:
            self.pixelMap[x_coordinate,y_coordinate] = (0,0,255)


    def draw_random_line(self):
        draw = ImageDraw.Draw(self.image)
        if randint(0,1) == 0:
            if randint(0, 1) == 0:
                start_x = 0
                start_y = randint(0, self.image_height - 1)
            else:
                start_x = self.image_width -1
                start_y = randint(0, self.image_height - 1)
        else:
            if randint(0, 1) == 0:
                start_y = 0
                start_x = randint(0, self.image_width - 1)
            else:
                start_y = self.image_height-1
                start_x = randint(0, self.image_width - 1)

        if randint(0, 1) == 0:
            if randint(0, 1) == 0:
                end_x = 0
                end_y = randint(0, self.image_height - 1)
            else:
                end_x = self.image_width - 1
                end_y = randint(0, self.image_height - 1)
        else:
            if randint(0, 1) == 0:
                end_y = 0
                end_x = randint(0, self.image_width - 1)
            else:
                end_y = self.image_height-1
                end_x = randint(0, self.image_width - 1)

        if start_x == end_x and start_x == 0:
            start_x = self.image_width-1
        elif start_x == end_x and start_x == self.image_width - 1:
            start_x = 0

        if start_y == end_y and start_y == 0:
            start_y = self.image_height-1
        elif start_y == end_y and start_y == self.image_height - 1:
            start_y = 0

        draw.line(((start_x,start_y),(end_x,end_y)), fill=128)

    def generate_random_algorythm_start(self):
        x = randint(0, self.image_width - 1)
        y = randint(0, self.image_height - 1)

        if self.pixelMap[x,y] == (128,0,0) or self.pixelMap[x,y] == (255,255,255):
            self.generate_random_algorythm_start()
        else:
            self.start_algorythm(x,y)

