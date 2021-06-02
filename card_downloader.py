import json, os.path, random, time, urllib
from os import path
from urllib.request import Request, urlopen

#custom_cardname_set = {"Ballista Squad", "Black Brachios", "Book of Moon", "Breakthrough Skill", "Compulsory Evacuation Device", "Dust Knight", "Fabled Soulkius", "Giant Rat", "Kelbek", "Mecha Phantom Beast Blackfalcon", "Miracle's Wake", "Poseidon Wave", "Raigeki Break", "Tackle Crusader", "Upstart Goblin", "Winged Rhynos"}

custom_cardname_set = {"Ballista Squad", "Book of Lunar Eclipse", "Book of Moon", "Breakthrough Skill"}

def get_ygoprodeck_json(cardname):
    req = Request("https://db.ygoprodeck.com/api/v7/cardinfo.php?name=" + cardname.replace(" ", "%20"), headers={'User-Agent': 'Mozilla/5.0'})
    ygoprodeck_json = json.loads((urlopen(req).read().decode()))
    time.sleep(0.2)
    return ygoprodeck_json

def get_id(cardname):
    return get_ygoprodeck_json(cardname)["data"][0]["id"]

def get_id_from_json(json):
    return json["data"][0]["id"]

def get_image_url(cardname):
    return get_ygoprodeck_json(cardname)["data"][0]["card_images"][0]["image_url"]

def get_image_url_from_json(json):
    return json["data"][0]["card_images"][0]["image_url"]

def download_img(cardname):
    ygoprodeck_json = get_ygoprodeck_json(cardname)
    card_id = get_id_from_json(ygoprodeck_json)
    image_filename = str(card_id) + ".jpg"
    if not path.exists("public/images/card_images/" + image_filename):
        image_url = get_image_url_from_json(ygoprodeck_json)
        urllib.request.urlretrieve(image_url, "public/images/card_images/" + image_filename)
        print(cardname + "(" + str(card_id) + ") image downloaded.")
        time.sleep(5)

def download_img_from_id(card_id):
    image_filename = str(card_id) + ".jpg"
    if not path.exists("public/images/card_images/" + image_filename):
        image_url = get_image_url_from_json(ygoprodeck_json)
        urllib.request.urlretrieve(image_url, "public/images/card_images/" + image_filename)
        print(cardname + " (" + str(card_id) + ") image downloaded.")
        time.sleep(2)

def download_imgs(cardname_set):
    for cardname in cardname_set:
        download_img(cardname)

#def download_json(cardname: str):
    #json_filename = cardname + ".json"
    #if not path.exists("card_jsons/" + json_filename):
        #json = "https://db.ygoprodeck.com/api/v7/cardinfo.php?name=" + cardname.replace(" ", "%20")
        #urllib.request.urlretrieve(json, "card_jsons/" + json_filename)
        #print(cardname + "json downloaded.")
        #time.sleep(1)

#def download_jsons(cardname_set):
    #for cardname in cardname_set:
        #download_json(cardname)

download_imgs(custom_cardname_set)
