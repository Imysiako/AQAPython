class Romb:
    def __init__(self, side, angle_1):

        self.side = side
        self.angle_1 = angle_1
        self.angle_2 = 180 - angle_1

    def __setattr__(self, key, value):
        if isinstance(value, str):
            raise TypeError ("The value should not be string")
        if value <= 0:
            raise TypeError("The value should be bigger than 0")
        if key == 'angle_1' and value >= 180:
            raise TypeError ("The value should not be 180 and bigger")
        super().__setattr__(key, value)
        if key == 'angle_1':
            super().__setattr__('angle_2', 180 - value)
        elif key == 'angle_2':
            super().__setattr__('angle_1', 180 - value)

    def __str__(self):
        return f'Side of romb is: {self.side}, first angle: {self.angle_1} and second angle is: {self.angle_2}'


my_rombs = Romb(side=14, angle_1=143)

print(my_rombs)
my_rombs.angle_1 = 39
print(my_rombs)
my_rombs.angle_2 = 39
print(my_rombs)