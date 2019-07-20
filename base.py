import requests


def get_pic_url_st():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    pic_url = response.json()['message']
    return pic_url


def get_pic_url_nd():
    response = requests.get('https://random.dog/woof?include=jpg,jpeg,png')
    pic = response.text
    pic_url = 'https://random.dog/' + pic
    return pic_url


def get_video_url():
    response = requests.get('https://random.dog/woof?include=mp4,webm,gif')
    video = response.text
    url = 'https://random.dog/' + video
    return url
