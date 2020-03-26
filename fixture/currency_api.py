import requests
import xml.etree.ElementTree as ET
from model.currency import Currency


def api(date):
    r = requests.get("http://www.cbr.ru/scripts/xml_daily.asp?date_req=%s" % date)
    root = ET.fromstring(r.text)
    list = []
    for Valute in root.findall('Valute'):
        num_code = Valute.find('NumCode').text
        char_code = Valute.find('CharCode').text
        nominal = Valute.find('Nominal').text
        name = Valute.find('Name').text
        value = Valute.find('Value').text
        list.append(Currency(numCode=num_code, charCode=char_code, nominal=nominal, name=name, value=value))
    return list

