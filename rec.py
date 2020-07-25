class Rectangle:
    x = 0
    y = 0

    def area(self, x, y):
        a = x * y
        print("area: " + str(a))

    def enveromint(self, x, y):
        env = 2*(x + y)
        print("enviroment: " + str(env))


r2 = Rectangle()
r2.x = 4
r2.y = 7
print(r2.area(r2.x, r2.y), r2.enveromint(r2.x, r2.y))
