import unittest
import requests
import datetime
import json
import csv

class challenge10(unittest.TestCase):

    vehicle_dict = {"Automobiles": "VEHTYPE_V",
                    "Dirt Bikes": "VEHTYPE_D",
                    "ATVs": "VEHTYPE_A",
                    "Jet Skis": "VEHTYPE_J",
                    "Motorcycle": "VEHTYPE_C",
                    "RVs": "VEHTYPE_R",
                    "Industrial Equipment": "VEHTYPE_E"}

    url = "https://www.copart.com/public/lots/search"
    payload = {"draw": "4",
               "columns[0][data]": "0",
               "columns[0][name]": "",
               "columns[0][searchable]": "true",
               "columns[0][orderable]": "false",
               "columns[0][search][value]": "",
               "columns[0][search][regex]": "false",
               "columns[1][data]": "1",
               "columns[1][name]": "",
               "columns[1][searchable]": "true",
               "columns[1][orderable]": "false",
               "columns[1][search][value]": "",
               "columns[1][search][regex]": "false",
               "columns[2][data]": "2",
               "columns[2][name]": "",
               "columns[2][searchable]": "true",
               "columns[2][orderable]": "true",
               "columns[2][search][value]": "",
               "columns[2][search][regex]": "false",
               "columns[3][data]": "3",
               "columns[3][name]": "",
               "columns[3][searchable]": "true",
               "columns[3][orderable]": "true",
               "columns[3][search][value]": "",
               "columns[3][search][regex]": "false",
               "columns[4][data]": "4",
               "columns[4][name]": "",
               "columns[4][searchable]": "true",
               "columns[4][orderable]": "true",
               "columns[4][search][value]": "",
               "columns[4][search][regex]": "false",
               "columns[5][data]": "5",
               "columns[5][name]": "",
               "columns[5][searchable]": "true",
               "columns[5][orderable]": "true",
               "columns[5][search][value]": "",
               "columns[5][search][regex]": "false",
               "columns[6][data]": "6",
               "columns[6][name]": "",
               "columns[6][searchable]": "true",
               "columns[6][orderable]": "true",
               "columns[6][search][value]": "",
               "columns[6][search][regex]": "false",
               "columns[7][data]": "7",
               "columns[7][name]": "",
               "columns[7][searchable]": "true",
               "columns[7][orderable]": "true",
               "columns[7][search][value]": "",
               "columns[7][search][regex]": "false",
               "columns[8][data]": "8",
               "columns[8][name]": "",
               "columns[8][searchable]": "true",
               "columns[8][orderable]": "true",
               "columns[8][search][value]": "",
               "columns[8][search][regex]": "false",
               "columns[9][data]": "9",
               "columns[9][name]": "",
               "columns[9][searchable]": "true",
               "columns[9][orderable]": "true",
               "columns[9][search][value]": "",
               "columns[9][search][regex]": "false",
               "columns[10][data]": "10",
               "columns[10][name]": "",
               "columns[10][searchable]": "true",
               "columns[10][orderable]": "true",
               "columns[10][search][value]": "",
               "columns[10][search][regex]": "false",
               "columns[11][data]": "11",
               "columns[11][name]": "",
               "columns[11][searchable]": "true",
               "columns[11][orderable]": "true",
               "columns[11][search][value]": "",
               "columns[11][search][regex]": "false",
               "columns[12][data]": "12",
               "columns[12][name]": "",
               "columns[12][searchable]": "true",
               "columns[12][orderable]": "true",
               "columns[12][search][value]": "",
               "columns[12][search][regex]": "false",
               "columns[13][data]": "13",
               "columns[13][name]": "",
               "columns[13][searchable]": "true",
               "columns[13][orderable]": "true",
               "columns[13][search][value]": "",
               "columns[13][search][regex]": "false",
               "columns[14][data]": "14",
               "columns[14][name]": "",
               "columns[14][searchable]": "true",
               "columns[14][orderable]": "false",
               "columns[14][search][value]": "",
               "columns[14][search][regex]": "false",
               "columns[15][data]": "15",
               "columns[15][name]": "",
               "columns[15][searchable]": "true",
               "columns[15][orderable]": "false",
               "columns[15][search][value]": "",
               "columns[15][search][regex]": "false",
               "start": "0",
               "length": "100",
               "search[value]": "",
               "search[regex]": "false",
               "filter[MODL]": "lot_model_desc:\"CIVIC SI\"",
               "filter[YEAR]": "lot_year:\"2014\"",
               "filter[VEHT]": "vehicle_type_code:VEHTYPE_D",
               "query": "honda",
               "watchListOnly": "false",
               "freeFormSearch": "true",
               "page": "0",
               "size": "100",
               "includeTagByField[MODL]": "{!tag = MODL}",
               "includeTagByField[YEAR]": "{!tag = YEAR}",
               "includeTagByField[VEHT]": "{!tag = VEHT}"}
    headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
               "Accept-Encoding": "gzip, deflate, br",
               "Accept-Language": "en-US,en;q=0.5",
               "Cache-Control": "max-age=0",
               "Connection": "keep-alive",
               # "Content-Length": "3493",
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "Cookie": "g2usersessionid=5fbdf2bd9d3db4851a39c669a2c8df33; G2JSESSIONID=B7306AED6ABE01F2A330239B97987453-n1; visid_incap_242093=NXzBZgQSTOuN2bP3+SFxxJ+TQF4AAAAAQUIPAAAAAAAgSqxWc/TnUpGwQF5NozRt; incap_ses_1160_242093=4fxAL1U/2TWboosRTyYZEJ+TQF4AAAAAsO7WutDwY18Sl/2r6pmPOA==; userLang=en; copartTimezonePref=%7B%22displayStr%22%3A%22PST%22%2C%22offset%22%3A-8%2C%22dst%22%3Afalse%2C%22windowsTz%22%3A%22America%2FLos_Angeles%22%7D; timezone=America%2FLos_Angeles; g2app.locationInfo=%7B%22countryCode%22%3A%22USA%22%2C%22countryName%22%3A%22United%20States%22%2C%22stateName%22%3A%22California%22%2C%22stateCode%22%3A%22CA%22%2C%22cityName%22%3A%22Hayward%22%2C%22latitude%22%3A37.66882%2C%22longitude%22%3A-122.0808%2C%22zipCode%22%3A%2294540%22%2C%22timeZone%22%3A%22-07%3A00%22%7D; s_fid=6D57C48011F67646-31EE8B51CD3333F9; s_depth=1; s_pv=public%3Ahomepage; s_nr=1581290442830-New; s_vnum=1583882422649%26vn%3D1; s_invisit=true; s_lv=1581290442830; s_lv_s=First%20Visit; s_cc=true; s_vi=[CS]v1|2F2049DB8515AE3F-60000B02A62B1121[CE]; _gcl_au=1.1.1667976879.1581290424; usersessionid=b8d4872aca78e4e741920941deb62716; OAGEO=US%7C%7C%7C%7C%7C%7C%7C%7C%7C%7C; OAID=17e763c0eb15f40a09818daa0b13fa45; s_ppv=public%253Ahomepage%2C40%2C9%2C481%2C320%2C480%2C320%2C480%2C1.25%2CL; __gads=ID=dd8dc8391adf2a5b:T=1581290423:S=ALNI_MaFqTOulBe1D7KUdgQLhibPnReAGA; _ga=GA1.2.1094098984.1581290424; _gid=GA1.2.250963414.1581290425; _gat_UA-90930613-1=1; _fbp=fb.1.1581290426160.897362765; s_ppvl=9; s_sq=copart-g2-us-prod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dpublic%25253Ahomepage%2526link%253D%25252Fimages%25252Ficons%25252Fsearch.svg%2526region%253Dmobile-search-form%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dpublic%25253Ahomepage%2526pidt%253D1%2526oid%253D%25250A%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%25250A%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%2526oidt%253D3%2526ot%253DSUBMIT",
               "Host": "www.copart.com",
               "Origin": "https://www.copart.com",
               # "Referer":"https://www.copart.com/lotSearchResults/?free=true&query=nissan",
               "TE": "Trailers",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
               "X-Requested-With": "XMLHttpRequest",
               "X-XSRF-TOKEN": "dc4c21c3-4908-41d4-b980-d679564b508c"}

    f = open("totalcars.log", "a+")
    now = datetime.datetime.now()
    f.write(now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
    with open('copart_data.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                payload.update({"query": row[0]})
                payload.update({"filter[MODL]": "lot_model_desc:\"" + row[1].upper() + "\""})
                payload.update({"filter[YEAR]": "lot_year:\"" + row[2] + "\""})
                for key in vehicle_dict.keys():
                    if row[3] == key:
                        payload.update({"filter[VEHT]": "vehicle_type_code:" + vehicle_dict[key]})
                response = requests.request("POST", url, data=payload, headers=headers)
                response_dict = json.loads(response.text)
                f.write(row[2] + " " + row[0] + " " + row[1] + ": "
                        + str(response_dict['data']['results']['totalElements']) + " found\n")
                line_count += 1
        f.write("\n")
    f.close()


if __name__ == '__main__':
    unittest.main()
