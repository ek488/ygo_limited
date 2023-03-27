import json, os.path, random, time, urllib
import os
#from os import path
from urllib.request import Request, urlopen

#custom_cardname_set = {"Ballista Squad", "Black Brachios", "Book of Moon", "Breakthrough Skill", "Compulsory Evacuation Device", "Dust Knight", "Fabled Soulkius", "Giant Rat", "Kelbek", "Mecha Phantom Beast Blackfalcon", "Miracle's Wake", "Poseidon Wave", "Raigeki Break", "Tackle Crusader", "Upstart Goblin", "Winged Rhynos"}

error_name_cards = set()

def get_ygoprodeck_json(cardname):
    req = Request("https://db.ygoprodeck.com/api/v7/cardinfo.php?name=" + cardname.replace(" ", "%20"), headers={'User-Agent': 'Mozilla/5.0'})
    ygoprodeck_json = json.loads((urlopen(req).read().decode()))
    time.sleep(0.2)
    return ygoprodeck_json

def get_id(cardname):
    return get_ygoprodeck_json(cardname)["data"][0]["id"]

# For example, "A" Cell Breeding Device is at position 0 in cardinfo.json.
def get_id_from_json(json, position = 0):
    return json["data"][position]["id"]

def get_name_from_json(json, position = 0):
    return json["data"][position]["name"]

def get_type_from_json(json, position = 0):
    return json["data"][position]["type"]

def get_image_url(cardname):
    return get_ygoprodeck_json(cardname)["data"][0]["card_images"][0]["image_url"]

def get_image_url_from_json(json, position = 0):
    print(json["data"][position]["card_images"][0]["image_url"]) #debug
    return json["data"][position]["card_images"][0]["image_url"]

def download_img(cardname):
    ygoprodeck_json = get_ygoprodeck_json(cardname)
    card_id = get_id_from_json(ygoprodeck_json)
    image_filename = str(card_id) + ".jpg"
    if not os.path.exists("public/images/card_images/" + image_filename):
        image_url = get_image_url_from_json(ygoprodeck_json)
        urllib.request.urlretrieve(image_url, "public/images/card_images/" + image_filename)
        print(cardname + "(" + str(card_id) + ") image downloaded.")
        time.sleep(5)

def download_img_from_id(card_id):
    image_filename = str(card_id) + ".jpg"
    if not os.path.exists("public/images/card_images/" + image_filename):
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


def create_custom_set_code(set, rarity, number):
    if len(set) > 4:
        return set[0:4] + "-" + rarity[0] + str(number)
    else:
        return set + "-" + rarity[0] + str(number)

# also downloads images
def write_custom_set_rarity(custom_set_name, filename_rarity):
    rarity = filename_rarity[0:2] # If "01co", then "co"
    if rarity == "Co":
        rarity = "01co"
    if rarity == "Ra":
        rarity = "02ra"
    if rarity == "Su":
        rarity = "03su"
    if rarity == "Ul":
        rarity = "04ul"
    if rarity == "Se":
        rarity = "05se"
    custom_set = set()
    g = open("public/custom_packs_texts/" + custom_set_name.replace(" ", "_").lower() + "/" + rarity + ".txt", "r", encoding="utf-8")
    for line in g:
        custom_set.add(line.replace('\n', '')) # Add each line, with the '\n' character at the end removed.

    set_number = 0
    f = open('cardinfo.json')

    ygoprodeck_json = json.load(f)

    ygoprodeck_json_data = ygoprodeck_json["data"]

    def get_card_position(card):
        counter = 0
        for card_info in ygoprodeck_json_data:                
            if card_info["name"] == card or card_info["name"].encode().decode() == card: # encode for Live★Twins, etc.
                return counter

            counter += 1

    first_datum = []

    for custom_set_card in custom_set:
        card_attributes = {}
        pos = get_card_position(custom_set_card)
        print(custom_set_card)
        try:
            id = get_id_from_json(ygoprodeck_json, pos)
            card_attributes.update({"id": id})
            card_attributes.update({"name": get_name_from_json(ygoprodeck_json, pos)})
            card_attributes.update({"type": get_type_from_json(ygoprodeck_json, pos)})
            
            # Downloads the image from the id
            image_filename = str(id) + ".jpg"
            if not os.path.exists("public/images/custom_card_images/" + image_filename):
                image_url = get_image_url_from_json(ygoprodeck_json, pos)
                time.sleep(2)
                #urllib.request.urlretrieve(image_url, "public/images/custom_card_images/" + image_filename)
                
                headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}

                request_= urllib.request.Request(image_url,None,headers) #The assembled request
                response = urllib.request.urlopen(request_)# store the response
                #create a new file and write the image
                f = open('public/images/custom_card_images/' + image_filename,'wb')
                f.write(response.read())
                f.close()

                print(get_name_from_json(ygoprodeck_json, pos) + "(" + str(id) + ") image downloaded.")
                time.sleep(2)


            first_custom_card_set = {}
            first_custom_card_set.update({"set_name": custom_set_name})
            first_custom_card_set.update({"set_code": create_custom_set_code(custom_set_name, rarity, set_number)})
            set_number += 1

            first_custom_card_set.update({"set_rarity": rarity})

            card_attributes.update({"card_sets": [first_custom_card_set]})

            first_datum.append(card_attributes)
        except:
            error_name_cards.add(custom_set_card)


    rarity_set = {}
    rarity_set.update({"data": first_datum})

    with open("public/json_files/custom_set_rarity/" + custom_set_name.replace(" ", "_").lower() + "_" + filename_rarity.lower() + ".json", "w") as outfile:
        json.dump(rarity_set, outfile)

#Alpha
#sets = ["@I'm sorry, @I can't do that (5122)",'Absolute Zero (5294)','Accelerated Synchronization (5289)','Adventurous Journey (5229)','Angelic Armies (5763)','Armies of the Sky and the Earth (5186)','Automated Sabotage (6020)','Autonomous Assembly (5275)','Beasts and Tamers (5529)','Beasts of the Mythical Forest (5718)','Birds of the Night (5405)','Bright Night (5017)','Burning Will (5639)','Carnivorous Cooperation (5523)','Celestial Forces (5762)','Chaos Enforcement (5774)','Chosen Signs (6201)','Clash of the Institutions (5127)','Clash of the Zefras (5007)','Cosmic Particles (6202)','Curtain Call (4999)','Cybernetic Support Force (6019)','Danger in the Inner Dephts (5650)','Danger in the Outer Dephts (5649)','Dangerous Excavation (5453)','Dangerous Variety (5336)','Deep Unity (5524)',"Destinie's Coin Flip (6214)","Devil's Bargain (5834)",'Digitalive (6160)','Dragon Riders (5528)',"Duelists' Kingdoms (6213)",'Dutybound Fighters (5553)','Elemental Force (5335)','Elements Combined (5399)','Eternal Rivals (6212)','Feral Planet (5562)','Ferocious Dance (5561)','Fiery Encore (4997)','Guardians of the Afterlife (5614)','Heroes Assemble! (5001)',"Heroes' Clash (5002)",'Heroic Clash (5187)','Icy Kingdoms (5293)','Infernal Banishment (5775)','Insects of the Mythical Forest (5717)','Jurassic Beasts Evolved (6181)',"Life's Gamble (6215)",'Living Minerals (5454)','Magical Summons (6216)',"Magistus' Origin (5125)",'Masters of Improvisation (5278)',"Mercenaries' Honor (5554)",'Mesmerizing Undead (5615)','Meteoric Explosions (6180)','Mindhacked Timeflow (6199)','Mindless Determinism (5276)','Miscellaneous Rituals (5201)','Mischievous Trappers (6191)','Molten Devastation (5640)','Mythic Constellation (5018)','Orbital Subjugation (6198)','Outlandish Tales (5257)','Pendulum Revolution (6217)','Plants of the Mythical Forest (5715)','Protagonists and Nemeses (5401)','Reign of the Underworld (5833)','Sect Gathering (5198)','Sparking Resistance (6085)','Storm of Battle (5290)','Storm of Darkness (5406)','Sudden Ambush (6188)','Tales and Legends - Climax (5752)','Tales and Legends - Epilogue (5753)','Tales and Legends - Prologue (5751)','The New Normal (5230)',"Tinkerer's Workshop (5277)",'Unfamiliar Threats (5258)','Utopic Creations (5084)','Words and Numbers (5077)','Wrath from the Heavens (6084)',"Zefras' Might (5008)"]

custom_sets = ['Fiery Encore (4997)','Curtain Call (4999)','Heroes Assemble! (5001)',"Heroes' Clash (5002)",'Clash of the Zefras (5007)',"Zefras' Might (5008)",'Bright Night (5017)','Mythic Constellation (5018)','Words and Numbers (5077)','Utopic Creations (5084)',"@I'm sorry, @I can't do that (5122)",'Digitalive (6160)',"Magistus' Origin (5125)",'Clash of the Institutions (5127)','Autonomous Assembly (5275)','Mindless Determinism (5276)','Armies of the Sky and the Earth (5186)','Heroic Clash (5187)','Sect Gathering (5198)','Miscellaneous Rituals (5201)','Adventurous Journey (5229)','The New Normal (5230)','Outlandish Tales (5257)','Unfamiliar Threats (5258)',"Tinkerer's Workshop (5277)",'Masters of Improvisation (5278)','Accelerated Synchronization (5289)','Storm of Battle (5290)','Icy Kingdoms (5293)','Absolute Zero (5294)','Elemental Force (5335)','Dangerous Variety (5336)','Elements Combined (5399)','Protagonists and Nemeses (5401)','Storm of Darkness (5406)','Birds of the Night (5405)','Dangerous Excavation (5453)','Living Minerals (5454)','Carnivorous Cooperation (5523)','Deep Unity (5524)','Dragon Riders (5528)','Beasts and Tamers (5529)','Dutybound Fighters (5553)',"Mercenaries' Honor (5554)",'Ferocious Dance (5561)','Feral Planet (5562)','Guardians of the Afterlife (5614)','Mesmerizing Undead (5615)','Burning Will (5639)','Molten Devastation (5640)','Danger in the Outer Depths (5649)','Danger in the Inner Dephts (5650)','Plants of the Mythical Forest (5715)','Insects of the Mythical Forest (5717)','Beasts of the Mythical Forest (5718)','Tales and Legends - Prologue (5751)','Tales and Legends - Climax (5752)','Tales and Legends - Epilogue (5753)','Celestial Forces (5762)','Angelic Armies (5763)','Chaos Enforcement (5774)','Infernal Banishment (5775)','Reign of the Underworld (5833)',"Devil's Bargain (5834)",'Cybernetic Support Force (6019)','Automated Sabotage (6020)','Meteoric Explosions (6180)','Jurassic Beasts Evolved (6181)','Wrath from the Heavens (6084)','Sparking Resistance (6085)','Sudden Ambush (6188)','Mischievous Trappers (6191)','Orbital Subjugation (6198)','Mindhacked Timeflow (6199)','Chosen Signs (6201)','Cosmic Particles (6202)','Eternal Rivals (6212)',"Duelists' Kingdoms (6213)","Destinie's Coin Flip (6214)","Life's Gamble (6215)",'Magical Summons (6216)','Pendulum Revolution (6217)']

rarities = {"Common", "Rare", "Super Rare", "Ultra Rare", "Secret Rare"}

for custom_set in custom_sets:
    for rarity in rarities:
        write_custom_set_rarity(custom_set, rarity)
        pass

with open("cardname_error.txt", "w") as outfile:
    for card in error_name_cards:
        outfile.write(card)
        outfile.write('\n')

# Makes empty folders by the name of the set
#for set in sets:
    #newpath = "public/custom_packs_texts/" + set.replace(" ", "_").lower()
    #if not os.path.exists(newpath):
        #os.makedirs(newpath)

#for set in sets:
    #path = "public/custom_packs_texts/" + set.replace(" ", "_").lower()
    #for rarity in rarities:
        #number = "00"
        #if rarity == "Common":
            #number = "01"
        #if rarity == "Rare":
            #number = "02"
        #if rarity == "Super Rare":
            #number = "03"
        #if rarity == "Ultra Rare":
            #number = "04"
        #if rarity == "Secret Rare":
            #number = "05"
        #with open(os.path.join(path, number + rarity.lower()[0:2] + ".txt"), 'w') as fp:
            #pass