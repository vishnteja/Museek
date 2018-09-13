from bs4 import BeautifulSoup as bs 
from requests import get
import csv 

def getGender(artist):
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
    return final_table[1][3]

def main():
    c = 0
    # with open("songs.csv", 'w') as f:
    #     writer = csv.writer(f)
    #     with open('../songdata.csv') as r:
    #         reader = csv.reader(r)
    #         for row in reader:
    #             if(c>0):
    #                 row.insert(0,c)
    #                 c+=1
    #                 writer.writerow(row)
    #             else:
    #                 c+=1
    #     r.close()
    # f.close()

    # with open("songdata.csv", "w+") as f:
    #     writer = csv.writer(f)
    #     with open("songs.csv", 'r') as it:
    #         reader = csv.reader(it)
    #         for row in reader:
    #             artist = row[1]
    #             gend = getGender(artist)
    #             if(gend==""):
    #                 gend = "Any"
    #             row.append(gend)
    #             writer.writerow(row)
    #             c+=1
    #             if(c>100):
    #                 break
    #     it.close()
    # f.close()
    art = ["1"]
    c = 0
    with open("songs.csv", 'r') as it:
        reader = csv.reader(it)
        for row in reader:
            if(row[1]==art[c]):
                continue
            else:
                art.append(row[1])
                c+=1
    art.remove("1")
    print(len(art))
    
    # with open("songdata.csv", "w+") as f:
    #     writer = csv.writer(f)
    # for x in art:
    #     gend = getGender(x)
    #     if(gend==""):
    #         gend = "Any"
    #     artgend[x] = gend

    # with open('test.csv', 'w') as f:
    #     for key in artgend.keys():
    #         f.write("%s,%s\n"%(key,my_dict[key]))
        



    print(art)

if __name__ == "__main__" :
    main()