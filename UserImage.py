from PIL import Image
import time

class UserImage:
    def __init__(self, image_width, image_height):
        self.image_width = image_width
        self.image_height = image_height
        self.default_color = (0,0,0)
        self.base_color = (255,255,255)
        self.image = Image.new('RGB', (self.image_width, self.image_height), self.default_color)  # create a new black image
        self.pixelMap = self.image.load()
        self.visited_pixels = 0
        self.coloured_pixels = 0
        self.last_algorythm_time = 0;

    def start_algorythm(self, x_coordinate, y_cordinate):
        t0 = time.clock()
        if self.pixelMap[x_coordinate, y_cordinate] != self.base_color:
            area_color = self.pixelMap[x_coordinate, y_cordinate];
            self.pixelMap[x_coordinate, y_cordinate] = self.base_color
            self.coloured_pixels = 1
            self.visited_pixels = 1
        else:
            return None

        coordinate_list = [(x_coordinate, y_cordinate)]


        while True:

            try:
                coordinates = coordinate_list.pop()

            except IndexError:
                break

            (x_value, y_value) = coordinates

            if x_value < self.image.size[0] - 1:
                if self.pixelMap[x_value + 1, y_value] == area_color:
                    self.pixelMap[x_value + 1, y_value] = self.base_color
                    coordinate_list.append((x_value + 1, y_value))
                    self.coloured_pixels += 1
                else:
                    self.visited_pixels += 1

            if x_value > 0:
                if self.pixelMap[x_value - 1, y_value] == area_color:
                    self.pixelMap[x_value - 1, y_value] = self.base_color
                    coordinate_list.append((x_value - 1, y_value))
                    self.coloured_pixels += 1
                else:
                    self.visited_pixels += 1

            if y_value < self.image.size[1] - 1:
                if self.pixelMap[x_value, y_value + 1] == area_color:
                    self.pixelMap[x_value, y_value + 1] = self.base_color
                    coordinate_list.append((x_value, y_value + 1))
                    self.coloured_pixels += 1
                else:
                    self.visited_pixels += 1

            if y_value > 0:
                if self.pixelMap[x_value, y_value - 1] == area_color:
                    self.pixelMap[x_value, y_value - 1] = self.base_color
                    coordinate_list.append((x_value, y_value - 1))
                    self.coloured_pixels += 1
                else:
                    self.visited_pixels += 1

        self.last_algorythm_time = time.clock() - t0

    def display_image(self):
        self.image.show()

    def display_algorythm_information(self):
        print("Liczba pixeli odwiedzonych bez zamalowywania: ", self.visited_pixels)
        print("Liczba pixeli zamalowanych: ", self.coloured_pixels)
        print("Maxymalna możliwa liczba odwiedzonych pixeli", 4*self.coloured_pixels)
        print("Czas dzialania alforytmu: ", self.last_algorythm_time)
