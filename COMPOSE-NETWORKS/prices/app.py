import json, requests
from flask import Flask, jsonify

app = Flask(_name_)

@app.route('/')
def prices():
    data = requests.get('http://bomasi').json()

    for i in range(len(data)):
        dat[i]['price'] = i*5 + 1

    return jsonify(data)

If _name_ == '_main_':
    app.run(host='0.0.0.0', port=80)





