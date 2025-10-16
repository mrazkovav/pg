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
    return False

def vrat_prvocisla(maximum):
    """
    Funkce spocita vsechna prvocisla v rozsahu 1 az maximum a vrati je jako seznam.
    """
    return [2,3,5]

if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)