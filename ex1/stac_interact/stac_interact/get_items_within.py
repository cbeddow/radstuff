class get_items_within:
    def __init__(self):
        ''' Constructor for this class. '''

def count_items_within(collection_id, geom):
    url = 'https://earth-search.aws.element84.com/v0/search'
    headers = {
        'collections' : collection_id,
        'intersects' : geom,
        'limit' : '1000'
    }
    resp = requests.post(url, headers = headers)
    if resp.status == 200:
        count = len(resp.json()['features'])
        return count
    else:
        return f'Error: {resp.status}'
