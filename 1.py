# Příklad 1: Práce s podmínkami a cykly
# Zadání:
# Napište funkci `process_numbers`, která přijme seznam celých čísel. 
# Funkce vrátí nový seznam, který obsahuje pouze čísla větší než 5, vynásobená 2.
# Pokud při procházení seznamu narazíte na cokoli jiného než je číslo (tzn. int nebo float), ukončete zpracování seznamu a vraťte dosud vytvořený seznam.
#
# Vaše řešení můžete otestovat pomocí pytest takto:
# pytest zkouska1.py
# pokud Vám pytest nazahlásí žádné chyby, máte hotovo!
#
# instalace pytest:
# pip install pytest


def process_numbers(numbers):
    result = []
    for n in numbers:
        if type(n) not in (int, float):
            break
        if n > 5:
            result.append(n * 2)
    return result


# Unit testy
def test_process_numbers():
    assert process_numbers([1, 6, 3, '5', 8]) == [12]
    assert process_numbers([7, 8, None, 12]) == [14, 16]
    assert process_numbers([1, 2, 3, 4]) == []
    assert process_numbers([5, 6, 7, 15]) == [12, 14, 30]
    assert process_numbers([True, 4, 8, 10, 15]) == []


if __name__ == "__main__":
    test_process_numbers()