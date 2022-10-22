import requests
from django.conf import settings

from src.apps.common.managers.common import BaseManager


def get_ngrok_url() -> str:
    ngrok_tunnels = settings.NGROK_API
    response = requests.get(ngrok_tunnels).json()
    tunnels = response["tunnels"]
    return tunnels[0]["public_url"] if "https://" in tunnels[0]["public_url"] else tunnels[1]["public_url"]


class ItemManager(BaseManager):
    def get_item_photo(self, pk):
        obj = self.filter(
            id=pk,
        ).first()
        ngrok_url = get_ngrok_url()
        photo = f"""{ngrok_url}{settings.MEDIA_URL}{obj.image}"""
        return obj, photo

    def get_item_by_pk(self, pk, status):
        pk_list = list(
            self.filter(
                status=status,
            ).values_list(
                "id",
                flat=True,
            ).all()
        )
        obj = self.filter(
            id=pk_list[pk - 1],
        ).first()
        return obj

    def get_next_item(self, pk):
        obj = self.filter(
            id__gt=pk,
        ).first()
        return obj

    def get_first_item(self):
        obj = self.first()
        ngrok_url = get_ngrok_url()
        photo = f"""{ngrok_url}{settings.MEDIA_URL}{obj.image}"""
        return obj, photo

    def get_first_item_by_status(self, status):
        obj = self.filter(
            status=status,
        ).first()
        ngrok_url = get_ngrok_url()
        photo = f"""{ngrok_url}{settings.MEDIA_URL}{obj.image}"""
        return obj, photo
