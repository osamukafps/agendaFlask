from flask import Flask, request, jsonify
from flask_cors import CORS
import db

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/api/contatos', methods=['GET'])
def api_get_contatos():
    return jsonify(db.get_contatos())


@app.route('/api/contatos/<id>', methods=['GET'])
def api_get_contato_by_id(id):
    return jsonify(db.get_contato_by_id(id))


@app.route('/api/contatos/<filter>', methods=['GET'])
def api_get_contato_by_filter(filter):
    return jsonify(db.get_contato_by_filter(filter))


@app.route('/api/contatos/create', methods=['POST'])
def api_create_contato():
    contato = request.get_json()
    return jsonify(db.criar_contato(contato))


@app.route('/api/contatos/update', methods=['PUT'])
def api_update_contato():
    contato = request.get_json()
    return jsonify(db.update_contato(contato))


@app.route('/api/contatos/delete/<id>', methods=['DELETE'])
def api_delete_contato(id):
    return jsonify(db.delete_contato(id))


if __name__ == "__main__":
    # app.debug = True
    # app.Run(debug=True)
    app.run()
