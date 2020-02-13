class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return Book(self.pages + other.pages)
    def __str__(self):
        return "Total no of pages in book are {}".format(self.pages)
    def __mul__(self,other):
        return Book(self.pages * other.pages)

b1=Book(100)
b2=Book(200)
b3=Book(300)
b4=Book(400)
b5=Book(500)
print(b1+b2+b3+b4+b5)
print('mul',b1*b2+b3*b4*b5)
