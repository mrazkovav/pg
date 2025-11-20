class ChybnaSuma(Exception):
    pass



class BankovniUcet:
    def __init__(self, jemno):
        self.jmeno = jemno
        self.zustatek = 0


    def __str__(self):
        return f"Ucet {self.jmeno} ma zustatek {self.zustatek} Kc"

    def vloz(self, suma):
        if suma <= 0:
            raise ChybnaSuma("Suma musi byt kladna")
        self.zustatek += suma

    def vyber(self, suma):
        if suma <= 0:
            raise ChybnaSuma("Suma musi byt kladna")
        if suma > self.zustatek:
            raise ChybnaSuma("Nedostatecny zustatek na uctu")
        self.zustatek -= suma

    


if __name__ == "__main__":
    try:
        ucet = BankovniUcet("Alice")
        print(ucet)
        ucet.vloz(100)
        print(ucet)
        ucet.vyber(1000)
        print(ucet)
    except ChybnaSuma as e:
        print(e)