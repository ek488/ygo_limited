import json, os.path, random, time, urllib
from os import path
from urllib.request import Request, urlopen

common_cardname_set = {"Book of Moon", "Compulsory Evacuation Device", "Dust Knight", "Raigeki Break", "Tackle Crusader"}

def get_ygoprodeck_json(cardname):
    req = Request("https://db.ygoprodeck.com/api/v7/cardinfo.php?name=" + cardname.replace(" ", "%20"), headers={'User-Agent': 'Mozilla/5.0'})
    return json.loads((urlopen(req).read().decode()))

def get_id(cardname):
    return get_ygoprodeck_json(cardname)["data"][0]["id"]

def get_image_url(cardname):
    return get_ygoprodeck_json(cardname)["data"][0]["card_images"][0]["image_url"]

def download_img(cardname: str):
    image_filename = cardname + ".jpg"
    if not path.exists("card_images/" + image_filename):
        image_url = get_image_url(cardname)
        urllib.request.urlretrieve(image_url, "card_images/" + image_filename)
        print("Image downloaded.")

def download_imgs(cardname_set):
    for cardname in cardname_set:
        image_filename = cardname + ".jpg"
        download_img(cardname)
        time.sleep(5)

download_imgs(common_cardname_set)
