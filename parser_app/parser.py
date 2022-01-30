import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://stopgame.ru"
URL = "https://stopgame.ru/articles/new"

HEADERS = {
    'Accept': '',
    'User-Agent': ''
}