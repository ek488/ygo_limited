import json, os.path, random, time, urllib
from os import path
from urllib.request import Request, urlopen

cardname_set = {"Ballista Squad", "Black Brachios", "Book of Moon", "Breakthrough Skill", "Compulsory Evacuation Device", "Dust Knight", "Fabled Soulkius", "Giant Rat", "Kelbek", "Mecha Phantom Beast Blackfalcon", "Miracle's Wake", "Poseidon Wave", "Raigeki Break", "Tackle Crusader", "Winged Rhynos"}

def get_ygoprodeck_json(cardname):
    req = Request("https://db.ygoprodeck.com/api/v7/cardinfo.php?name=" + cardname.replace(" ", "%20"), headers={'User-Agent': 'Mozilla/5.0'})
    ygoprodeck_json = json.loads((urlopen(req).read().decode()))
    time.sleep(1)
    return ygoprodeck_json

def get_id(cardname):
    return get_ygoprodeck_json(cardname)["data"][0]["id"]

def get_image_url(cardname):
    return get_ygoprodeck_json(cardname)["data"][0]["card_images"][0]["image_url"]

def download_img(cardname: str):
    image_filename = cardname + ".jpg"
    if not path.exists("card_images/" + image_filename):
        image_url = get_image_url(cardname)
        urllib.request.urlretrieve(image_url, "card_images/" + image_filename)
        print(cardname + " image downloaded.")
        time.sleep(5)

def download_imgs(cardname_set):
    for cardname in cardname_set:
        download_img(cardname)


def download_json(cardname: str):
    json_filename = cardname + ".json"
    if not path.exists("card_jsons/" + json_filename):
        json = "https://db.ygoprodeck.com/api/v7/cardinfo.php?name=" + cardname.replace(" ", "%20")
        urllib.request.urlretrieve(json, "card_jsons/" + json_filename)
        print(cardname + "json downloaded.")
        time.sleep(1)

def download_jsons(cardname_set):
    for cardname in cardname_set:
        download_json(cardname)

download_imgs(cardname_set)

#download_jsons(cardname_set)
