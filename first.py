def sude_nebo_liche(cislo):
    if cislo % 2 == 0:
        print(f"cislo {cislo} je sude")
    else:
        print(f"cislo {cislo} je liche")


cislo = input("zadej cislo: ")
cislo = int(cislo)
print(f"zadane cislo je: {cislo}")
sude_nebo_liche(cislo)
sude_nebo_liche(5)
sude_nebo_liche(1_000_000)