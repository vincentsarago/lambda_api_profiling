"""app: handle requests."""

import json
from lambda_proxy.proxy import API


handler = API(name="app")


@handler.get("/ping", cors=True)
def main():
    return ("OK", "application/json", json.dumps({"ping": "pong!"}))
