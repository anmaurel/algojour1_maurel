from flask import Flask
from flask_cors import CORS, cross_origin
from blockchain import Blockchain
import json

bchain = Blockchain()

"""
API Flask
"""
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def get_all_blocks():
    return json.dumps(bchain.get_blocks(), sort_keys = True, default = str, indent = 2)

# @app.route('/add', methods=['POST'])
# def add_block():
#     data = request.form.get('data')
#     block = bchain.new_block(data)
#     bchain.add_block(block)
#     return json.dumps(bchain.get_blocks(), sort_keys = True, default = str, indent = 2)

app.run(debug = True, port = 4000)