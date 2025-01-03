import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from custom_reponse import success, error, notfound
from schemas import StoreSchema


blp = Blueprint('stores', __name__, description='Operations on stores')

@blp.route('/store/<string:store_id>')
class Store(MethodView):
    @blp.response(200, StoreSchema)
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
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return success({'stores': list(stores.values())})
    
    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(cls, store_data):
        for store in stores.values():
            if store_data['name'] == store['name']:
                abort(400, message=f'Store already exists.')
        
        store_id = uuid.uuid4().hex
        store = {**store_data, 'id': store_id}
        stores.update({store_id: store})
        
        return success(store)