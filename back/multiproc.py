from bs4 import BeautifulSoup as bs 
from requests import get
import multiprocessing as mp 
import os, time
import pandas as pd

exceptions = []
artist_list = pd.read_csv("../500k_Songs/ArtistUrl.csv")

def writeExceptions(artist):
    try:
        with open("except1.csv", "a+") as f:
            f.write("%s\n"%(artist))
        f.close()
    except Exception as e:
        print(str(e)+" Function Write Exception")

def getGender(artist):
    artist = artist.replace(' ', '+')
    try:
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
    except Exception as e:
        writeExceptions(artist)
        print(str(e)+" Function Write GetGender")

def addQueue(artist_list,  qu):
    for row in artist_list.iterrows():
        try:
            gend = getGender(row[1]['Artist'])
            if(gend==""):
                gend = "Any"
            row[1]['Gender'] = gend
            qu.put(row)
        except Exception as e:
            print(str(e)+" Function Add Queue")
    qu.put("Done")   

def writeFile(qu, nproc):
    c = 0
    count = 0
    try:
        with open("full1.csv", "w+") as f:
            while True:
                row = qu.get()
                if(row=="Done"):
                    c+=1
                    if(c==nproc):
                        break
                else:
                    f.write("%s,%s,%s\n"%(row[1]['Artist'], row[1]['Urls'], row[1]['Gender'])) 
                    count+=1
                    if(count%1000==0):
                        print(count+" Done")
                        sleep(1000)
                    
        f.close()
    except Exception as e:
        print(str(e)+" Function Write File")

def main():
    artist_list["Gender"] = ""
    l, _ = artist_list.shape
    # Multiprocessing
    qu = mp.Queue()
    nproc = 3
    
    start_time = time.time()
    writeProcess = mp.Process(target=writeFile, args=(qu, nproc))
    writeProcess.daemon = True
    writeProcess.start()

    p1 = mp.Process(target=addQueue, args=(artist_list[0:int(l/3)], qu))
    p2 = mp.Process(target=addQueue, args=(artist_list[int(l/3):int(2*l/3)], qu))
    p3 = mp.Process(target=addQueue, args=(artist_list[int(2*l/3):l], qu))
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
    writeProcess.join()
    print("Multiprocess Executed in {0} seconds".format(time.time()-start_time))


if __name__ == '__main__':
    main()
