import requests


def get_pic_url_st():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    pic_url = response.json()['message']
    return pic_url


def get_pic_url_nd():
    response = requests.get('https://random.dog/woof.json')
    pic_url = response.json()['url']
    return pic_url
