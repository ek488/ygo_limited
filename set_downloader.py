import json, os.path, random, time, urllib
from os import path
from urllib.request import Request, urlopen

def download_img(card_id, img_url):
    image_filename = str(card_id) + ".jpg"
    if not path.exists("card_images/" + image_filename):
        urllib.request.urlretrieve(img_url, "card_images/" + image_filename)
        print(str(card_id) + " image downloaded.")
        time.sleep(2)

def download_set_card_images(set_name):
    set_json = json.load(open(set_name))
    
    for card in set_json["data"]:
        download_img(card["id"], card["card_images"][0]["image_url"])

set_set = {#"legend_of_blue_eyes_white_dragon", "metal_raiders", 
"magic_ruler", "pharaohs_servant", "labyrinth_of_nightmare", "legacy_of_darkness", "pharaonic_guardian", "magicians_force", "dark_crisis", "invasion_of_chaos", "ancient_sanctuary", "soul_of_the_duelist", "rise_of_destiny", "flaming_eternity"}

download_set_card_images("set_jsons/legend_of_blue_eyes_white_dragon.json")

#download_set_card_images("set_jsons/metal_raiders.json")
