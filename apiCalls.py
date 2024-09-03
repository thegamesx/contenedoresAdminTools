import os
from authUtils import getAccessToken
from dotenv import load_dotenv
import requests

load_dotenv()


def requestNewCont(name, config, password):
    accessToken = getAccessToken()

    headers = {"Authorization": f'Bearer {accessToken["access_token"]}'}

    response = requests.post(os.getenv("SERVER_URL") +
                             "/cont/create/?password=" + password +
                             "&name=" + name +
                             "&config_name=" + config,
                             headers=headers)

    return response

