from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser

# page_num = 7
# URL = f"https://www.realtor.ca/map#ZoomLevel=10&Center=43.708087%2C-79.376385&LatitudeMax=44.02541&LongitudeMax=-78.54074&LatitudeMin=43.38908&LongitudeMin=-80.21203&view=list&CurrentPage={page_num}&PropertyTypeGroupID=1&Currency=CAD"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0"
}

if __name__ == "__main__":
        
    with sync_playwright() as p:

        for page_num in range(1,2):
            URL = f"https://www.realtor.ca/map#ZoomLevel=10&Center=43.708087%2C-79.376385&LatitudeMax=44.02541&LongitudeMax=-78.54074&LatitudeMin=43.38908&LongitudeMin=-80.21203&view=list&CurrentPage={page_num}&PropertyTypeGroupID=1&Currency=CAD"


            browser = p.chromium.launch(headless=False)
            page = browser.new_page(extra_http_headers=headers)
            page.goto(URL)

            page.wait_for_load_state("networkidle")
            page.evaluate("() => window.scroll(0, document.body.scrollHeight)")
            page.wait_for_load_state("domcontentloaded")
            page.wait_for_selector("div[class*='largeListingCardCon']") # *= means "contains"

            page.screenshot(path=f"realtor_pics/page{page_num}.png", full_page=True)

            html = page.inner_html("body")
            tree = HTMLParser(html)

            divs = tree.css("div[class='cardCon']")

            print(len(divs))
            for d in divs:
                price = d.css_first("div[class*='listingCardPrice']").text()
                address = d.css_first("div[class*='listingCardAddress']").text()

                if address[:4] == "#LOT":
                    type = "lot"
                    bedrooms, bathrooms = '0', '0'
                elif address[0] == "#":
                    type = "suite"
                    bedrooms, bathrooms = [room.text() for room in d.css("div[class*=listingCardIconNum]")]
                else:
                    type = "detatched"
                    bedrooms, bathrooms = [room.text() for room in d.css("div[class*=listingCardIconNum]")]

                agents = len(d.css("img[class*=listingCardRealtorImg]"))

                try:
                    brokerage = d.css_first("img[class*=listingCardOfficeImg]").attributes.get("alt")
                except:
                    brokerage = "none"


            #     tags = [a.text() for a in d.css("div[class*='StoreSaleWidgetTags'] > a")[:5]]
            #     release_date = d.css_first("div[class*='WidgetReleaseDateAndPlatformCtn'] > div[class*='StoreSaleWidgetRelease']").text()
            #     # release_date = d.css_first("div[class*='WidgetReleaseDateAndPlatformCtn']").text()
            #     review_count = d.css_first("div[class*='ReviewScoreCount']").text()
            #     review_score = d.css_first("div[class*='ReviewScoreValue'] > div").text()
            #     sale_price = d.css_first("div[class*='StoreSalePriceBox']").text()
            #     original_price = d.css_first("div[class*='StoreOriginalPrice']").text()

                attrs = {"price":price, "type":type, "address":address,
                         "bedrooms":bedrooms, "bathrooms":bathrooms, "agents":agents,
                         "brokerage":brokerage}

                print(attrs)