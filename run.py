from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time', methods=['GET'])
def get_current_time():
    # Get the current time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({'current_time': current_time})

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
