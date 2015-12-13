import requests


def get_restaurants(latitude, longitude, cuisine, establishment_type):

    url = 'https://developers.zomato.com/api/v2.1/search'

    # Parameters are basically data sent with the URL
    params = {'lat': latitude,
              'lon': longitude,
              'sort': 'rating',
              'order': 'desc',
              'cuisines': cuisine,
              'establishment_type': establishment_type,
              'radius': 2000.0,
              'count': 100}

    header = {
        'User-Agent': 'curl/7.30.0',
        'Accept': 'application/json',
        'user_key': '<Zomato API KEY>',
    }
    # The requests package will generate a request with the required data
    # The URL looks like :
    # https://developers.zomato.com/api/v2.1/search?lat=2.4937483&lon=2.43234323&sort=rating...
    r = requests.get(
        url=url, headers=header, params=params)

    restaurants = r.json()
    # This puts the best_rated_restaurants in a list. Refer to JSON Response.
    restaurants_list = {'restaurants': restaurants['restaurants']}
    return restaurants_list
