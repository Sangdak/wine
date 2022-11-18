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
    pprint('ED', excel_data_df)
    translate2dict = excel_data_df.to_dict(orient='record')
    pprint('T2D', translate2dict)
    wines = collections.defaultdict(list)
    # for wine in translate2dict:
    #     category = wine['Категория']
    #     wine[category].append(wine)
    output = {key: value for key, value in sorted(wines.items())}
    return output


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

# excel_reader = pandas.read_excel(
#     'wine2.xlsx',
#     sheet_name=0,
#     usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка'],
#     na_values=None,
#     keep_default_na=False,
# )
#
# wines2dict = excel_reader.to_dict(orient='records')
# output = {}
# for item in wines2dict:
#     category = item['Категория']
#     if category not in output.keys():
#         output[category] = [{
#             'Картинка': item['Картинка'],
#             'Категория': item['Категория'],
#             'Название': item['Название'],
#             'Сорт': item['Сорт'],
#             'Цена': item['Цена'],
#         }]
#     else:
#         output[category].append(
#             {
#                 'Картинка': item['Картинка'],
#                 'Категория': item['Категория'],
#                 'Название': item['Название'],
#                 'Сорт': item['Сорт'],
#                 'Цена': item['Цена'],
#             }
#         )
#
# pprint(output)

# pprint(wines2dict)

wines = get_wines_from_excel('wine2.xlsx')
pprint(wines)

rendered_page = template.render(
    established_counter=est_counter(),
    products=get_wines_from_excel('wine2.xlsx'),
    # wines=wines2dict,
    # wines=[
    #     {
    #         'wine_title': 'Изабелла',
    #         'wine_sort': 'Изабелла',
    #         'wine_price': 350,
    #         'wine_img': 'images/izabella.png',
    #     },
    #     {
    #         'wine_title': 'Гранатовый браслет',
    #         'wine_sort': 'Мускат розовый',
    #         'wine_price': 350,
    #         'wine_img': 'images/granatovyi_braslet.png',
    #     },
    #     {
    #         'wine_title': 'Шардоне',
    #         'wine_sort': 'Шардоне',
    #         'wine_price': 350,
    #         'wine_img': 'images/shardone.png',
    #     },
    #     {
    #         'wine_title': 'Белая леди',
    #         'wine_sort': 'Дамский пальчик',
    #         'wine_price': 399,
    #         'wine_img': 'images/belaya_ledi.png',
    #     },
    #     {
    #         'wine_title': 'Ркацители',
    #         'wine_sort': 'Ркацители',
    #         'wine_price': 499,
    #         'wine_img': 'images/rkaciteli.png',
    #     },
    #     {
    #         'wine_title': 'Хванчкара',
    #         'wine_sort': 'Александраули',
    #         'wine_price': 550,
    #         'wine_img': 'images/hvanchkara.png',
    #     },
    # ]
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
