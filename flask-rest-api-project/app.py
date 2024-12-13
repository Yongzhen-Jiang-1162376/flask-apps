from flask import Flask, request
from flask_smorest import abort
from custom_reponse import success, error, notfound
from db import stores, items
import uuid


app = Flask(__name__)

# stores = [{'name': 'My Store', 'items': [{'name': 'my item', 'price': 15.99}]}]

@app.get('/store')
def get_stores():
    return success(list(stores.values())), 200


@app.post('/store')
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores.update({
        store_id: store
    })

    return success(store)


@app.post('/item')
def create_item():
    item_data = request.get_json()

    if item_data['stored_id'] not in stores:
        return notfound('Store not found')
    
    item_id = uuid.uuid4().hex
    item = {**item_data, 'id': item_id}
    items[item_id] = item

    return success(item)


@app.get('/item')
def get_all_items():
    return success(list(items.values()))


@app.get('/store/<string:store_id>')
def get_store(store_id):
    try:
        return success(stores[store_id])
    except KeyError:
        abort(404, message='Store not found')


@app.get('/store/<string:item_id>')
def get_item(item_id):
    try:
        return success(items[item_id])
    except KeyError:
        abort(404, message='Item not found')

