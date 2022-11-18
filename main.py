from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pprint import pprint
import collections
import datetime
import pandas


def est_counter():
    est_year = 1920
    now_year = datetime.date.today().year
    num_of_years = now_year - est_year
    if 10 < num_of_years % 100 < 20 or num_of_years % 10 in (0, 5, 6, 7, 8, 9):
        return f'{num_of_years} лет'
    elif num_of_years % 10 == 1:
        return f'{num_of_years} год'
    else:
        return f'{num_of_years} года'


def get_wines_from_excel(filename, sheet_name=0):
    excel_data_df = pandas.read_excel(
        filename,
        sheet_name=sheet_name,
        na_values=None,
        keep_default_na=False,
    )

    translate2dict = excel_data_df.to_dict(orient='record')
    wines = collections.defaultdict(list)
    for wine in translate2dict:
        category = wine['Категория']
        wines[category].append(wine)
    output = {key: value for key, value in sorted(wines.items())}
    return output


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('template.html')
rendered_page = template.render(
    established_counter=est_counter(),
    products=get_wines_from_excel('products.xlsx')
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
