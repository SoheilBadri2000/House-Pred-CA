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

df = pd.read_csv("data/aug/data-aug-2024-04-22.csv")
urls = df[df["size_interior"].isna()]["page_url"]


def dim_to_sqft(area_list):
  area = 0.0
  full_dims = 0
  empty_dims = 0


  for dims in area_list:
    if dims and len(dims) <=2 :
      full_dims += 1
      sub_area = 1
      for dim in dims:
        sub_area *= abs(float(dim))
      area += sub_area
    else:
      empty_dims += 1

  if full_dims / (empty_dims+full_dims) > 0.3:
    area = area + (empty_dims * (area/full_dims))*0.5
    return area * 10.764
  else:
    return 1

# page.query_selector("span[class='ControlBaseWrapper*'] > h1")
  
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Accept": "*/*",
    "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.realtor.ca/",
    "Origin": "https://www.realtor.ca",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Connection": "keep-alive"
}

print(len(urls))

while len(urls) != 0:
    urls_150 = urls[:150]
    
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page(extra_http_headers=headers)

        for url in urls_150:
            try:
                print(url)
                page.goto(url)

                page.wait_for_load_state("networkidle")
                page.evaluate("() => window.scroll(0, document.body.scrollHeight)")
                page.wait_for_load_state("domcontentloaded")

                if not page.query_selector("span[class*='ControlBaseWrapper'] > h1"):
                  page.wait_for_selector("div[class*='listingDetailsRoomDetails_Dimensions']") # *= means "contains"

                  # page.screenshot(path=f"detail_pics.png", full_page=True)

                  html = page.inner_html("body")
                  tree = HTMLParser(html)

                  if page.query_selector("div[id='propertyDetailsMeasurementsSectionVal_4_1'] > div[class*='propertyDetailsSectionContentValue']"):
                    div = tree.css_first("div[id='propertyDetailsMeasurementsSectionVal_4_1'] > div[class*='propertyDetailsSectionContentValue']")
                    pattern = r"[-+]?(?:\d*\.*\d+)"
                    area = re.findall(pattern, div.text())[0]
                    print(area)
                    df.loc[df["page_url"] == url, "size_interior"] = float(area)
                  else:
                    divs = tree.css("div[class*='Metric']")
                    # areas = soup.find_all("div", attrs={"class": "listingDetailsRoomDetails_Dimensions Metric"})
                    [print(area.text()) for area in divs]
                    pattern = r"[-+]?(?:\d*\.*\d+)"
                    area_list = [(re.findall(pattern, area.text())) for area in divs]
                    print(area_list)
                    df.loc[df["page_url"] == url, "size_interior"] = dim_to_sqft(area_list)
                    # numbers = re.findall(r'\d+(\.\d+)?|\.\d+', area.text())
                    print()
                else:
                   print("not listed")

                   df.loc[df["page_url"] == url, "size_interior"] = 0

            except Exception as exception:
                print(exception)
                df.loc[df["page_url"] == url, "size_interior"] = 1

    print(f"scraped 150 records, {len(urls)} URLs remain")
    df.to_csv("data/aug/data-aug-2024-04-22.csv", index=False)
    urls = urls[150:]


# while list not empty:
#     launch playwright
#     for url in (list of 150):
#       do stuff on url
#   pop url[-1:-100]