import requests
import re
from bs4 import BeautifulSoup

def crawling(soup):
    result = []
    result_list = soup.find("tbody").find_all("tr")
    
    for re in result_list:
        re = re.get_text().split()#.replace("\t","")
        result.append(re)
    result = result[7:]
    #USA 부터는 앞쪽 숫자제거
    for i in range(1,len(result)):
        del result[i][0] #제거
        
        
    #리스트 수정 나라(0),확진자(1), 사망자(3), 완치자(5)
    result2 = []
    for i in range(len(result)):
        del result[i][6:]
        del result[i][2] 
        del result[i][3]
        
    #print(result)
    
    #딕셔너리
    data = dict()
    for i in range(len(result)):
        data[result[i][0]] = result[i][1:]#정수 자료형
    print(data)

def main() :
    html = requests.get("https://www.worldometers.info/coronavirus/")
    soup = BeautifulSoup(html.text, "html.parser")
    crawling(soup)

if __name__ == "__main__" :
    main()
