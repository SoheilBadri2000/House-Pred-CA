from playwright.sync_api import sync_playwright
from playwright_context import playwright_context

URL = "https://www.realtor.ca/map#view=list&CurrentPage=1&Sort=6-D&GeoIds=g30_dpxpsf37&GeoName=Milton%2C%20ON&PropertyTypeGroupID=1&TransactionTypeId=2&PropertySearchTypeId=1&Currency=CAD&HiddenListingIds=&IncludeHiddenListings=false"


day_num = 8
page_num = 1
lat_min = 42
lat_max = 83
lng_min = -141
lng_max = -53

def capture_all_requests(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # List to store captured requests
        captured_requests = []

        # Enable request interception
        def capture_request(route, request):
            request_info = {
                "url": request.url,
                "method": request.method,
                "headers": dict(request.headers),
                "post_data": request.post_data,
            }
            captured_requests.append(request_info)
            route.continue_()

        page.route("**", capture_request)

        # Navigate to the URL
        page.goto(url)

        # Wait for some time or specific conditions if needed
        page.wait_for_load_state("networkidle")
        page.evaluate("() => window.scroll(0, document.body.scrollHeight)")
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_selector("div[class='footerLabel']")

        # Optionally, you can log or analyze captured requests
        for idx, request_info in enumerate(captured_requests):
            if request_info["url"] == "https://api2.realtor.ca/Listing.svc/PropertySearch_Post":
                # print(f"Request {idx + 1}:")
                # print("URL:", request_info["url"])
                # print("Method:", request_info["method"])
                # print("Headers:", request_info["headers"])
                # print("Post data:", request_info["post_data"])
                # # Replace the request_info["post_data"] by our own payload
                # payload = f"LatitudeMax={lat_max+1}&LongitudeMax={lng_max+1}&LatitudeMin={lat_min}&LongitudeMin={lng_min}&CurrentPage={page_num}&Sort=6-D&PropertyTypeGroupID=1&TransactionTypeId=2&PropertySearchTypeId=0&NumberOfDays={day_num}&Currency=CAD&RecordsPerPage=200&ApplicationId=1&CultureId=1&Version=7.0"
                # context = browser.new_context()
                # response = context.request.post(request_info["url"], headers=request_info["headers"], data=payload)
                # print(response.json())
                playwright_context(browser=browser, request_info=request_info)
                print()
                break


        browser.close()

# Example usage:
capture_all_requests(URL)
