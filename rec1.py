class Regtangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        a = self.x * self.y
        print(a)

    def enviroment(self):
        env = 2 * (self.x + self.y)
        print(env)


r1 = Regtangle(4, 5)
print(r1.area(), r1.enviroment())
