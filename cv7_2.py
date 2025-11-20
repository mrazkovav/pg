class Osoba:
    def __init__(self, name, age):
        self.jmeno = name
        self.vek = age

    def __str__(self):
        return f'osoba {self.jmeno} ma {self.vek} let'  
    

class Student(Osoba):
    def __init__(self, name, age, rocnik=1):
        super().__init__(name, age)
        self.rocnik = rocnik 
    

    def __str__(self):
        return f'Student {self.jmeno} ma {self.vek} let a studuje {self.rocnik} rocnik'
    

    
    def pridej_rok(self):
        super().pridej_rok()
        if self .rocnik < 5:
            self.rocnik += 1

class Ucitel(Osoba):
    def __init__(self, name, age, roky_praxe=0):
        super().__init__(name, age)
        self.roky_praxe = roky_praxe

    def __str__(self):
        return f'Ucitel {self.jmeno} ma {self.vek} let a {self.roky_praxe} let praxe'
    
    def pridej_rok(self):
        super().pridej_rok()
        self.roky_praxe += 1


class Udrzbar(Osoba):
    def __str__(self):
        return f'Udrybar {self.jmeno} ma {self.vek} let'

if __name__ == "__main__":
    Student1 = Student("Alice", 19, 2)
    Student2 = Student("Bob", 20)
    print(Student1)
    print(Student2)

    ucitel = Ucitel("Karel", 40)
    print(ucitel)

    osoby = [Student1, Student2, ucitel, Udrzbar]
   
   
    for i in range(10):
        for osoba in osoby:
            osoba.pridej_rok()