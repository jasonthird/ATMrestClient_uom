# example usage and client library for the endpoint graphql
from decimal import Decimal

import requests
import json


class Atm(object):
    def __init__(self, Endpoint):
        self.Endpoint = Endpoint

    def auth(self, username, pin):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        json_data = {
            'username': username,
            'pin': pin
        }

        response = requests.post(self.Endpoint + 'atm/auth', headers=headers, json=json_data)
        json_load = json.loads(response.text)
        return json_load['token']

    def balance(self, auth):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        json_data = {
            'token': auth
        }

        response = requests.get(self.Endpoint + 'atm/balance', headers=headers, json=json_data)
        json_load = json.loads(response.text)
        return json_load['balance']

    def withdraw(self, auth, amount):
        if Decimal(amount) <= 0:
            return 0
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        json_data = {
            'token': auth,
            'amount': str(-Decimal(amount)),
        }

        response = requests.patch('http://127.0.0.1:8000/atm/balance', headers=headers, json=json_data)
        json_data = json.loads(response.text)
        return str(json_data['withdrawn'])

    def deposit(self, auth, amount):
        if Decimal(amount) <= 0:
            return 0
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        json_data = {
            'token': auth,
            'amount': amount,
        }

        response = requests.patch('http://127.0.0.1:8000/atm/balance', headers=headers, json=json_data)
        json_data = json.loads(response.text)
        return str(json_data['deposited'])
