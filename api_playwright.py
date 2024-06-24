from playwright.sync_api import sync_playwright
import time
import random

def fetch_realtor_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Run in headed mode
        context = browser.new_context()

        # Prepare the request parameters and headers
        url = 'https://api2.realtor.ca/Listing.svc/PropertySearch_Post'
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0',
            'Accept': '*/*',
            'Accept-Language': 'en-CA,en-US;q=0.7,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.realtor.ca',
            'DNT': '1',
            'Sec-GPC': '1',
            'Connection': 'keep-alive',
            'Referer': 'https://www.realtor.ca/',
            # 'Cookie': 'visid_incap_2269415=tLCmvVNdTq6o1DnzAMBYsaZueWYAAAAAQUIPAAAAAAAfMuTiVa5rzG6CGtV9TWAZ; incap_ses_676_2269415=d+GidQAFsm2IwO4VgKJhCaZueWYAAAAA6KlYeKcol2DdB+nemXI9Qg==; _gcl_au=1.1.657170755.1719234217; _ga_Y07J3B53QP=GS1.1.1719234217.1.1.1719234233.44.0.0; _ga=GA1.1.1823832629.1719234217; reese84=3:p3fpnF45bTMjIjdnTogWkg==:UxYGg3EIQpgi5IeeCLRLqwb9GaD9o2MTSffFklEAfFvRMovDV9QYmdnrN0yJvwPGJBMm1TLvdY0OaxGRXX86k9ElvW6EdppxVa7Oz70NsEPDlSkmd8e1L4d5KxNw2OqyTeUTgOcuxiHpAvkGujbODB63Xo4Du8PL7dS5FilvndHzxR+pY6wuXABtpq9tH7hZQP20TgvjiCV6Q66fG2y2QWGKQRR9aPVdkrhT8KQc9tJqeR8c8PnghxtZERS6Nf4Z7oAzbbWxLpjHAhgDfa2fz/nb8Kl5FK0azXeBkscsrPtjwkOXeKnGhiIMV0z8Y2RAw4kOSMALKVT2QMkvq9mZOjmQVQaFoDax2RqfGSCYB80awAbammWYdKWH9molnkhu1SaAmPxgL9lsXV36e9Nib40KfswRLgBKDZIHi4UXgJqPRxcTTrUuchu+ZCKRiczFGDAmAF5lzUZl71Ee7CKh4W8xQzbrV70cpFCU0tXwiro=:C0CD+1tCqBFJsTgllLgkakz7yl5z0y6264HuCZnTURw=; visid_incap_3057435=rsv8nz4+QaSLqF2rIDqt6apueWYAAAAAQUIPAAAAAADV4iyAbpRcOe5WW82bpT61; nlbi_3057435=YW/ZGEGQewt0kKhwoWGLxgAAAADri8vYomQl0djxjN/mjiGU; incap_ses_676_3057435=VyxkBXCQREpFwe4VgKJhCapueWYAAAAATsJlEjcKELPWbEybO8JmQw==; gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko=gigya-pr_ver4',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site'
        }
        data = {
            # 'CurrentPage': '2',
            'Sort': '6-D',
            'GeoIds': 'g30_dpz89rm7',
            'PropertyTypeGroupID': '1',
            'TransactionTypeId': '2',
            'PropertySearchTypeId': '1',
            'Currency': 'CAD',
            'IncludeHiddenListings': 'false',
            'RecordsPerPage': '12',
            'ApplicationId': '1',
            'CultureId': '1',
            'Version': '7.0'
        }

        # Perform the POST request with human-like delays
        response = context.request.post(url, headers=headers, data=data)
        
        # Simulate human-like delays
        time.sleep(random.uniform(1, 3))

        # Print the response
        print(response.json())

        # Close the browser
        browser.close()

# Execute the function to fetch data
fetch_realtor_data()
