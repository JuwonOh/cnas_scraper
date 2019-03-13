from .utils import get_soup
from .utils import now
from dateutil.parser import parse

def parse_page(url):
    """
    Argument
    --------
    url : str
        Web page url

    Returns
    -------
    json_object : dict
        JSON format web page contents
        It consists with
            title : article title
            time : article written time
            content : text with line separator \\n
            url : web page url
            scrap_time : scrapped time
    """
    try:
        if '/reports/' in url:
            return parse_report(url)
        if '/commentary/' in url:
            return parse_commentary(url)
        if '/congressional-testimony/' in url:
            return parse_testimony(url)
        if '/transcript/' in url:
            return parse_transcript(url)
        if '/blog/' in url:
            return parse_blog(url)
    except Exception as e:
        print(e)
        print('Parsing error from {}'.format(url))
        return None

def parse_report(url):
    def parse_author(soup):
        author = soup.find('a', class_='contributor')
        if not author:
            return ''
        return author.text

    def parse_title(soup):
        title = soup.find('div', class_='article__header__title-group')
        if not title:
            return ''
        return title.text

    def parse_date(soup):
        date = soup.find('p', class_= 'sans-serif fz11 bold uppercase margin-bottom-1em')
        if not date:
            return ''
        return parse(date.text)

    def parse_content(soup):
        sub_content = soup.find_all('div', class_= 'wrapper wysiwyg margin-vertical')
        if not sub_content:
            return ''
        content = '\n'.join([p.text.strip() for p in sub_content])
        return content

    def parse_publication_link(soup):
        a =  soup.find_all('a', class_='button margin-top-1em')
        for b in a:
            b=b
        if '//s3.amazonaws.com/files.cnas.org/documents/' in b.attrs['href']:
            url = 'https:' + b.attrs['href'] + ".pdf"
            return url
        if 'print()' in b.attrs['href']:
            return 'no link'

    soup = get_soup(url)
    content_url = parse_publication_link(soup)
    return {
        'url': url,
        'title': parse_title(soup),
        'date': parse_date(soup),
        'author': parse_author(soup),
        'content': parse_content(soup),
        'content_url':  content_url,
        'scrap_time' : now()
    }

def parse_testimony(url):
    def parse_author(soup):
        author = soup.find('a', class_='contributor')
        if not author:
            author = soup.find('span', class_='contributor')
            return author.text
        return author.text

    def parse_title(soup):
        title = soup.find('div', class_='article__header__title-group')
        if not title:
            return ''
        return title.text

    def parse_date(soup):
        date = soup.find('p', class_= 'sans-serif fz11 bold uppercase margin-bottom-1em')
        if not date:
            return ''
        return parse(date.text)

    def parse_content(soup):
        sub_content = soup.find_all('div', class_= 'wrapper wysiwyg margin-vertical drop-cap')
        if not sub_content:
            return ''
        content = '\n'.join([p.text.strip() for p in sub_content])
        return content

    def parse_publication_link(soup):
        a =  soup.find_all('a', class_='button margin-top-1em')
        for b in a:
            b=b
        if '//s3.amazonaws.com/files.cnas.org/documents/' in b.attrs['href']:
            url = 'https:' + b.attrs['href'] + ".pdf"
            return url
        if 'print()' in b.attrs['href']:
            return 'no link'

    soup = get_soup(url)
    content_url = parse_publication_link(soup)
    return {
        'url': url,
        'title': parse_title(soup),
        'date': parse_date(soup),
        'content': parse_content(soup),
        'author': parse_author(soup),
        'content_url': content_url,
        'scrap_time' : now()
    }
def parse_commentary(url):
    def parse_author(soup):
        sub_author = soup.find_all('a', class_='contributor')
        if not sub_author:
            return ''
        author = '\n'.join([p.text.strip() for p in sub_author])
        return author

    def parse_title(soup):
        title = soup.find('div', class_='article__header__title-group')
        if not title:
            return ''
        return title.text

    def parse_date(soup):
        date = soup.find('p', class_= 'sans-serif fz11 bold uppercase margin-bottom-1em')
        if not date:
            return ''
        return parse(date.text)

    def parse_content(soup):
        sub_content = soup.find_all('div', class_= 'wrapper wysiwyg margin-vertical drop-cap')
        if not sub_content:
            return ''
        content = '\n'.join([p.text.strip() for p in sub_content])
        return content

    soup = get_soup(url)
    return {
        'url': url,
        'title': parse_title(soup),
        'date': parse_date(soup),
        'content': parse_content(soup),
        'author': parse_author(soup),
        'scrap_time' : now()
    }

def parse_transcript(url):
    def parse_author(soup):
        sub_author = soup.find_all('a', class_='contributor')
        if not sub_author:
            return ''
        author = '\n'.join([p.text.strip() for p in sub_author])
        return author

    def parse_title(soup):
        title = soup.find('div', class_='article__header__title-group')
        if not title:
            return ''
        return title.text

    def parse_date(soup):
        date = soup.find('p', class_= 'sans-serif fz11 bold uppercase margin-bottom-1em')
        if not date:
            return ''
        return parse(date.text)

    def parse_content(soup):
        content = soup.find('div', class_= 'wrapper wysiwyg margin-vertical drop-cap')
        if not content:
            return ''
        return content.text

    soup = get_soup(url)
    return {
        'url': url,
        'title': parse_title(soup),
        'date': parse_date(soup),
        'content': parse_content(soup),
        'author': parse_author(soup),
        'scrap_time' : now()
    }

def parse_blog(url):
    def parse_author(soup):
        sub_author = soup.find_all('a', class_='contributor')
        if not sub_author:
            return ''
        author = '\n'.join([p.text.strip() for p in sub_author])
        return author

    def parse_title(soup):
        title = soup.find('div', class_='article__header__title-group')
        if not title:
            return ''
        return title.text

    def parse_date(soup):
        date = soup.find('p', class_= 'sans-serif fz11 bold uppercase margin-bottom-1em')
        if not date:
            return ''
        return parse(date.text)

    def parse_content(soup):
        content = soup.find('div', class_= 'wrapper wysiwyg margin-vertical drop-cap')
        if not content:
            return ''
        return content.text

    soup = get_soup(url)
    return {
        'url': url,
        'title': parse_title(soup),
        'date': parse_date(soup),
        'content': parse_content(soup),
        'author': parse_author(soup),
        'scrap_time' : now()
    }
