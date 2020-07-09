import time
from urllib.request import urlopen
import json
from datetime import datetime

# https://api.kraken.com/0/public/Ticker?pair=ADAETH,ADAEUR,ADAUSD,ADAXBT,ALGOETH,ALGOEUR,ALGOUSD,ALGOXBT,ATOMETH,ATOMEUR,ATOMUSD

# They call it an 'ID' but you are right this is the UNIX TimeStamp.
#
# I agree that it is not clear from the API documentation.
#
# There is a limit in the number of results returned, see https://support.kraken.com/hc/en-us/articles/218198197-How-to-pull-all-trade-data-using-the-Kraken-REST-API
#
#     With an interval of 30 minutes you get all data from 15 days ago : https://api.kraken.com/0/public/OHLC?pair=EOSETH&since=0&interval=30
#
#     If you change the interval to 60 minutes you get data from 1 month ago : https://api.kraken.com/0/public/OHLC?pair=EOSETH&since=0&interval=60
#
#     With an interval of 1 minute you got data from less than 1 day (as stated in the article above) : https://api.kraken.com/0/public/OHLC?pair=EOSETH&since=0&interval=30
#
# I tried and indeed you cannot get all 30 min data from 27/10/2017.
#
# It seems the since parameter is useless once you reach the limit. It works great if not (i.e. data from yesterday https://api.kraken.com/0/public/OHLC?pair=EOSETH&since=1517774700&interval=30).
#
# As soon as you reach the limit the count starts from today to the past and you get only last 15 days data...
#
# Maybe a solution is, as stated in the article, to build your own OHLC from trades data...
#
# Try to contact the support to clarify this point (I already contacted them for another problem and they reply pretty fast).
#
# (I'm writing this as an answer because too much text the for a comment, sorry if it does not answer your question)


baseUrl = "https://api.kraken.com/0/public/"
assetsUrl = "Assets"

#listesymboles
mesMonnaies = ["XBT", "BCH", "XTZ", "XRP", "EUR"]
symbol = "XXBTZUSD"

def createUrlFromMesPairs():
    str = ""
    for pair in createPairsFromMesMonnaies():
        str+=pair
    print(str)
    return str


def createPairsFromMesMonnaies():
    listPairs = []
    for monnaie in mesMonnaies:
        for mon in mesMonnaies:
            if(monnaie!=mon):
                listPairs.append(monnaie+mon)
    return listPairs


def getListAssets():
    listAssets = []
    try:
        api_data = urlopen(baseUrl+assetsUrl).read()
        jsonResult = json.loads(api_data)
        for asset in jsonResult["result"]:
            listAssets.append(asset)
            # print(asset)
    except Exception:
        print("error in getListAssets")
    return listAssets


def aa():
    try:
        api_data = urlopen('https://api.kraken.com/0/public/Trades?pair=xbtusd&since=1559350785297011117').read()
        jsonResult = json.loads(api_data)
        return jsonResult
    except Exception:
        time.sleep(3)

def bb(x):
    print(x)
    for trade in x["result"][symbol]:
        dt_object = datetime.fromtimestamp(trade[2])
        print("__________")
        print("date : ", dt_object)
        print("price : " + trade[0])
        print("volume : " + trade[1])


def main():
    print("Hello World!")
    # print(bb(aa()))
    # print(getListAssets())
    # createPairsFromMesMonnaies()
    createUrlFromMesPairs()


if __name__ == "__main__":
    main()