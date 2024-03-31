# data portal
# https://www.data.go.kr/iim/api/selectAPIAcountView.do

# vworld API
# 박물관미술관 - https://www.vworld.kr/dev/v4dv_2ddataguide2_s002.do?svcIde=dgmuseumart
import dotenv
import os
dotenv.load_dotenv()

import requests

def request_api( ):
    #os.getenv("VWORLD_API_KEY")
    api_url = "http://api.data.go.kr/openapi/tn_pubr_public_museum_artgr_info_api"
    params = {'serviceKey': 'HdPVZBWIyEo6eTW3QUk1W2fhwWiBXSaShB33mzL2swdUPAfxsHyNfZ6oU2u+QUfNUe717QDwcGD7U6b8Vk3gHg==', 'pageNo': '1', 'numOfRows': '100', 'type': 'xml', 'fcltyNm': '', 'fcltyType': '', 'rdnmadr': '', 'lnmadr': '', 'latitude': '', 'longitude': '', 'operPhoneNumber': '', 'operInstitutionNm': '', 'homepageUrl': '', 'fcltyInfo': '', 'weekdayOperOpenHhmm': '', 'weekdayOperColseHhmm': '', 'holidayOperOpenHhmm': '', 'holidayCloseOpenHhmm': '', 'rstdeInfo': '', 'adultChrge': '', 'yngbgsChrge': '', 'childChrge': '', 'etcChrgeInfo': '', 'fcltyIntrcn': '', 'trnsportInfo': '', 'phoneNumber': '', 'institutionNm': '', 'referenceDate': '', 'instt_code': ''}

    print( os.getenv("DATAPORTAL_API_KEY") )
    response = requests.get(api_url, params=params)
    return response

def fecth_result( result ):
    return result.content

def main() :
    # request api
    result = fecth_result( request_api() )
    print( result )



if __name__ == "__main__":
    main()
