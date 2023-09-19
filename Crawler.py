from bs4 import BeautifulSoup
import requests

class WebCrawler:
    def crawl_one_page(self, url):
        req = requests.get(url)
        names, prices = self.getNamePrice(req)
    
    def getNamePrice(self, req):
        soup = BeautifulSoup(req.text, "html.parser")
        names = soup.find_all("p", attrs={"class":"D_pt M_kA D_oq M_jR D_pu M_kB D_py M_kG D_p_ M_kI D_pE M_kM D_pH M_kP D_pK"})
        prices = soup.find_all("p", attrs={"class":"D_pt M_kA D_oq M_jR D_pu M_kB D_py M_kG D_p_ M_kI D_pE M_kM D_pG M_kO D_pJ"})
        names = [str(name) for name in names] # convert to string
        prices = [str(price) for price in prices] # convert to string
        # Name example
        # <p class="D_pt M_kA D_oq M_jR D_pu M_kB D_py M_kG D_p_ M_kI D_pE M_kM D_pH M_kP D_pK">LOVFEE 圓領坑條針織上衣 無袖 背心</p>
        names = [name[name.index(">")+1:name.index("</")] for name in names]
        prices = [price[price.index(">")+1:price.index("</")] for price in prices]
        return names, prices

if __name__=="__main__":
    url = "https://tw.carousell.com/categories/women-s-fashion-4/"
    crawler = WebCrawler()
    crawler.crawl_one_page(url)