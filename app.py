from flask import Flask
from flask import render_template
from flask import request

import json

app = Flask(__name__)
app.config['TESTING'] = True
app.config['FLASK_DEBUG'] = True

app.testing = True


@app.route('/')
def index():
    with open('all_resources.json') as f:
        data = json.load(f)
    greeting="To export"
    return render_template('index.html',dict=dict, isinstance=isinstance, items=data['data']['items'], greet=greeting)

@app.route('/load_filtered_header', methods=['POST'])
def load_filtered_header():
    headers = request.form.getlist('headers[]')
    print('-- headers',headers)
    with open('all_resources.json') as f:
        data = json.load(f)
    greeting="Data Loaded !"
    items = data['data']['items']
    new_items = []
    for header in headers:
        print('-- header : ',header)
        for item in items:
            print('-- item : ',item)
            new_items.append(item)
            # del item[header]        
    return render_template('loaded.html',headers=headers, dict=dict, isinstance=isinstance, items=new_items, greet=greeting)

