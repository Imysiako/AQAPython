import requests
from requests.auth import HTTPBasicAuth


class CarController:
    def __init__(self, base_url="http://127.0.0.1:8080"):
        self.base_url = base_url
        self.session = requests.Session()

    def dz_auth(self):
        auth_url = f"{self.base_url}/auth"
        response = self.session.post(auth_url, auth=HTTPBasicAuth('test_user', 'test_pass'))

        if response.status_code == 200:
            data = response.json()
            access_token = data.get("access_token")
            if access_token:
                self.session.headers.update({'Authorization': f'Bearer {access_token}'})
            return data
        return response.json()

    def get_cars(self, sort_by=None, limit=None):
        cars_url = f"{self.base_url}/cars"
        params = {}
        if sort_by is not None:
            params['sort_by'] = sort_by
        if limit is not None:
            params['limit'] = limit

        response = self.session.get(cars_url, params=params)
        return response