from requests_html import HTMLSession
# from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup

url = "https://www.realtor.ca/real-estate/26413271/912-1787-st-clair-ave-w-toronto-weston-pellam-park"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Accept": "*/*",
    "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.realtor.ca",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.realtor.ca/",
    "Cookie": "visid_incap_2269415=pJhvPn6ASnSR2yvC8gP58n+eoGUAAAAAQUIPAAAAAADgjQjWnfHRjGUrhSLlXlgo; incap_ses_305_2269415=Zw38Tc2zJVXTTruglZQ7BH+eoGUAAAAAa6wJ1JirRMS6hDdIs2ebTQ==; _gcl_au=1.1.1745302456.1705025154; _ga_Y07J3B53QP=GS1.1.1705025154.1.1.1705025228.56.0.0; _ga=GA1.1.679786856.1705025155; reese84=3:NmVaptrRYGHK+sPDt9By+Q==:fh88zdht0ZAdSFH+IZViX3My/SaTigGFuS7FrfCuKKqPMy4NTn+r6SCgStn1HAAqQqDImSwjtUq6sS7pertWpYYFxqXZgD4G72aYSp2U2Ct+c7KJ4zPD1xovBtDMFE/yskgr81sLEkl8bTUG01jKdmGzkI0uNad/aOZT2HWVHB0dDpNBz+EGifuKhL9cS8R/HbueSEsxB5nmFmHlETfJ0fbuANWNN4EDvrws5h8LYILH6t1EAH+z8q+Hhevo/xqbjwhyk4+WxjtsYd4KTW5FTXSRf0XQbEZi0rpjk0H1nYWqA5LYvYasgPszSr/tG+4bpMbW+CjIh4+TV2VuvSkAAZJKHZAx/FKLXbdCMqb2LF/b/0oSvdgilBYom6DechV7p/b3RQurSkGsi0ddr3OYSI/qrz3fsAoDzk7h58ElIGF15/AnpfGKk8mcObfi14XzwsoCYSjQpCJWqVycwvts6g==:KTxwuZocs5N8zKag0pVg/IijEzNmD6OHDhHWyEHZZG8=; gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko=gigya-pr_ver4; visid_incap_2271082=kSXLyU8MR92Lzw55P4prVcieoGUAAAAAQUIPAAAAAADMalAjk7DIkkKOEEdTT/Hc; nlbi_2271082=v8kGHhMebxjsLku8VPrQ3QAAAADvKG9+2aD2dzsdXRbqe/Ew; incap_ses_305_2271082=H4I5T5YEUCy/m7uglZQ7BMieoGUAAAAAwpBPCkxPM3JqF9dDTdjZpA==",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers"
}

session = HTMLSession()
resp = session.get(url)
# resp.html.render(sleep=1, scrolldown=1)
print(resp.status_code)
# print(resp.text)

soup = BeautifulSoup(resp.text, 'html.parser')
areas = soup.find_all("div", attrs={"class": "listingDetailsRoomDetails_Dimensions metric"})
[print(area.text) for area in areas]