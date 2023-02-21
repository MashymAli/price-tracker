import requests
from bs4 import BeautifulSoup as bs

url = "https://www.amazon.com/OnePlus-Unlocked-Smartphone-Hasselblad-Wireless/dp/B08Y73NTXY/?_encoding=UTF8&pd_rd_w=TOcBu&content-id=amzn1.sym.595f69d1-9647-4ce9-9fca-a43eb1c1f3b6&pf_rd_p=595f69d1-9647-4ce9-9fca-a43eb1c1f3b6&pf_rd_r=MV5ZHQVBT52SR5ZPE0W7&pd_rd_wg=M34Tn&pd_rd_r=4c8ef00f-ac78-49b9-80a9-cce5a496c2ca&ref_=pd_gw_exports-popular-this-season-with-similar-asins"
#url2 = "https://www.amazon.com/dp/B0B3T9D5T8/ref=sspa_dk_detail_4?psc=1&pd_rd_i=B0B3T9D5T8&pd_rd_w=YX5h7&content-id=amzn1.sym.af9528d2-09ba-47ee-b909-59e3022bebe1&pf_rd_p=af9528d2-09ba-47ee-b909-59e3022bebe1&pf_rd_r=666PHG555J6EHK93FT7F&pd_rd_wg=EKACK&pd_rd_r=784c2fb9-06e4-41f6-a9d6-a2f3ea9e5126&s=wireless&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyMFU5S1hYQ0UySjlKJmVuY3J5cHRlZElkPUExMDEzMDUzMUxJTUw4MU9ENjBHUCZlbmNyeXB0ZWRBZElkPUEwNTUyODI3MVpLQjQzTDMySEtGWSZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
#url3 = "https://www.amazon.com/dp/B0B3BZZWSL/ref=va_live_carousel?pf_rd_r=0KP4323SNM03TSEDX7P1&pf_rd_p=ad3d6c63-0532-4175-87c3-43a01fbfb2e8&pf_rd_m=ATVPDKIKX0DER&pf_rd_t=Landing&pf_rd_i=165793011&pf_rd_s=merchandised-search-3&linkCode=ilv&tag=a0004911-20&ascsubtag=Best_LEGO_Sets_for_Adults_with_LEGO_Master_BrickinNick_230216190007&asc_contentid=amzn1.amazonlive.broadcast.e8ba3c8a-baca-4435-b09a-b93fa30d2569&pd_rd_i=B0B3BZZWSL&th=1"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}
page=requests.get(url,headers=headers)
soup = bs(page.content,"html.parser")

try:
    actual_price = soup.find('span', attrs={'class': 'a-price-whole'}).get_text()
    actual_price = float(actual_price.replace(",", ""))
except:
    actual_price = "Out of Stock"
print(actual_price)