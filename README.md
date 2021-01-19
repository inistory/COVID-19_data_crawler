# Covid19_data_crawler

Covid19_data_crawling by Python

https://www.worldometers.info/coronavirus/

- soup 객체에 있는 국가들의 코로나 관련 데이터에 대해 크롤링
- 크롤링된 코로나 관련 데이터 중 국가 이름이 key, 확진자, 사망자, 완치가 value인 딕셔너리 형태로 저장
- 각 데이터는 정수 자료형으로 표현하되 유효하지 않은 값은 문자열 "N/A"로 처리
