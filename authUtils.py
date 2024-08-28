import http.client
import os
import json
from dotenv import load_dotenv

load_dotenv()


def getAccessToken():
    conn = http.client.HTTPSConnection(os.getenv("AUTH0_DOMAIN"))

    payload = ("{\"client_id\":\"" + os.getenv("AUTH0_CLIENT") +
               "\",\"client_secret\":\"" + os.getenv("AUTH0_SECRET") +
               "\",\"audience\":\"" + os.getenv("AUTH0_AUDIENCE") +
               "\",\"grant_type\":\"client_credentials\"}")

    headers = {'content-type': "application/json"}

    conn.request("POST", "/oauth/token", payload, headers)

    res = conn.getresponse()
    data = res.read()

    return json.loads(data.decode("utf-8"))
