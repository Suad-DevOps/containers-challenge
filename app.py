from flask import Flask, render_template
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=int(os.environ.get('REDIS_PORT', 6379)))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/count')
def count():
    count = redis.incr('visits')
    return render_template('index.html', count=count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)