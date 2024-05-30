import requests
s = requests.Session()


def get_sites(lat, long, radius, limit=100):

    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "format": "json",
        "list": "geosearch",
        "gscoord": f"{lat}|{long}",
        "gslimit": f"{limit}",
        "gsradius": f"{radius}",
        "action": "query"
    }
    r = s.get(url=url, params=params)
    pages = r.json()['query']['geosearch']
    sites = [i['title'] for i in pages]
    return sites


def test_step1(coord1, text1):
    assert text1 in get_sites(coord1[0], coord1[1], 100), "Not found"