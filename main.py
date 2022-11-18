from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pprint import pprint
import collections
import datetime
import pandas


def count_years_from_establish():
    establish_year = 1920
    now_year = datetime.date.today().year
    winery_age = now_year - establish_year
    if 10 < winery_age % 100 < 20 or winery_age % 10 in (0, 5, 6, 7, 8, 9):
        return f'{winery_age} лет'
    elif winery_age % 10 == 1:
        return f'{winery_age} год'
    else:
        return f'{winery_age} года'


def get_wines_from_excel(filename, sheet_name=0):
    excel_data_df = pandas.read_excel(
        filename,
        sheet_name=sheet_name,
        na_values=None,
        keep_default_na=False,
    )

    translated_excel = excel_data_df.to_dict(orient='record')
    wines = collections.defaultdict(list)
    for wine in translated_excel:
        category = wine['Категория']
        wines[category].append(wine)
    products_from_excel = {key: value for key, value in sorted(wines.items())}
    return products_from_excel


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    rendered_page = template.render(
        established_counter=count_years_from_establish(),
        products=get_wines_from_excel('products.xlsx')
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
