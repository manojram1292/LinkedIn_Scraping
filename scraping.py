# Tested on: 26-01-2024
# Author: Tufayel Ahmed
# Github: https://www.github.com/TufayelLUS
# LinkedIn: https://www.linkedin.com/in/tufayel-ahmed-cse/
# Follow me on GitHub for more premium projects!
# This script collects all *COMPANY WISE* profiles listed in LinkedIn
# This version doesn't collect e-mail addresses as of now
import requests
import re
import csv
import os
from time import sleep


s = requests.Session()
company_link = "https://www.linkedin.com/company/apple/"  # target company link
output_file_name = "leads.csv"  # output CSV excel file name
pagination_delay = 5  # delay in seconds before going to the next page
cookies = 'li_sugr=514d0640-1bf8-4eb8-b595-b9546be09556; bcookie="v=2&f46b9d61-9617-4374-827c-5ba06334471f"; bscookie="v=1&2024020401173324a28bbd-c634-4814-89f3-c4fc15019f7aAQGOEBs4t6CB2vLY4QboBRtOCBQOyNim"; li_rm=AQE3ssDEnjru0wAAAY8Q_H5nwEBtFd0fI5Ar4LKSNYxEymb51EheptHU5TpDyG39MWPx2e50dFoURLLitbFkh66i_SOyBel3BaSMAzRixSP1QbaMwKddcSs9; aam_uuid=22095582005058124140499558563586490625; _gcl_au=1.1.244595973.1713976963; li_at=AQEDASteJX4E23kWAAABjxD87NsAAAGPNQlw21YAH8ow20T8owEePp3CprMFHEgBp5hglEG-ImhNpO_yv_F3io7nporr3Ic172Egyd0fiPF01Obc1STyWF0Kc9CLCJAyewLWZMAU6q74O47M-Z_5jE4u; liap=true; JSESSIONID="ajax:8569736536422275995"; timezone=America/Halifax; li_theme=light; li_theme_set=app; _guid=bb5170c7-cb94-4165-abb5-a76488d2115d; AnalyticsSyncHistory=AQL4ATB9px-Z9wAAAY8Q_P7-J8LL2Zu2bEFLqng474FlQhdvQM_fuzY6LUPWfyZpC3wo0Js28DWoDwmwYut6wA; lms_ads=AQHS885GJwovOgAAAY8Q_P_gSRgUGqsr38-x_srO-ioCnTkXKjZ7T91zfXnBKTN4nuhc4wan8Ba3KFZqcF7TzDs9DESscaNw; lms_analytics=AQHS885GJwovOgAAAY8Q_P_gSRgUGqsr38-x_srO-ioCnTkXKjZ7T91zfXnBKTN4nuhc4wan8Ba3KFZqcF7TzDs9DESscaNw; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19838%7CMCMID%7C21906518778745790610441888094042534602%7CMCAAMLH-1714581767%7C7%7CMCAAMB-1714581767%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1713984167s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C-1889180192; dfpfpt=40a47c4d44934ad393f6bf529b1ba3b9; lang=v=2&lang=en-us; fptctx2=taBcrIH61PuCVH7eNCyH0CYjjbqLuI8XF8pleSQW5NaA8YRH7mJI2g724MUYj7VF4h2lnI3T6ErxEBEF%252fbF0OEK%252bVIHxnJBWIfeYfU%252fs03AX5fRN314UjG%252fer8001vBM2h1n%252ft2PTYfBgl0WrPHpZTg8m52Zs0u%252bSsN27GuFFlGe4LY6N9HPVhuCsNPdxMSIeh%252bO1c7paaPWjq9ytL4Fh0YoDJ3KhTn5U8Xp7%252fD9UGPWNdVwLPw4B%252btLFG5g9zJFqHU6ZCfs9yxN2A4cSIup%252fQOdKNGYSzegHefCgGjZQylM4zldl0TkbZC%252b6NxD8gjpm2XDpewrbO7WELAQbalEBHZdWZYNUtWtXr6iPkGEpa0%253d; UserMatchHistory=AQIiDZkmp_scmwAAAY8RET33yj2whj0VTRh6h_ma4LzlfU9kykwp9mJVPdQeQMmvKs6uZ5qr3d6Sh8eW-JTRGUx2rWh19lUUE_ctfo8oiU6BDKoDO8QKJg4p740GYPb0o0B3w-si-nT3m-A2bJ0Rbk8qy9z0KVWsrpjq2c1YWkro5hx3nhbo7cqOTl0W3uNT-ciH6bQ6wNaJded8sG3lTFAxXAZft8KFNO-vICfk1oj6AKozQOIW0Wc4jumjZnFwW83ctWoUT5gTx5qwTUZvPm9VSIksHMtuseSWdvAPpRbXGDE0Gbc8ttlXRvhKj6OAnZOWCRiTVNK24SPB2c_yzg5vZpm1JOwjNC8bhPrwdyli74j1bQ; lidc="b=OB70:s=O:r=O:a=O:p=O:g=3411:u=360:x=1:i=1713984881:t=1714068578:v=2:sig=AQHzajTqEZOlfs8Rx90n9uVOB2qbnyDe"'  # place cookie here


class LinkedIn:
    def __init__(self):
        self.fieldnames = ["Profile Link", "Name", "Designation", "Location"]

    def saveData(self, dataset):
        with open(output_file_name, mode='a+', encoding='utf-8-sig', newline='') as csvFile:

            writer = csv.DictWriter(
                csvFile, fieldnames=self.fieldnames, delimiter=',', quotechar='"')
            if os.stat(output_file_name).st_size == 0:
                writer.writeheader()
            writer.writerow({
                "Profile Link": dataset[0],
                "Name": dataset[1],
                "Designation": dataset[2],
                "Location": dataset[3]
            })

    @classmethod
    def getCompanyID(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Dnt': '1',
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        }
        try:
            resp = requests.get(company_link, headers=headers).text
        except:
            print("Failed to open {}".format(company_link))
            return None
        try:
            companyID = re.findall(
                r'"objectUrn":"urn:li:organization:([\d]+)"', resp)[0]
        except:
            print("Company ID not found")
            return None
        return companyID

    def paginateResults(self, companyID):
        headers = {
            'Accept': 'application/vnd.linkedin.normalized+json+2.1',
            'Cookie': cookies,
            'Csrf-Token': re.findall(r'JSESSIONID="(.+?)"', cookies)[0],
            'Dnt': '1',
            'Referer': 'https://www.linkedin.com/search/results/people/?currentCompany=%5B%22' + companyID + '%22%5D&origin=COMPANY_PAGE_CANNED_SEARCH&page=2&sid=7Gd',
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'X-Li-Lang': 'en_US',
            'X-Li-Page-Instance': 'urn:li:page:d_flagship3_search_srp_people_load_more;Ux/gXNk8TtujmdQaaFmrPA==',
            'X-Restli-Protocol-Version': '2.0.0',
        }
        for page_no in range(0, 1000, 10):
            print("Checking facet: {}/990".format(page_no))
            link = f"https://www.linkedin.com/voyager/api/graphql?variables=(start:{page_no},origin:COMPANY_PAGE_CANNED_SEARCH,query:(flagshipSearchIntent:SEARCH_SRP,queryParameters:List((key:currentCompany,value:List({companyID})),(key:resultType,value:List(PEOPLE))),includeFiltersInResponse:false))&queryId=voyagerSearchDashClusters.e1f36c1a2618e5bb527c57bf0c7ebe9f"
            
            try:
                response = s.get(link, headers=headers).json()
            except Exception as e:
                print(f"Failed to fetch data from {link} with error {e}")
                continue

            results = response.get('included', [])
            for person_data in results:
                if person_data.get('$type') == "com.linkedin.voyager.dash.search.EntityResultViewModel":
                    title = person_data.get('title')
                    primarySubtitle = person_data.get('primarySubtitle')
                    secondarySubtitle = person_data.get('secondarySubtitle')

                    person_name = title.get('text', 'N/A') if title else 'N/A'
                    profile_link = person_data.get('navigationUrl', 'N/A')
                    designation = primarySubtitle.get('text', 'N/A') if primarySubtitle else 'N/A'
                    person_location = secondarySubtitle.get('text', 'N/A') if secondarySubtitle else 'N/A'

                    print("Profile Link: {}".format(profile_link))
                    print("Name: {}".format(person_name))
                    print("Designation: {}".format(designation))
                    print("Location: {}".format(person_location))
                    print()

                    dataset = [profile_link, person_name, designation, person_location]
                    self.saveData(dataset)
            print("Waiting for {} seconds".format(pagination_delay))
            sleep(pagination_delay)



if __name__ == "__main__":
    companyID = LinkedIn.getCompanyID()
    if companyID is not None:
        linkedin = LinkedIn()
        linkedin.paginateResults(companyID)