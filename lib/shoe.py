class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # private variable to store size
        self.size = size  # This will trigger the setter
        self.condition = "Used"  # Default condition

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")
            self._size = None

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
