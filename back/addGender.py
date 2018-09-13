import multiprocessing as mp 
import os, time
import pandas as pd
import utils.scraper as sc
import utils.log as log 

artist_list = pd.read_csv("../500k_Songs/ArtistUrl.csv")

def addQueue(artist_list,  qu):
    for row in artist_list.iterrows():
        try:
            gend = getGender(row[1]['Artist'])
            if(gend==""):
                gend = "Any"
            row[1]['Gender'] = gend
            qu.put(row)
        except Exception as e:
            log.writeExceptions(e, ["Add Queue"])
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
        log.writeExceptions(e, ["Write Error"])

def main():
    # Add Gender Column
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
