import csv
import urllib.request
from bs4 import BeautifulSoup

BASE_URL = 'https://www.weblancer.net/jobs/'


def get_html(url):
    """
     get html from site
    """
    response = urllib.request.urlopen(url)
    return response.read()


def get_page_count(html):
    """
     get number of pages
    """
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find('div', class_='pagination_box')
    last_page = pagination.findAll('a')[-1]['href'][12:]

    return last_page


def check(current_row):
    """
    check correct information
    """
    if current_row[-1].span.span is not None:
        return current_row[-1].span.span.text
    else:
        return "Нет инфы"


def parse(html):
    """
    parse site and return information about projects
    """
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.findAll('div', class_='cols_table')
    rows = table[1].findAll('div', class_='row')

    projects = []
    for row in rows:
        current_row = row.findAll('div')
        projects.append({
            'title': current_row[0].h2.text.replace('\u2062', "").replace('\xe9', ""),
            'price': current_row[2].text[1:],
            'categories': current_row[4].text.replace('\xa0', ""),
            'opened': check(current_row)
        })

    return projects


def save(projects, path):
    """
    save data to csv file
    """
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Проект', 'Цена', 'Сфера', 'Как давно создан'))

        for project in projects:
            writer.writerow((project['title'], project['price'], project['categories'].encode('utf-8').decode('utf-8'), project['opened']))


def main():
    page_count = get_page_count(get_html(BASE_URL))
    page_count = int(page_count)
    print('Всего найдено страниц %d' % page_count)

    projects = []
    for page in range(1, page_count + 1):
        print('Парсинг %d%%' % (page / page_count * 100))
        print(page)
        projects.extend(parse(get_html(BASE_URL + '?page=%d' % page)))

    print("Парсинг закончен")
    print(projects)

    save(projects, 'projects.csv')


if __name__ == '__main__':
    main()
