# Luwei Wang
# lw3511

from flask import Flask
app = Flask(__name__)
import pytz
from datetime import datetime


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/time')
def get_time():
    timezone = pytz.timezone('US/Eastern')
    time_now = datetime.now(timezone)
    formatted_time = time_now.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    return formatted_time

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
