import time
from seleniumwire.webdriver import Firefox
from seleniumwire.webdriver import FirefoxOptions
import gzip
import fileinput #i forgot how much i hate dealing with inputs 


#Read from stdin - including wsl 
idList=[_.replace("\n","") for _ in fileinput.input()]
print(idList)




#had to setup Driver(wire=True) before
driver = Firefox()


def stealJson(xs):
    #Predictable link
    link = r"https://www.barchart.com/futures/quotes/"+xs+"/price-history/historical"


    driver.get(link)
    #Testing issues
    time.sleep(2)

    #Get all requests whose responses were json
    #Take advantage of lazy evals to write short code
    jsonRequests = [x for x in driver.requests if x.response != None 
            and all([s not in x.url for s in ["firefox", "cookie"]])
            and "barchart" in x.url
            and x.response.headers.get("content-type")=='application/json'
            #I have no idea how to filter them better than this, but I always get
            #the same requests and it's probably this one 
            ]

    #should just be one left

    #assert len(jsonRequests)==1
    print(len(jsonRequests))

    #Doing this on windows, despite always using WSL
    with open(xs+".json","wb") as file:
        file.write(gzip.decompress(jsonRequests[0].response.body))


for i in idList:
    print("Stealing "+i, flush=True)
    try:
        stealJson(i)
    except IndexError:
        print("No data available", flush=True)

    #Clear previous requests
    del driver.requests

print("done")
