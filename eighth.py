def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
    
    s = str(binarni_cislo)

    vysledek = 0

   
    for cislo in s:
        if cislo not in "01":
            raise ValueError("vstup musi byt binarni cislo")
        vysledek = vysledek * 2 + int(cislo)

    return vysledek



def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128