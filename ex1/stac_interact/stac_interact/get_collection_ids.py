def get_collection_ids():
    collection_ids = []
    url = ' https://earth-search.aws.element84.com/v0/collections'
    resp = requests.get(url)
    if resp.status = 200:
        for i in resp.json():
            collection_ids.append(i['id'])
        return collection_ids
    else:
        return f'Error: {resp.status}'
