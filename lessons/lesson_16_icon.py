import requests
from requests_oauthlib import OAuth1
import os


class IconSaver:
    def __init__(self):
        self._auth = OAuth1(os.getenv('kEY'), os.getenv('SECRET'))
        self._base_url = 'http://api.thenounproject.com/icon/'

    def get_icon(self, id_icon):
        self._id_icon = id_icon
        try:
            url_icon = self._get_icon_url(id_icon)
            icon_data = self._get_icon_data(url_icon)
            self.save_icon(icon_data)
        except Exception:  # TODO
            pass

    def _get_icon_url(self, id_icon):
        endpoint = self._base_url + str(id_icon)
        response = requests.get(endpoint, auth=self._auth)
        res = response.json()
        return res['icon'].get('icon_url')

    def _get_icon_data(self, url_icon):
        response_icon = requests.get(url_icon)
        return response_icon.content

    def _save_icon(self, icon_data):
        with open('icons/test.svg', 'wb') as icon_file:
            icon_file.write(icon_data)


icon_saver = IconSaver()

