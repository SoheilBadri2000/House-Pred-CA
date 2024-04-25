from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
import re
import pandas as pd

# page_num = 7
# URL = f"https://www.realtor.ca/map#ZoomLevel=10&Center=43.708087%2C-79.376385&LatitudeMax=44.02541&LongitudeMax=-78.54074&LatitudeMin=43.38908&LongitudeMin=-80.21203&view=list&CurrentPage={page_num}&PropertyTypeGroupID=1&Currency=CAD"

# urls = [
#     'https://realtor.ca/real-estate/26399369/591-wellington-avenue-windsor',
#     'https://realtor.ca/real-estate/26398326/955-ouellette-avenue-unit-102-windsor'
# ]

df = pd.read_csv("data_complete.csv")
urls = df["page_url"]


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0"
}

if __name__ == "__main__":
        
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page(extra_http_headers=headers)

        for URL in urls:
            try:
                print(URL)
                page.goto(URL)

                page.wait_for_load_state("networkidle")
                page.evaluate("() => window.scroll(0, document.body.scrollHeight)")
                page.wait_for_load_state("domcontentloaded")
                page.wait_for_selector("div[class*='listingDetailsRoomDetails_Dimensions']") # *= means "contains"

                # page.screenshot(path=f"detail_pics.png", full_page=True)

                html = page.inner_html("body")
                tree = HTMLParser(html)

                divs = tree.css("div[class*='Metric']")
                # areas = soup.find_all("div", attrs={"class": "listingDetailsRoomDetails_Dimensions Metric"})
                [print(area.text()) for area in divs]
                pattern = r"[-+]?(?:\d*\.*\d+)"
                area_list = [(re.findall(pattern, area.text())) for area in divs]
                print(area_list)
                with open ("data_area.txt", 'a') as f:
                    f.write(str(area_list))
                    f.write("\n")
                # numbers = re.findall(r'\d+(\.\d+)?|\.\d+', area.text())
                print()
            except Exception as exception:
                print(exception)
                with open ("data_area.txt", 'a') as f:
                    f.write("[0]")
                    f.write("\n")


            