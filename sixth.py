import sys
import requests
import re


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"odpoved skoncila chybovym statusem {response.status_code}")
 
    html = response.content.decode(errors="ignore")
    hrefs = re.findall(r'<a\s+[^>]*href=["\'](.*?)["\']', html, re.IGNORECASE)

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        hrefs =  download_url_and_get_all_hrefs(url)
        for href in hrefs:
            print(href)
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
