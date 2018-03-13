import requests
import json
from django.http import Http404


class VerifyPhone(object):
    # using free NEXMO.COM verification

    headers = {'content-type': 'application/x-www-form-urlencoded'}
    data = {
        'api_key': '0928046d',
        'api_secret': '4c9d7a6a59228fad',
        'brand': 'ps4you.com'
    }

    def send_code(self, phone):
        url = 'https://api.nexmo.com/verify/json'
        r = requests.post(url=url, data=self.data.update({'phone': phone}), headers=self.headers)
        responce = r.json()
        print(responce)
        if responce.get('status') == '0':
            return responce.get('request_id')
        return False

    def verify_code(self, request_id, code):
        url = 'https://api.nexmo.com/verify/check/json'
        r = requests.post(url=url, data=json.dumps(self.data.update({'request_id': request_id, 'code': code})))
        print(r.json())

