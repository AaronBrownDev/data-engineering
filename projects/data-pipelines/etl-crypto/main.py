import requests

fng_url = "https://api.alternative.me/fng/"
fng_params = {
    "limit" : 0,
    "format" : "json",

}

def get_data(url, params):
    r = requests.get(url, params=params)
    if r.status_code != 200:
        raise ConnectionError(f"Error: {r.status_code} - {r.text}")
    else:
        return r.json()

def handle_data(data):
    # print(type(data), data)

    print(data["name"])
    # print(data["data"])
    # print(data["metadata"])

fng_data = get_data(fng_url, fng_params)

handle_data(fng_data)