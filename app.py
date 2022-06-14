from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)


# @app.route('/index')
# def index():
# return jsonify({"mensaje": 'Hola Mundo'})


@app.route('/products')
def getProducts():
    return jsonify({"productos": products, "mensaje": "Linea de productos"})


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"Product": productsFound[0]})
    else:
        return jsonify({"mensaje": "El producto solicitado no existe."})


@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"mensaje": "Producto agregado correctamente.", "products": products})


@app.route('/products/<string:product_name>', methods=['PUT'])
def updateProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "mensaje": "Producto actualizado.", "product": productsFound[0]
        })
    else:
        return jsonify({"mensaje": "Producto no encontrado."})


@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        products.remove(productsFound[0])
        return jsonify({"mensaje": "Producto eliminado.", "products": products})
    else:
        return jsonify({"mensaje": "Producto no encontrado."})


if __name__ == '__main__':
    app.run(debug=True, port=2000)
