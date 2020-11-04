class get_item_dict:
    def __init__(self):
        ''' Constructor for this class. '''

def get_item_dict(collection_id):
    url = f'https://earth-search.aws.element84.com/v0/collections/{collection_id}/items'
    resp = requests.get(url)
    if resp.status == 200:
        data=resp.json()
        item = data['features'][0]
        return item
    else:
        return f'Error: {resp.status}'
