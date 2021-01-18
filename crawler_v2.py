import requests
import re
from bs4 import BeautifulSoup

def crawling(soup):
    # country_all = [] 
    # country_list = soup.find("tbody").find_all("a",class_="mt_a")
    # for country in country_list:
    #     country_all.append(country.get_text())
    # country_all.insert(0,"World")
    # #print(country_all)



    result_old = []
    result_new = []
    result_list = soup.find("tbody").find_all("tr")
    
    for res in result_list:
        #res_old = res.get_text()
        res_old = res.get_text().split()
        #res_new = re.findall("\d+",res_old)

        result_old.append(res_old)
        #result_new.append(res_new)
    #result = result[7:]
    print(res_old)

    # for i in range(1,len(result)):
    #     del result[i][0]
        
        

    # result2 = []
    # for i in range(len(result)):
    #     del result[i][6:]
    #     del result[i][2] 
    #     del result[i][3]
        
    # #print(result)
    
 
    # data = dict()
    # for i in range(len(result)):
    #     data[country_all[i]] = result[i][1:]
    # print(data)

def main() :
    html = requests.get("https://www.worldometers.info/coronavirus/")
    soup = BeautifulSoup(html.text, "html.parser")
    crawling(soup)

if __name__ == "__main__" :
    main()
