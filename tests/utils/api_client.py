import requests


class Client:
    def __init__(self):
        self._base_url = 'http://localhost:8080/v2{}'

    def post(self, uri, *args, **kwargs):
        return requests.post(self._base_url.format(uri), *args, **kwargs)

    def get(self, uri, *args, **kwargs):
        return requests.get(self._base_url.format(uri), *args, **kwargs)

    def put(self, uri, *args, **kwargs):
        return requests.put(self._base_url.format(uri), *args, **kwargs)

    def delete(self, uri, *args, **kwargs):
        return requests.delete(self._base_url.format(uri), *args, **kwargs)

    def add_pet(self, data):
        return self.post('/pet', json=data)


