class Animal:
    __name = ""
    __size = ""
    __color = ""

    #Metodos Getters
    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def get_color(self):
        return self.__color

    #Metodos Setters
    def set_name(self, name):
        self.__name = name

    def set_size(self, size):
        self.__size = size

    def set_color(self, color):
        self.__color = color


