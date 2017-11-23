import requests

import utils


def page_count(json_date):
    last_page = json_date['page']['last']
    return last_page


def json_parse(json_date):

    for i in range(int(json_date['page']['items'])):
        flat = json_date['apartments'][i]
        address = flat['location']['address']
        room = flat['rent_type'].split('_')[0]
        price = flat['price']['amount']
        link = flat['url']
        date = flat['last_time_up']
        print(address, room, price, link, date)
        arg = [address, room, price, link, date]
        utils.create_list(*arg)


def run():
    'https://ak.api.onliner.by/search/apartments?rent_type[]=1_room&rent_type[]=2_rooms&price[min]=50&price[max]=300&currency=usd&bounds[lb][lat]=53.80195173669948&bounds[lb][long]=27.231065552987502&bounds[rt][lat]=53.99482078154424&bounds[rt][long]=27.893614347831367&page=1'
    params = {
        'rent_type[]': '1_room',
        'price[min]': 50,
        'price[max]': 300,
        'currency': 'usd',
    }
    url = 'https://ak.api.onliner.by/search/apartments/'
    json_date = utils.pares(url.format('/'))
    last_page = page_count(json_date)

    for i in range(1, last_page):
        params['page'] = i
        print(params)
        print(requests.get(url, params=params).json())
        json_parse(requests.get(url, params=params).json())
    utils.csv_file_writer(utils.LIST_OF_FLATS, 'onliner.csv')