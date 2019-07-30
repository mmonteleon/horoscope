import requests

def horoscope(sign):
    r = requests.get("http://ohmanda.com/api/horoscope/"+sign.lower(), headers={"Accept":"application/json"})
    message =r.json()['horoscope']
    return message
    