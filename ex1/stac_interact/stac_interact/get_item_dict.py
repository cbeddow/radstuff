def get_item_dict(collection_id):
    url = f'https://earth-search.aws.element84.com/v0/collections/{collection_id}/items'
    resp = requests.get(url)
    if resp.status == 200:
        data=resp.json()
        item = data['features'][0]
        return item
    else:
        print(f'Error: {resp.status}')
        item = 'error'
        return item
