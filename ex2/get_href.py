from stac_interact import get_collection_ids, get_item_dict, get_items_within

# desired collection ID
collection = 'sentinel-s2-l2a'

# get first item in desired collections

data = get_item_dict(collection)
assets = data['assets']
keys = assets.keys()
for key in keys:
    print(assets[key]['href'])
