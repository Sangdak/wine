from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
from pprint import pprint
import collections


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
    # pprint(excel_data_df)
    translate2dict = excel_data_df.to_dict(orient='record')
    pprint(translate2dict)
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

prod = get_wines_from_excel('wine2.xlsx')
pprint(prod)

rendered_page = template.render(
    established_counter=est_counter(),
    products=prod
    # products=get_wines_from_excel('wine2.xlsx'),
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
