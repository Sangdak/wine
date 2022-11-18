# New Russian Wine

This repository is a website design project of the company-producer of wines.

## How to install 
To start the project, you should download the repository to your device. 
- Python3 and pip should already be installed.
- Add the file `products.xlsx` with products info next to 'main.py'. Approximate file content:

| Категория     | Название           | Сорт            | Цена       | Картинка             | Акция                |
| ------------- |:------------------:|:---------------:|:----------:|:--------------------:|:--------------------:|
| Белые вина    | Белая леди         | Дамский пальчик |399         | belaya_ledi.png      | Выгодное предложение |

- Use pip (or pip3, there is a conflict with Python2) to install dependencies from a file in the repository: shell pip install -r
requirements.txt

## How to run

- Open project directory from cmd and execute:
```
$ python3 main.py
```

In browser open 'http://127.0.0.1:8000/'


## Project purposes

The code is written for educational purposes - a tutorial on Python and web development on the site [Devman](https://dvmn.org).
