import json
from urllib.request import urlopen


def get_country(ip_address):
    """
    Запрос к сервису на получение данных об ip
    """
    response = urlopen("http://freegeoip.net/json/" + ip_address).read().decode('utf-8')
    response_json = json.loads(response)

    return response_json.get("country_code")

for i in range(1, 120):
    "Просмотр какой стране пренадлежит данный адрес"
    print(get_country(str(i) + ".78.253.59"))
