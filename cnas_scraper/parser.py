from .utils import get_soup
from .utils import now

def parse_page(url):
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
    return None

def parse_report(url):
    def parse_author(soup):
        author = soup.find('a', class_='contributor').text
        if not author:
            return ''
        return author

    def parse_title(soup):
        title = soup.find('div', class_='article__header__title-group').text
        if not title:
            return ''
        return title

    def parse_date(soup):
        date = soup.find('p', class_= 'sans-serif fz11 bold uppercase margin-bottom-1em').text
        if not date:
            return ''
        return date

    def parse_content(soup):
        sub_content = soup.find_all('div', class_= 'wrapper wysiwyg margin-vertical')
        content = '\n'.join([p.text.strip() for p in sub_content])
        if not content:
            return ''
        return content

    def parse_publication_link(soup):
        for a in soup.select('a'):
            if '//s3.amazonaws.com/files.cnas.org/documents/' in a.attrs.get('href', ''):
                return a.attrs['href']

    soup = get_soup(url)
    temp_content_url = parse_publication_link(soup)
    if 'https:' not in temp_content_url:
        content_url = 'https:' + temp_content_url
    else:
        content_url = temp_content_url
    return {
        'url': url,
        'title': parse_title(soup),
        'date': parse_date(soup),
        'author': parse_author(soup),
        'content': parse_content(soup),
        'content_url': content_url+ ".pdf"
    }

def parse_testimony(url):
    def parse_author(soup):
        author = soup.find('a', class_='contributor').text
        if not author:
            return ''
        return author

    def parse_title(soup):
        title = soup.find('div', class_='article__header__title-group').text
        if not title:
            return ''
        return title

    def parse_date(soup):
        date = soup.find('p', class_= 'sans-serif fz11 bold uppercase margin-bottom-1em').text
        if not date:
            return ''
        return date

    def parse_content(soup):
        sub_content = soup.find_all('div', class_= 'wrapper wysiwyg margin-vertical')
        content = '\n'.join([p.text.strip() for p in sub_content])
        if not content:
            return ''
        return content

    def parse_publication_link(soup):
        for a in soup.select('a'):
            if '//s3.amazonaws.com/files.cnas.org/documents/' in a.attrs.get('href', ''):
                return a.attrs['href']
    soup = get_soup(url)
    content_url = parse_publication_link(soup)
    return {
        'url': url,
        'title': parse_title(soup),
        'date': parse_date(soup),
        'content': parse_content(soup),
        'author': parse_author(soup),
        'content_url': 'https:' + content_url + ".pdf"
    }
def parse_commentary(url):
    def parse_author(soup):
        sub_author = soup.find_all('a', class_='contributor')
        author = '\n'.join([p.text.strip() for p in sub_author])
        if not author:
            return ''
        return author

    def parse_title(soup):
        title = soup.find('div', class_='article__header__title-group').text
        if not title:
            return ''
        return title

    def parse_date(soup):
        date = soup.find('p', class_= 'sans-serif fz11 bold uppercase margin-bottom-1em').text
        if not date:
            return ''
        return date

    def parse_content(soup):
        sub_content = soup.find_all('div', class_= 'wrapper wysiwyg margin-vertical drop-cap')
        content = '\n'.join([p.text.strip() for p in sub_content])
        if not content:
            return ''
        return content

    soup = get_soup(url)
    return {
        'url': url,
        'title': parse_title(soup),
        'date': parse_date(soup),
        'content': parse_content(soup),
        'author': parse_author(soup)
    }

def parse_transcript(url):
    def parse_author(soup):
        sub_author = soup.find_all('a', class_='contributor')
        author = '\n'.join([p.text.strip() for p in sub_author])
        if not author:
            return ''
        return author

    def parse_title(soup):
        title = soup.find('div', class_='article__header__title-group').text
        if not title:
            return ''
        return title

    def parse_date(soup):
        date = soup.find('p', class_= 'sans-serif fz11 bold uppercase margin-bottom-1em').text
        if not date:
            return ''
        return date

    def parse_content(soup):
        content = soup.find('div', class_= 'wrapper wysiwyg margin-vertical drop-cap')
        if not content:
            return ''
        return content

    soup = get_soup(url)
    return {
        'url': url,
        'title': parse_title(soup),
        'date': parse_date(soup),
        'content': parse_content(soup),
        'author': parse_author(soup)
    }

def parse_blog(url):
    def parse_author(soup):
        sub_author = soup.find_all('a', class_='contributor')
        author = '\n'.join([p.text.strip() for p in sub_author])
        if not author:
            return ''
        return author

    def parse_title(soup):
        title = soup.find('div', class_='article__header__title-group').text
        if not title:
            return ''
        return title

    def parse_date(soup):
        date = soup.find('p', class_= 'sans-serif fz11 bold uppercase margin-bottom-1em').text
        if not date:
            return ''
        return date

    def parse_content(soup):
        content = soup.find('div', class_= 'wrapper wysiwyg margin-vertical drop-cap')
        if not content:
            return ''
        return content

    soup = get_soup(url)
    return {
        'url': url,
        'title': parse_title(soup),
        'date': parse_date(soup),
        'content': parse_content(soup),
        'author': parse_author(soup)
    }
