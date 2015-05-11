__author__ = 'Xin Huang'

from flask import render_template, jsonify

from app import app, db


@app.route('/')
def pie():
    return render_template('pie.html')


@app.route('/pie_data')
def pie_data():
    response = {
        'cols': [
            {'id': '', 'label': 'Topping', 'pattern': '', 'type': 'string'},
            {'id': '', 'label': 'Slices', 'pattern': '', 'type': 'number'}
        ],
        'rows': [
            {'c': [{'v': 'Mushrooms', 'f': None}, {'v': 3, 'f': None}]},
            {'c': [{'v': 'Onions', 'f': None}, {'v': 1, 'f': None}]},
            {'c': [{'v': 'Olives', 'f': None}, {'v': 1, 'f': None}]},
            {'c': [{'v': 'Zucchini', 'f': None}, {'v': 1, 'f': None}]},
            {'c': [{'v': 'Pepperoni', 'f': None}, {'v': 2, 'f': None}]}
        ]
    }

    return jsonify(response)


@app.route('/bar')
def bar():
    return render_template('bar.html')


@app.route('/bar_data')
def bar_data():
    response = {
        'cols': [
            {'id': '', 'label': 'Galaxy', 'type': 'string'},
            {'id': '', 'label': 'Distance', 'type': 'number'}
        ],
        'rows': [
            {'c': [{'v': 'Canis Major Dwarf'}, {'v': 8000}]},
            {'c': [{'v': 'Sagittarius Dwarf'}, {'v': 24000}]},
            {'c': [{'v': 'Ursa Major II Dwarf'}, {'v': 30000}]},
            {'c': [{'v': 'Lg. Magellanic Cloud'}, {'v': 50000}]},
            {'c': [{'v': 'Bootes I'}, {'v': 60000}]},
        ]
    }

    return jsonify(response)


@app.route('/col')
def col():
    return render_template('col.html')


@app.route('/col_data')
def col_data():
    response = {
        'cols': [
            {'id': '', 'label': 'Galaxy', 'type': 'string'},
            {'id': '', 'label': 'ValueA', 'type': 'number'},
            {'id': '', 'label': 'ValueB', 'type': 'number'}
        ],
        'rows': [
            {'c': [{'v': 'Canis Major Dwarf'}, {'v': 80}, {'v': 23.3}]},
            {'c': [{'v': 'Sagittarius Dwarf'}, {'v': 24}, {'v': 4.5}]},
            {'c': [{'v': 'Ursa Major II Dwarf'}, {'v': 30}, {'v': 14.3}]},
            {'c': [{'v': 'Lg. Magellanic Cloud'}, {'v': 50}, {'v': 0.9}]},
            {'c': [{'v': 'Bootes I'}, {'v': 60}, {'v': 13.1}]}
        ]
    }

    return jsonify(response)


@app.route('/scatter')
def scatter():
    return render_template('scatter.html')


@app.route('/scatter_data')
def scatter_data():
    data = {
        'cols': [
            {'id': '', 'label': 'Hour', 'type': 'number'},
            {'id': '', 'label': 'Final', 'type': 'number'}
        ],
        'rows': [
            {'c': [{'v': 0}, {'v': 23}]},
            {'c': [{'v': 0}, {'v': 45}]},
            {'c': [{'v': 0}, {'v': 76}]},
            {'c': [{'v': 1}, {'v': 80}]},
            {'c': [{'v': 2}, {'v': 90}]},
            {'c': [{'v': 3}, {'v': 100}]}
        ]
    }
    return jsonify(data)


@app.route('/google_map')
def google_map():
    return render_template('map.html')


@app.route('/google_map_data')
def google_map_data():
    data = {
        'geo': [
            [41.758425, -87.605513],
            [41.964988, -87.700031],
            [41.8781136, -87.6297982],
            [41.92972694, -87.65279869],
            [41.85216899, -87.61598398],
            [41.91867338, -87.6996311],
            [41.68474572, -87.66521486]
        ]
    }
    return jsonify(data)


@app.route('/couch')
def couch_data():
    """
    sample data for querying couchdb and return json
    :return: json
    """
    data = list(db.query("HashtagsView/Hashtags", group='true', limit=10))
    return jsonify({'data': data})