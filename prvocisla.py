def je_prvocislo(cislo):
    """
    Funkce overi, zda zadane cislo je nebo neni prvocislo a vrati True nebo False

    Prvocislo je takove cislo vetsi nez 1, ktere neni delitelne zadnym jinym cislem jenom 1 a samo sebou.

    Napoveda jak otestova prvocislo:
    Cislo 36 vznikne nasobenim:
    1 * 36
    2 * 18
    3 * 12
    4 * 9
    6 * 6
    9 * 4
    12 * 3
    18 * 2
    36 * 1
    Jak vidite v druhe polovine se dvojice opakuji, tzn. v tomto pripade staci overit delitelnost pouze do 6 (vcetne)
    """
    # předpokládáme, že se jedná o prvočíslo, která následně testujeme
    prvocislo = True
    # projdeme čísla od 2 až do poloviny testovaného čísla
    # a následně jimi číslo zkusíme vydělit
    # - začínáme 2 protože 1 je validní pro prvočíslo
    # - končíme v odmocnině testovaného čísla (odmocnina se dá udělat jako umocnění na 1/2), protože pak se začnou dvojice opakovat, viz rozklad nahoře
    # +1 je tam proto, že jinak bychom poslední číslo z rozsahu nevyzkoušeli (iterace by se zastavila ještě před ním)
    # přetypování na int() je potřeba, jelikož funkce range() ma jako parametr pouze cela čisla(int)
    for i in range(2, int(cislo ** (1/2)) + 1):
        # pokud není zbytek po dělení
        # znamená to, že je testované číslo dělitelné
        # a tudíš se nejedná o prvočíslo => změna na False
        # takto se testované číslo pokusíme vydělit všemi čísly v daném rozmezí
        # a stačí pouze jedno dělení beze zbytku a nejedná se o prvočíslo
        if not(cislo % i):
            prvocislo = False
    # vracíme výsledek testu True/False
    return prvocislo

def vrat_prvocisla(maximum):
    """
    Funkce spocita vsechna prvocisla v rozsahu 1 az maximum a vrati je jako seznam.
    """
    prvocisla = []
    # prochází se všechna čísla v rozmezí 1 až maximum
    # a testují se, zda se jedná o prvočísla
    for i in range(1, int(maximum)):
        # test zda se jedná o prvočíslo
        # pokud ano, přidá se do seznamu prvočísel
        if je_prvocislo(i):
            prvocisla.append(i)
    # vrátí se seznam se všemi prvočísly, které přošly testem
    return prvocisla

if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
