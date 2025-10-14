
def cislo_text(cislo):
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desitky = ["", "deset", "dvacet", "třicet", "čtyřicet", "padesát",
               "šedesát", "sedmdesát", "osmdesát", "devadesát"]

 
    cislo = int(cislo)

   
    if cislo < 10:
        return jednotky[cislo]

   
    if 10 <= cislo < 20:
        special = {
            10: "deset", 11: "jedenáct", 12: "dvanáct", 13: "třináct",
            14: "čtrnáct", 15: "patnáct", 16: "šestnáct", 17: "sedmnáct",
            18: "osmnáct", 19: "devatenáct"
        }
        return special[cislo]


    if 20 <= cislo < 100:
        d = cislo // 10
        j = cislo % 10
        if j == 0:
            return desitky[d]
        else:
            return f"{desitky[d]} {jednotky[j]}"

  
    if cislo == 100:
        return "sto"

    return "Číslo mimo rozsah (0–100)"


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
