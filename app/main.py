import os
import socket

import redis
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# All configuration comes from the environment, never from code
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = int(os.environ.get("REDIS_PORT", "6379"))
APP_ENV = os.environ.get("APP_ENV", "development")

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
app = FastAPI(title="SWE40006 Task 4.3")


@app.get("/", response_class=HTMLResponse)
def index():
    visits = r.incr("visits")
    return f"""
    <h1>SWE40006 — Task 4.3</h1>
    <p>Environment: <b>{APP_ENV}</b></p>
    <p>Served by container: <code>{socket.gethostname()}</code></p>
    <p>Redis host: <code>{REDIS_HOST}</code></p>
    <p>Total visits (stored in Redis): <b>{visits}</b></p>
    """


@app.get("/health")
def health():
    try:
        r.ping()
        return {"status": "ok", "redis": "up"}
    except redis.RedisError:
        return {"status": "degraded", "redis": "down"}
