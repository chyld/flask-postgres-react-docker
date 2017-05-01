from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({
		'hello': 'space'
	})

@app.route('/nested')
def nested():
	return jsonify({"a": 3,
					"b": True, 
					"c": None, 
					"d": "hello json",
					"e": 3.14,
					"f": [1,2,3],
					"g": {"x":1, "y":2, "z":3}
					})

@app.route('/echo', methods=['POST'])
def echo():
	# import IPython
	# from IPython import embed
	# embed() # this call anywhere in your program will start IPython
	# import pdb; pdb.set_trace()
	# IPython.start_ipython()
	return jsonify(request.json)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ['PORT']))
