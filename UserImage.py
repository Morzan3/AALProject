from PIL import Image
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

    def start_algorythm(self, x_coordinate, y_cordinate):
        t0 = time.clock()
        if self.pixelMap[x_coordinate, y_cordinate] != self.base_color:
            area_color = self.pixelMap[x_coordinate, y_cordinate];
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
            try:

            #if x_value < self.image.size[0] - 1:
                if self.pixelMap[x_value + 1, y_value] == area_color:
                    self.pixelMap[x_value + 1, y_value] = self.base_color
                    coordinate_list.append((x_value + 1, y_value))
                    self.coloured_pixels += 1
                else:
                    print(self.pixelMap[x_value + 1, y_value])
                    self.visited_pixels += 1
                    if self.visited_pixels == 120000:
                        print("Teraz")

            #if x_value > 0:
                if self.pixelMap[x_value - 1, y_value] == area_color:
                    self.pixelMap[x_value - 1, y_value] = self.base_color
                    coordinate_list.append((x_value - 1, y_value))
                    self.coloured_pixels += 1
                else:
                    print(self.pixelMap[x_value - 1, y_value])
                    self.visited_pixels += 1
                    if self.visited_pixels == 120000:
                        print("Teraz")

            #if y_value < self.image.size[1] - 1:
                if self.pixelMap[x_value, y_value + 1] == area_color:
                    self.pixelMap[x_value, y_value + 1] = self.base_color
                    coordinate_list.append((x_value, y_value + 1))
                    self.coloured_pixels += 1
                else:
                    print(self.pixelMap[x_value, y_value + 1])
                    self.visited_pixels += 1
                    if self.visited_pixels == 120000:
                        print("Teraz")

            #if y_value > 0:
                if self.pixelMap[x_value, y_value - 1] == area_color:
                    self.pixelMap[x_value, y_value - 1] = self.base_color
                    coordinate_list.append((x_value, y_value - 1))
                    self.coloured_pixels += 1
                else:
                    print(self.pixelMap[x_value , y_value - 1])
                    self.visited_pixels += 1
                    if self.visited_pixels == 120000:
                        print("Teraz")

            except IndexError:
                continue


        self.last_algorythm_time = time.clock() - t0
        # self.test()

    def display_image(self):
        self.image.show()


    def display_algorythm_information(self):
        print("Liczba pixeli odwiedzonych bez zamalowywania: ", self.visited_pixels)
        print("Liczba pixeli zamalowanych: ", self.coloured_pixels)
        print("Liczba pixeli przetworzonych (n)", self.processed_pixels)
        print("Maxymalna możliwa liczba odwiedzonych i zamalowanych pixeli", 4*self.processed_pixels + 1)
        print("Czas dzialania alforytmu: ", self.last_algorythm_time)

    def set_base_color(self, new_base_color):
        self.base_color = new_base_color


    def test(self):
        for i in range (self.image_width):
            for j in range(self.image_height):
                print (self.pixelMap[i,j])


    def color_pixel(self,x_coordinate, y_coordinate):
        if x_coordinate < self.image_width and y_coordinate < self.image_height:
            self.pixelMap[x_coordinate,y_coordinate] = (0,0,255)

