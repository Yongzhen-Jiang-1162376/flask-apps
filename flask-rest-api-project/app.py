from flask import Flask, request

app = Flask(__name__)

stores = [{'name': 'My Store', 'items': [{'name': 'my item', 'price': 15.99}]}]

def success(data):
    return {'data': data}

def error(message, code):
    return {'error': {'code': code, 'message': message}}



@app.get('/store')
def get_store():
    return success(stores), 200


@app.post('/store')
def create_store():
    request_data = request.get_json()

    filtered_stored = [s for s in stores if s['name'] == request_data['name']]

    if len(filtered_stored) > 0:
        return error('Store already exists', 409), 409

    new_store = {'name': request_data['name'], 'items': request_data['items']}

    stores.append(new_store)
    
    return success(new_store), 200


@app.post('/store/<string:name>/item')
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {'name': request_data['name'], 'price': request_data['price']}
            store['items'].append(new_item)

            print(stores)

            return success(new_item), 200
    
    return error('Store not found', 404), 404
