from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

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

print(est_counter())

rendered_page = template.render(
    established_counter=est_counter(),
    wine1_title='Изабелла',
    wine1_sort='Изабелла',
    wine1_price=350,
    wine1_img='images/izabella.png',
    wine2_title='Гранатовый браслет',
    wine2_sort='Мускат розовый',
    wine2_price=350,
    wine2_img='images/granatovyi_braslet.png',
    wine3_title='Шардоне',
    wine3_sort='Шардоне',
    wine3_price=350,
    wine3_img='images/shardone.png',
    wine4_title='Белая леди',
    wine4_sort='Дамский пальчик',
    wine4_price=399,
    wine4_img='images/belaya_ledi.png',
    wine5_title='Ркацители',
    wine5_sort='Ркацители',
    wine5_price=499,
    wine5_img='images/rkaciteli.png',
    wine6_title='Хванчкара',
    wine6_sort='Александраули',
    wine6_price=550,
    wine6_img='images/hvanchkara.png',
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
