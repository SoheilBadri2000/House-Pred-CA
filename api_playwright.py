from playwright.sync_api import sync_playwright

URL = "https://www.realtor.ca/map#view=list&CurrentPage=2&Sort=6-D&GeoIds=g30_dpxpsf37&GeoName=Milton%2C%20ON&PropertyTypeGroupID=1&TransactionTypeId=2&PropertySearchTypeId=1&Currency=CAD&HiddenListingIds=&IncludeHiddenListings=false"

def capture_first_request(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Enable request interception
        def capture_request(route, request):
            nonlocal first_request
            if not first_request:
            # if not first_post_request and request.method == "POST" and request.url.startswith(url):
                first_request = request
                route.continue_()
            if first_request:
                print("First request URL:", first_request.url)
                print("First request method:", first_request.method)
                print("First request headers:", first_request.headers)

        # page.route("**", capture_request)

        # Initialize first_request to None
        first_request = None

        # Navigate to the URL
        page.goto(url)

        # Wait for some time or specific conditions if needed
        page.wait_for_load_state("networkidle")
        page.evaluate("() => window.scroll(0, document.body.scrollHeight)")
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_selector("div[class='footerLabel']")

        page.route("**", capture_request)

        # # Optionally, you can log or analyze the first request
        # if first_request:
        #     print("First request URL:", first_request.url)
        #     print("First request method:", first_request.method)
        #     print("First request headers:", first_request.headers)

        browser.close()

# Example usage:
capture_first_request(URL)