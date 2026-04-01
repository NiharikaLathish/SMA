from flask import Flask, request, jsonify

app = Flask(__name__)

data_store = []

@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.json
    data_store.append(data)
    return jsonify({"message": "Data stored successfully"})

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(data_store)

if __name__ == '__main__':
    app.run(debug=True)