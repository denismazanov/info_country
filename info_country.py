import requests,os
os.chdir(input("write directory/folder for saving files"))
while True:
    try:
        country = input("\tWrite Country\t")
        req_country = requests.get(f'https://restcountries.eu/rest/v2/name/{country}')
        info_country = req_country.json()[0]
    except Exception:
        print("You input incorrect country name")
    else:
        len_borders = len(info_country["borders"])
        capital = info_country["capital"]
        region = info_country["region"]
        subregion = info_country["subregion"]
        population = "{:,}".format(info_country["population"])
        area = f"{info_country['area']} square kilometer"
        cur_code = info_country["currencies"][0]["code"]
        cur_name = info_country["currencies"][0]["name"]
        lang_name = info_country["languages"][0]["name"]
        lang_nnative = info_country["languages"][0]["nativeName"]

        try:
            file=f"{country}_info.txt"
            if os.path.exists(file):
                print("File exists .Try another country")
                continue
        except Exception:
            print("Error accured. Please try again")
        else:
            with open(file,"a") as f:
                num=1
                info_borders = f"{country.title()} has borders with {len_borders} countries :"
                info_all = f"\t\tAbout {country.title()}\n Capital : {capital}\nRegion : {region}\nPopulation : {population}\n" \
                    f"Area : {area}\nCurrency : {cur_code} ( {cur_name} )\nLanguage : {lang_name}\n{info_borders}\n"
                f.write(info_all)
                for border in info_country["borders"]:
                    req_border = requests.get(f"https://restcountries.eu/rest/v2/alpha/{border}")
                    border_name = f" {req_border.json()['name']}"
                    f.write(f"{num}{border_name}\n")
                    num+=1
            print("File created")
