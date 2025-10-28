def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    :return: True, pokud je tah možný, jinak False.
    """

    typ = figurka["typ"]
    start = figurka["pozice"]
    r1, c1 = start
    r2, c2 = cilova_pozice

    # Tah mimo šachovnici
    if not (1 <= r2 <= 8 and 1 <= c2 <= 8):
        return False

    # Pokud je cílová pozice obsazená jinou figurou
    if cilova_pozice in obsazene_pozice:
        return False

    dr, dc = r2 - r1, c2 - c1

    if typ == "pěšec":
        # Pěšec se může pohnout o jedno pole vpřed (směrem dolů)
        if dc == 0 and dr == 1 and (r2, c2) not in obsazene_pozice:
            return True
        # Z výchozí pozice může o dvě vpřed
        if r1 == 2 and dc == 0 and dr == 2 and (r1 + 1, c1) not in obsazene_pozice:
            return True
        return False

    elif typ == "jezdec":
        # Jezdec se pohybuje do tvaru písmene L
        return (abs(dr), abs(dc)) in [(2, 1), (1, 2)]

    elif typ == "věž":
        # Věž se pohybuje pouze po řádcích nebo sloupcích
        if r1 == r2 or c1 == c2:
            # Kontrola, zda v cestě nestojí jiná figura
            step_r = (dr > 0) - (dr < 0)
            step_c = (dc > 0) - (dc < 0)
            r, c = r1 + step_r, c1 + step_c
            while (r, c) != (r2, c2):
                if (r, c) in obsazene_pozice:
                    return False
                r += step_r
                c += step_c
            return True
        return False

    elif typ == "střelec":
        # Střelec se pohybuje diagonálně
        if abs(dr) == abs(dc):
            step_r = (dr > 0) - (dr < 0)
            step_c = (dc > 0) - (dc < 0)
            r, c = r1 + step_r, c1 + step_c
            while (r, c) != (r2, c2):
                if (r, c) in obsazene_pozice:
                    return False
                r += step_r
                c += step_c
            return True
        return False

    elif typ == "dáma":
        # Dáma kombinuje pohyb věže a střelce
        if abs(dr) == abs(dc) or r1 == r2 or c1 == c2:
            step_r = (dr > 0) - (dr < 0)
            step_c = (dc > 0) - (dc < 0)
            r, c = r1 + step_r, c1 + step_c
            while (r, c) != (r2, c2):
                if (r, c) in obsazene_pozice:
                    return False
                r += step_r
                c += step_c
            return True
        return False

    elif typ == "král":
        # Král se pohybuje o jedno pole jakýmkoli směrem
        return max(abs(dr), abs(dc)) == 1

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True