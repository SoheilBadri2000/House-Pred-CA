import requests
import json
import csv
from time import sleep
from random import randint


url = "https://api2.realtor.ca/Listing.svc/PropertySearch_Post"

# payload = "LatitudeMax=44.02541&LongitudeMax=-78.73025&LatitudeMin=43.38908&LongitudeMin=-80.02252&CurrentPage=2&Sort=6-D&PropertyTypeGroupID=1&TransactionTypeId=2&PropertySearchTypeId=0&Currency=CAD&RecordsPerPage=120&ApplicationId=1&CultureId=1&Version=7.0"
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

with open (r"data/inc/data-inc-2024-06-24.csv", 'w') as f:
    writer_obj = csv.writer(f)
    writer_obj.writerow(["id", "id_mls", "bathrooms_total", "bedrooms", "stories_total","size_interior", "building_type",
                        "agency_name", "agency_type", "property_type", "lng", "lat", "ownership_type", "ownership_type_group_ids", "land_size",
                        "parkings", "page_url", "timestamp", "postal_code", "province", "price"])
    
def write_to_csv(result):

    if ("Longitude" in result["Property"]["Address"]) and ("Latitude" in result["Property"]["Address"]):
        id = result["Id"]
        id_mls = result["MlsNumber"]
        bathrooms_total = result["Building"]["BathroomTotal"] if "BathroomTotal" in result["Building"] else 0
        bedrooms = result["Building"]["Bedrooms"] if "Bedrooms" in result["Building"] else 0
        stories_total = result["Building"]["StoriesTotal"]
        size_interior = result["Building"]["SizeInterior"]if "SizeInterior" in result["Building"] else ""
        building_type = result["Building"]["Type"] if "Type" in result["Building"] else "none"
        agency_name = result["Individual"][0]["Organization"]["Name"]
        agency_type = result["Individual"][0]["Organization"]["OrganizationType"]
        property_type = result["Property"]["Type"]
        lng = result["Property"]["Address"]["Longitude"]
        lat = result["Property"]["Address"]["Latitude"]
        ownership_type = result["Property"]["OwnershipType"] if "OwnershipType" in result["Property"] else "none"
        ownership_type_group_ids = " ".join(str(id) for id in result["Property"]["OwnershipTypeGroupIds"]) if "OwnershipTypeGroupIds" in result["Property"] else "none"
        parkings = result["Property"]["ParkingSpaceTotal"] if "ParkingSpaceTotal" in result["Property"] else 0
        land_size = result["Land"]["SizeTotal"] if "SizeTotal" in result["Land"] else ""
        page_url = f"https://realtor.ca{result["RelativeDetailsURL"]}"
        timestamp = result["InsertedDateUTC"]
        postal_code = result["PostalCode"]
        province = result["ProvinceName"]
        price = result["Property"]["PriceUnformattedValue"]
        
        with open (r"data/inc/data-inc-2024-06-24.csv", 'a') as f:
            writer_obj = csv.writer(f)
            writer_obj.writerow([id, id_mls, bathrooms_total, bedrooms, stories_total, size_interior, building_type,
                                agency_name, agency_type, property_type, lng, lat, ownership_type, ownership_type_group_ids, land_size,
                                parkings, page_url, timestamp, postal_code, province, price])


day_num = 8

lat_min = 42
lat_max = 83
lng_min = -141
lng_max = -53

safety_count = 0


for latitude in range(lat_min, lat_max):
    for longitude in range(lng_min, lng_max):
        for page_num in range(1,51):
                
            try:
                print(safety_count)
                safety_count += 1
                payload = f"LatitudeMax={latitude+1}&LongitudeMax={longitude+1}&LatitudeMin={latitude}&LongitudeMin={longitude}&CurrentPage={page_num}&Sort=6-D&PropertyTypeGroupID=1&TransactionTypeId=2&PropertySearchTypeId=0&NumberOfDays={day_num}&Currency=CAD&RecordsPerPage=200&ApplicationId=1&CultureId=1&Version=7.0"
                response = requests.request("POST", url, data=payload, headers=headers)
                res_json = response.json()

                req_total = res_json["Paging"]["TotalRecords"]

                if req_total >=10000:
                    with open ("list_overflow.txt", 'a') as f:
                        f.write(str(f"lat {latitude} lng {longitude}:\t{req_total-10000} entries missed"))
                        f.write("\n")

                if req_total != 0:
                    results = res_json["Results"]
                    res_num = 0

                    for result in results:
                        res_num += 1
                        write_to_csv(result)
                    # incase the upcoming pages do not contain any data, break the loop
                    if res_num == 0: 
                        break
                    
                    print(f"lat:{latitude} lng:{longitude} Scraped page {page_num} with {res_num} records")
                    safety_count += 1
                    if safety_count >= 100:
                        rand = randint(20, 60)
                        print(f"Safety sleep for {rand} secs...")
                        sleep(rand)
                        safety_count = 0

                else:
                    print(f"lat:{latitude} lng:{longitude} had no results")
                    break
            except Exception as exception:
                print("An exception occurred")
                print(exception)
                rand = randint(150, 300)
                print(f"Safety sleep for {rand} secs...")
                sleep(rand)
                safety_count += 1
                payload = f"LatitudeMax={latitude+1}&LongitudeMax={longitude+1}&LatitudeMin={latitude}&LongitudeMin={longitude}&CurrentPage={page_num}&Sort=6-D&PropertyTypeGroupID=1&TransactionTypeId=2&PropertySearchTypeId=0&NumberOfDays={day_num}&Currency=CAD&RecordsPerPage=200&ApplicationId=1&CultureId=1&Version=7.0"

                response = requests.request("POST", url, data=payload, headers=headers)
                res_json = response.json()
                

                req_total = res_json["Paging"]["TotalRecords"]

                if req_total != 0:
                    
                    results = res_json["Results"]
                    res_num = 0

                    for result in results:

                        res_num += 1

                        write_to_csv(result)
                        
                    # incase the upcoming pages do not contain any data, break the loop
                    if res_num == 0: 
                        break
                    
                    print(f"lat:{latitude} lng:{longitude} Scraped page {page_num} with {res_num} records")
                    safety_count += 1
                    if safety_count >= 100:
                        rand = randint(20, 60)
                        print(f"Safety sleep for {rand} secs...")
                        sleep(rand)
                        safety_count = 0

                else:
                    print(f"lat:{latitude} lng:{longitude} had no results")
                    break
            
        if safety_count == 50:
            rand = randint(10, 30)
            print(f"Safety sleep for {rand} secs...")
            sleep(rand)
            safety_count = 0
                    

            # with open("data.json", "w") as f:
            #     json.dump(res_json, f, indent=4)


