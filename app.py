from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=int(os.environ.get('REDIS_PORT', 6379)))

@app.route('/')
def home():
    return 'Hello!'

@app.route('/count')
def count():
    count = redis.incr('visits')
    return f'Visit count: {count}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)