import json, os.path, random, time, urllib
from os import path
from urllib.request import Request, urlopen

#custom_cardname_set = {"Ballista Squad", "Black Brachios", "Book of Moon", "Breakthrough Skill", "Compulsory Evacuation Device", "Dust Knight", "Fabled Soulkius", "Giant Rat", "Kelbek", "Mecha Phantom Beast Blackfalcon", "Miracle's Wake", "Poseidon Wave", "Raigeki Break", "Tackle Crusader", "Upstart Goblin", "Winged Rhynos"}

custom_cardname_set = {"Book of Moon"}

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
    if not path.exists("card_images/" + image_filename):
        image_url = get_image_url_from_json(ygoprodeck_json)
        urllib.request.urlretrieve(image_url, "card_images/" + image_filename)
        print(cardname + " image downloaded.")
        time.sleep(5)

def download_img_from_id(card_id):
    image_filename = str(card_id) + ".jpg"
    if not path.exists("card_images/" + image_filename):
        image_url = get_image_url_from_json(ygoprodeck_json)
        urllib.request.urlretrieve(image_url, "card_images/" + image_filename)
        print(cardname + " image downloaded.")
        time.sleep(2)

#def download_imgs(cardname_set):
    #for cardname in cardname_set:
        #download_img(cardname)

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

def download_set_card_images(set_name):
    set_json = json.load(open(set_name))
    
    for card in set_json["data"]:
        download_img_from_id(card["id"])

download_set_card_images("set_jsons/legend_of_blue_eyes_white_dragon.json")

#download_set_card_images("set_jsons/metal_raiders.json")

set_list = {"legend_of_blue_eyes_white_dragon", "metal_raiders", "magic_ruler", "pharaohs_servant", "labyrinth_of_nightmare", "legacy_of_darkness", "pharaonic_guardian", "magicians_force", "dark_crisis", "invasion_of_chaos", "ancient_sanctuary", "soul_of_the_duelist", "rise_of_destiny", "flaming_eternity"}

#download_imgs(custom_cardname_set)
