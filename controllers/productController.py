from flask import request, jsonify
from models.schemas.productSchema import product_schema, products_schema
from services import productService
from marshmallow import ValidationError
from utils.util import role_required

@role_required('admin')
def save():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    product_save = productService.save(product_data)
    return product_schema.jsonify(product_save), 201

def getAll():
    try:
        products = productService.getAll()
        return products_schema.jsonify(products), 201
    except ValidationError as err:
        return jsonify(err.messages), 400    
    
def find_all_pagination():
    page = request.args.get('page', 1 ,type=int)
    per_page = request.args.get('per_page', 10 ,type=int)
    return products_schema.jsonify(productService.find_all_pagination(page=page, per_page=per_page)), 200