def cislo_text(cislo):
    # seznam (list) jednotek
    jednotky = [
        # index (pozice) - na položky v seznamu se podle nich dá odkazovat
        # 0.      1.       2.     3.      4.      5.     6.      7.      8.      9
        "nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"
    ]

    # seznam (list) desitek
    desitky = [
        # stejné jako u jednotek, první řetězec na indexu 0. je prázdný, tzn. že číslo nemá desítky
        # 0.   1.        2.        3.         4.         5.         6.          7.           8.          9
        "", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"
    ]

    # slovník (dict) pro 10 až 19 protože se prostě textově liší
    special = {
        # klíč:hodnota, v našem případě číslo které chci převést je klíč a jeho textová reprezentace je hodnota
        10: "deset", 11: "jedenáct", 12: "dvanáct", 13: "třináct", 14: "čtrnáct",
        15: "patnáct", 16: "šestnáct", 17: "sedmnáct", 18: "osmnáct", 19: "devatenáct"
    }

    # přetypování textového řetězce (str) na číslo (int)
    # s textovým řetězcem by nešlo počítat,
    # respektive by šlo, ale (+, -, ...) znamenají něco jiného přo text než pro čísla
    cislo = int(cislo)

    # kontrola záporného čísla
    if cislo < 0:
        return "Číslo je záporné"

    # číslo je 100, není co řešit
    if cislo == 100:
        return "sto"
    
    # číslo je menší než 10, není co řešit, stačí vrátit jednotky
    if 0 <= cislo < 10:
        return jednotky[cislo]

    # tady ta podminka kontroluje jestli je číslo ve slovníku pro 10 až 19
    if cislo in special:
        # pokud ano, můžeme ji hned vrátit
        # odkazuje na něj pomocí klíče v hranatých závorkách
        # číslo je například 15, pak si to lze představit jako special[15]
        # a slovník pak vrátí textovou hodnotu pro to číslo
        return special[cislo]

    # číslo nepřošlo jedinou předchozí podmínkou (==100, <10, není ve special) a je menší než 100
    # to znamená
    if cislo < 100:
        # dělení čísla bez zbytku deseti, dostanu číslovku na pozici desítek
        desitkova_cislovka = cislo // 10
        # zbytek po dělení deseti, dostanu pouze číslovku na pozici jednotek
        jednotkova_cislovka = cislo % 10

        # když je jednotková číslovka 0, znamená to, že máme desítky... 10, 20, 30, ...
        if jednotkova_cislovka == 0:
            return desitky[desitkova_cislovka]
        # v ostatních případech musíme vrátit oboje, desítky i jednotky
        else:
            return f"{desitky[desitkova_cislovka]} {jednotky[jednotkova_cislovka]}"

    # pokud číslo neprošlo ani jednou podmínkou, znamená to, že je větší než 100
    return "Číslo je větší než 100"

# zadání čísla, hodnota je textova (str)
cislo = input("Zadej číslo: ")
# zde nám funkce 'cislo_text' vratí textovou podobu odpovidajici našemu číslu
text = cislo_text(cislo)
# vypsání hodnoty
print(text)
