from bs4 import BeautifulSoup as bs 
from requests import get





def main():
    
    artist = "Linkin Perk"
    artist = artist.replace(' ', '+')
    page = get("https://musicbrainz.org/search?query="+artist+"&type=artist&method=indexed")
    soup = bs(page.text, "html.parser")
    table = soup.find("tbody")
    table_rows = soup.find_all("tr")
    final_table=[]
    for tr in table_rows:
        td = tr.find_all("td")
        row = [i.text for i in td]
        final_table.append(row)
    print(final_table[1][3])


if __name__ == "__main__" :
    main()