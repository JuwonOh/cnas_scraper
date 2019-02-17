# cnas_scraper
미국의 씽크탱크인 Center for a New American Security의 자료들(reports, commentar, congressional-testimony, transcript, blog)을 받아오기 위한 크롤러입니다.

## User guide

크롤러의 파이썬 파일은 util.py, scraper.py 그리고 parser.py download.py로 구성되어 있습니다. 
util.py는 크롤링 한 파이썬의 beautifulsoup 패키지를 받아서 url내의 html정보를 정리합니다.
scraper는 util.py내의 사이트내의 url 링크들을 get_soup함수를 통해 모아줍니다.
parser는 이렇게 만들어진 url리스트를 통해서 각 분석들의 제목/일자/내용을 모아줍니다.
downdload는 parser에서 parsing된 각 보고서를 다운로드 해줍니다.

```
전체 카테고리의 자료를 일정한 조건으로 크롤링하기 위해서는 python scraping_latest_news.py를 사용하세요.
```
특정한 페이지를 parse하기 위해서는 usage.ipynb의 다음 함수들을 참고하세요.
```
[1 / 10] (February 12, 2019) 
Negotiating With North Korea
How Will This End?

[2 / 10] (February 06, 2019) 
Understanding China's AI Strategy
Clues to Chinese Strategic Thinking on Artificial Intelligence and National Security

[3 / 10] (January 29, 2019) 
A Realistic Path for Progress on Iran
12 Guiding Principles to Achieve U.S. Policy Goals

[4 / 10] (January 24, 2019) 
Financial Networks of Mass Destruction

[5 / 10] (January 15, 2019) 
Rethinking Requirements and Risk in the New Space Age

[6 / 10] (December 02, 2018) 
Ending Gaza’s Perpetual Crisis
A New U.S. Approach

Stop scrapping. 6 / 10 report was scrapped
The oldest blog article has been created after 2018-12-01
```
특정한 기사를 scrap하려면 다음과 같은 코드를 참고하세요.
```
from cnas_scraper import parse_page
def pprint(json_object):
    for k, v in json_object.items():
        print('{} : {} ..'.format(k, str(v)[:100]))
    print('\n')

SLEEP = 0.5

   
for url in report_urls[:3]:
    rjson_object = parse_page(url)
    pprint(rjson_object)

for url in article_urls[:3]:
    ajson_object = parse_page(url)
    pprint(ajson_object)
```

## 참고 코드

본 코드는 https://github.com/lovit/whitehouse_scraper를 참조하여 만들어졌습니다.
