# compose_flask/app.py
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    counter  = redis.get('hits').decode('utf-8')
    return f"This Compose/Flask demo has been viewed {counter} time(s)."


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
