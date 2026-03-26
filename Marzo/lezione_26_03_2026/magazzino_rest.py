from magazzino_service import MagazzinoService

from flask import Flask, jsonify

app = Flask(__name__)

service = MagazzinoService()

@app.get('/api/prodotti')
def prodotti():
    return jsonify(service.getAllProducts())

if __name__ == '__main__':
    app.run(debug=True)