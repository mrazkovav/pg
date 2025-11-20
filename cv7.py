class vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'vektor({self.x}, {self.y})'
    

    def secti(self, jiny_vektor):
        x = self.x + jiny_vektor.x
        y = self.y + jiny_vektor.y
        return vektor(x, y)
    
    def vynasob(self, skalar):
        x = self.x * skalar
        y = self.y * skalar 
        return vektor(x, y)


if __name__ == "__main__":
    v1 = vektor(5, 6)
    v2 = vektor(10, 15)

    v3 = v1.secti(v2)
    print(v3)


    v4 = v1.vynasob(4)
    print(v4)