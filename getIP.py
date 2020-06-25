import requests

IPv4 = requests.get('https://api.ipify.org/?format=json')
IPv6 = requests.get('https://api6.ipify.org?format=json')
