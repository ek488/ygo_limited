import json, os.path, random, time, urllib
from os import path
from urllib.request import Request, urlopen

def download_img(card_id, img_url):
    image_filename = str(card_id) + ".jpg"
    if not path.exists("public/images/card_images/" + image_filename):
        urllib.request.urlretrieve(img_url, "public/images/card_images/" + image_filename)
        print(str(card_id) + " image downloaded.")
        time.sleep(2)

def download_set_card_images(set_name):
    set_json = json.load(open(set_name))
    
    for card in set_json["data"]:
        download_img(card["id"], card["card_images"][0]["image_url"])

set_set = {"legend_of_blue_eyes_white_dragon", "metal_raiders", "magic_ruler", "pharaohs_servant", "labyrinth_of_nightmare", "legacy_of_darkness", "pharaonic_guardian", "magicians_force", "dark_crisis", "invasion_of_chaos", "ancient_sanctuary", "soul_of_the_duelist", "rise_of_destiny", "flaming_eternity", "the_lost_millennium", "cybernetic_revolution", "elemental_energy", "shadow_of_infinity", "enemy_of_justice", "power_of_the_duelist", "cyberdark_impact", "strike_of_neos", "force_of_the_breaker", "tactical_evolution", "gladiators_assault", "phantom_darkness", "light_of_destruction", "the_duelist_genesis", "crossroads_of_chaos", "crimson_crisis", "raging_battle", "ancient_prophecy", "stardust_overdrive", "absolute_powerforce", "the_shining_darkness", "duelist_revolution", "starstrike_blast", "storm_of_ragnarok", "extreme_victory", "generation_force", "photon_shockwave", "order_of_chaos", "galactic_overlord", "return_of_the_duelist", "abyss_rising", "cosmo_blazer", "lord_of_the_tachyon_galaxy", "judgment_of_the_light", "shadow_specters", "legacy_of_the_valiant", "primal_origin", "duelist_alliance", "the_new_challengers", "secrets_of_eternity", "crossed_souls", "clash_of_rebellions", "dimension_of_chaos", "breakers_of_shadow", "shining_victories", "the_dark_illusion", "invasion_vengeance", "raging_tempest", "maximum_crisis", "code_of_the_duelist", "circuit_break", "extreme_force", "flames_of_destruction", "cybernetic_horizon", "soul_fusion", "savage_strike", "dark_neostorm", "rising_rampage", "chaos_impact", "ignition_assault", "eternity_code", "rise_of_the_duelist", "phantom_rage", "blazing_vortex", "lightning_overdrive"}

for set in set_set:
    download_set_card_images("set_jsons/" + set + ".json")
