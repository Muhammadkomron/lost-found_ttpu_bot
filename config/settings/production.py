import requests
from django.conf import settings

from .base import *  # noqa


def get_ngrok_url():
    ngrok_tunnels = settings.NGROK_API
    response = requests.get(ngrok_tunnels).json()
    tunnels = response["tunnels"]
    tunnel = tunnels[0]["public_url"] if "https://" in tunnels[0]["public_url"] else tunnels[1]["public_url"]
    return tunnel.strip("https://")


SERVER_IP = os.environ["SERVER_IP"]
SERVER_DOMAIN = get_ngrok_url()

DEBUG = os.environ["DEBUG"]

ALLOWED_HOSTS = [SERVER_IP, SERVER_DOMAIN]
print(ALLOWED_HOSTS)
