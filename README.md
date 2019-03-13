# cnas_scraper
미국의 씽크탱크인 Center for a New American Security의 자료들(reports, commentar, congressional-testimony, transcript, blog)을 받아오기 위한 크롤러입니다.

## User guide# rand_scraper

미국의 싱크탱크인 랜드 연구소(The RAND Corporation, https://www.rand.org)의 자료들을 받아오는 크롤러입니다. 랜드 연구소내의 2가지 자료들(Blog post, Reserch paper)들에 대한 자료를 받아옵니다.

## User guide

크롤러의 파이썬 파일은 util.py, scraper.py, parser.py, downloader.py 그리고 scraping_latest_news.py 총 다섯가지로 구성되어 있습니다. 
util.py는 크롤링 한 파이썬의 beautifulsoup 패키지를 받아서 url내의 html정보를 정리하는 등 scraper가 필요한 기본적인 기능을 가지고 있습니다.
parser.py는 모아진 url리스트를 통해서 각 분석들의 제목/일자/내용 등의 문자, 시간 데이터들을 parsing 합니다.
scraper.py는 사이트내의 url 링크들을 get_soup함수를 통해 모아주고, parser를 통해서 json형식으로 변환시킵니다.
downloader.py는 reserch paper와 Brookings papers on economy activity article의 pdf파일을 다운로드 하는 파일입니다.
scraping_latest_news.py는 scraper.py를 통해 만들어진 json파일을 저장시켜줍니다. scraping_latest_news.py파일의 parameter는 다음과 같습니다.

Using Python script with arguments

| Argument name | Default Value | Note |
| --- | --- | --- |
| begin_date | 2018-07-01 | datetime YYYY-mm-dd |
| directory | ./output/ | Output directory |
| max_num | 1000 | Maximum number of news to be scraped |
| sleep | 1.0 | Sleep time for each news |
| verbose | False, store_true | If True use verbose mode |

만일 2018년 7월 1일부터 작성된 자료를 1000개까지 받고 싶다면 다음과 같이 실행코드를 입력해주시면 됩니다.

```
scraping_latest_news.py --begin_date 2018/07/01 --directory ./output --max_num 1000 --sleep 1.0
```
최근 순서대로 크롤링한 파일을 살펴보고 싶을때는 usage.ipynb를 사용하세요.

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


## 참고 코드

본 코드는 https://github.com/lovit/whitehouse_scraper를 참조하여 만들어졌습니다.
