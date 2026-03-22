
from flask import Flask, render_template, jsonify
import psycopg2
import redis
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB", "devopsdb")
DB_USER = os.getenv("POSTGRES_USER", "devops")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "devops")

REDIS_HOST = os.getenv("REDIS_HOST", "redis")

def check_postgres():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        conn.close()
        return True
    except:
        return False

def check_redis():
    try:
        r = redis.Redis(host=REDIS_HOST, port=6379)
        r.ping()
        return True
    except:
        return False

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/status")
def status():
    return jsonify({
        "postgres": check_postgres(),
        "redis": check_redis()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
