from playwright.sync_api import sync_playwright

URL = "https://www.realtor.ca/map#view=list&CurrentPage=2&Sort=6-D&GeoIds=g30_dpxpsf37&GeoName=Milton%2C%20ON&PropertyTypeGroupID=1&TransactionTypeId=2&PropertySearchTypeId=1&Currency=CAD&HiddenListingIds=&IncludeHiddenListings=false"

def capture_requests_responses(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # List to store captured requests and responses
        captured_requests_responses = []

        # Enable request interception
        def capture_request(route, request):
            # Intercept request details
            request_info = {
                "url": request.url,
                "method": request.method,
                "request_headers": dict(request.headers),
                "post_data": request.post_data,
            }

            # Continue the request
            route.continue_()

            # Function to capture response details
            def capture_response(response):
                response_info = {
                    "response_status": response.status,
                    "response_headers": dict(response.headers),
                    "response_body": response.body(),
                }
                # Combine request and response details
                request_response_info = {**request_info, **response_info}
                captured_requests_responses.append(request_response_info)

            # Intercept response
            route.continue_().then(capture_response)

        page.route("**", capture_request)

        # Navigate to the URL
        page.goto(url)

        # Wait for some time or specific conditions if needed
        page.wait_for_load_state("load")

        # Optionally, you can log or analyze captured requests and responses
        for idx, request_response in enumerate(captured_requests_responses):
            print(f"Request {idx + 1}:")
            print("URL:", request_response["url"])
            print("Method:", request_response["method"])
            print("Request Headers:", request_response["request_headers"])
            print("Post Data:", request_response["post_data"])
            print("Response Status:", request_response["response_status"])
            print("Response Headers:", request_response["response_headers"])
            print("Response Body:", request_response["response_body"][:200])  # Limiting to 200 characters for brevity
            print()

        browser.close()

# Example usage:
capture_requests_responses(URL)
