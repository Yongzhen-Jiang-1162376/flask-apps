import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from custom_reponse import success, error, notfound


blp = Blueprint('stores', __name__, description='Operations on stores')

@blp.route('/store/<string:store_id>')
class Store(MethodView):
    def get(self, store_id):
        try:
            return success(stores[store_id])
        except KeyError:
            abort(404, message='Store not found')
    
    def delete(self, store_id):
        try:
            del stores[store_id]
            return success(message='Store deleted')
        except KeyError:
            abort(404, message='Store not found')

@blp.route('/store')
class StoreList(MethodView):
    def get(self):
        return success({'stores': list(stores.values())})
    
    def post(self):
        store_date = request.get_json()
        if 'name' not in store_date:
            abort(
                400,
                message="Bad request. Ensure 'name' is included in the JSON payload"
            )
        for store in stores.values():
            if store_date['name'] == store['name']:
                abort(400, message=f'Store already exists.')
        
        store_id = uuid.uuid4().hex
        store = {**store_date, 'id': store_id}
        stores.update({store_id: store})
        
        return success(store)