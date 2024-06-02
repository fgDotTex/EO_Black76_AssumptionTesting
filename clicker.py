import time
from seleniumbase.webdriver import Firefox
from seleniumbase.webdriver.common.by import By

br = Firefox()

link = r"https://www.barchart.com/futures/quotes/ESH98/price-history/historical"

signupButton = r"/html/body/div[8]/div/div/div[1]"

page = br.get(link)
rawCsv = r"https://www.barchart.com/proxies/core-api/v1/quotes/get?symbol=ES%5EF&fields=symbol%2CsymbolType%2CcontractName%2CcontractExpirationDate%2ClastPrice%2CpriceChange%2ChighPrice%2ClowPrice%2Cvolume%2CtradeTime%2CsymbolCode&orderBy=contractExpirationDate&orderDir=asc&limit=6&meta=field.shortName%2Cfield.description&raw=1"

time.sleep(1)
br.get(rawCsv)

#histPrices = br.find_element(By.XPATH, "/html/body/main/div/div[2]/div[1]/div/div[2]/div[2]/div/ul/li[4]/ul/li[7]/a")

