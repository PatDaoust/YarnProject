# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 11:00:56 2021

@author: catal
"""

import requests
from requests.adapters import HTTPAdapter
from browser import document, prompt, html, alert
from browser.local_storage import storage


def getPatternID(pattern_url):
    """asssumes pattern_url is a string, representing the URL of a ravelry pattern
    e.g.https://www.ravelry.com/patterns/library/velvet-cache-cou
    returns an int, the pattern ID
    """
    permalink = pattern_url[41:]
    with requests.Session() as a_session:
        auth_name = "read-046277a3027f680ebe3fa030e755eb34"
        auth_pass = "O+mL0KzfjgQ1eLA7K8FO9s28QPvr6QuiL+pOvFHZ"
        a_session.auth = (auth_name, auth_pass)
        ravelry_adapter = HTTPAdapter(max_retries=3)
        a_session.mount('https://ravelry.com', ravelry_adapter)
        base_request = "https://api.ravelry.com/patterns/search.json?query="
        pattern = a_session.get(base_request+permalink)
        if pattern.status_code != 200:
            raise RuntimeError("Ravelry not responding as expected.\
                               Please check your internet connection or try again later")
        pattern_id = pattern.json()['patterns'][0]['id']
    return pattern_id


# print(getPatternID("https://www.ravelry.com/patterns/library/velvet-cache-cou"))


def getPattern(pattern_id):
    """assumes pattern_id is an int, representing a pattern id on ravelry
    returns a dict, representing the json pattern object
    see https://www.ravelry.com/api for pattern object description
    """
    with requests.Session() as a_session:
        auth_name = "read-046277a3027f680ebe3fa030e755eb34"
        auth_pass = "O+mL0KzfjgQ1eLA7K8FO9s28QPvr6QuiL+pOvFHZ"
        a_session.auth = (auth_name, auth_pass)
        ravelry_adapter = HTTPAdapter(max_retries=3)
        a_session.mount('https://ravelry.com', ravelry_adapter)
        base_request = "https://api.ravelry.com/patterns.json?ids="
        pattern = a_session.get(base_request+str(pattern_id))
        if pattern.status_code != 200:
            raise RuntimeError("Ravelry not responding as expected.\
                               Please check your internet connection or try again later")
    return pattern


# pattern_cache_cou = getPattern(972499).json()
# print(pattern_cache_cou['patterns']['972499']['packs'][0])
# yarn_id = pattern_cache_cou['patterns']['972499']['packs'][0]['yarn']['id']
# print(yarn_id)


def getRecommendedYarnID(pattern_id):
    """assumes pattern_id is an int, representing a pattern id on ravelry
    returns an int, repressenting the yarn ID of the yarn recommended for the pattern
    see https://www.ravelry.com/api for pattern object description
    """
    pattern = getPattern(pattern_id)
    if pattern.status_code != 200:
        raise RuntimeError("Ravelry not responding as expected.\
                           Please check your internet connection or try again later")
    try:
        return pattern.json()['patterns'][str(pattern_id)]['packs'][0]['yarn']['id']
    except (IndexError, TypeError):
        raise RuntimeError("The pattern writer has not suggested any yarns for this\
                           pattern. Unfortunately we cannot recommend any yarns")


# print(getRecommendedYarnID(972499))

def prettyPrintDictionary(a_dict):
    """assumes a_dict is a dictionary
    prints out the dictionary one key per line"""
    for key, value in a_dict.items():
        print(key, ' : ', value)


def getRecommendedYarn(yarn_id):
    """assumes pattern_id is an int, representing a yarn id on ravelry
    returns a dict, representing the json yarn object
    see https://www.ravelry.com/api for yarn object description
    """
    with requests.Session() as a_session:
        auth_name = "read-046277a3027f680ebe3fa030e755eb34"
        auth_pass = "O+mL0KzfjgQ1eLA7K8FO9s28QPvr6QuiL+pOvFHZ"
        a_session.auth = (auth_name, auth_pass)
        ravelry_adapter = HTTPAdapter(max_retries=3)
        a_session.mount('https://ravelry.com', ravelry_adapter)
        base_request = "https://api.ravelry.com/yarns.json?ids="
        yarn = a_session.get(base_request+str(yarn_id))
        if yarn.status_code != 200:
            raise RuntimeError("Ravelry not responding as expected.\
                               Please check your internet connection or try again later")
    return yarn


# print(getRecommendedYarn(181030).json())


def getYarn(yarn_URL):
    """asssumes yarn_URL is a string, representing a ravelry URL of a yarn
    e.g. https://www.ravelry.com/yarns/library/fyberspates-scrumptious-lace
    returns returns a dict, representing the json yarn object
    see https://www.ravelry.com/api for yarn object description
    """
    with requests.Session() as a_session:
        auth_name = "read-046277a3027f680ebe3fa030e755eb34"
        auth_pass = "O+mL0KzfjgQ1eLA7K8FO9s28QPvr6QuiL+pOvFHZ"
        a_session.auth = (auth_name, auth_pass)
        ravelry_adapter = HTTPAdapter(max_retries=3)
        a_session.mount('https://ravelry.com', ravelry_adapter)
        permalink = yarn_URL[38:]
        base_request = "https://api.ravelry.com//yarns/" + permalink + ".json"
        yarn = a_session.get(base_request)
        if yarn.status_code != 200:
            raise RuntimeError("Ravelry not responding as expected.\
                               Please check your internet connection or try again later")
    return yarn


# print(getYarn('https://www.ravelry.com/yarns/library/fyberspates-scrumptious-lace'))


def yarnSearch(weight, attributes):
    """assumes weight is a string, describing a weight of yarn
    assumes attributes is a list of strings, each describing qualities of yarn
    returns a list of yarn objects that match the given weight and attributes
    """
    # pdb.set_trace()
    with requests.Session() as a_session:
        auth_name = "read-046277a3027f680ebe3fa030e755eb34"
        auth_pass = "O+mL0KzfjgQ1eLA7K8FO9s28QPvr6QuiL+pOvFHZ"
        a_session.auth = (auth_name, auth_pass)
        ravelry_adapter = HTTPAdapter(max_retries=3)
        a_session.mount('https://ravelry.com', ravelry_adapter)
        base_request = "https://api.ravelry.com/yarns/search.json?"
        attributes_query = ''
        for attribute in attributes:
            attributes_query += '&ya=' + attribute
        yarns = a_session.get(base_request + "weight=" + weight + attributes_query)
        if yarns.status_code != 200:
            raise RuntimeError("Ravelry not responding as expected.\
                               Response status code is " + str(yarns.status_code))
    return yarns.json()['yarns']


# print(yarnSearch('dk', ['gradient', 'halo']))
# print(yarnSearch('lace', ['halo']))
# print(yarnSearch('worsted', ['crepe']))


def suggestYarn(pattern_url):
    """assumes asssumes pattern_url is a string, representing the URL of a ravelry pattern
    returns a list of 2-tuples, of dicts and ints,
    each dict representing a yarn that could be used to make the pattern,
    each int representing how mant skeins of that yarn would be needed to make the pattern
    """
    # analyze yarn recommended by pattern
    pattern_id = getPatternID(pattern_url)
    pattern = getPattern(pattern_id)
    yarn_id = getRecommendedYarnID(pattern_id)
    pattern_yarn = getRecommendedYarn(yarn_id)
    pattern_yarn_attributes =\
        pattern_yarn.json()['yarns'][str(yarn_id)]['yarn_attributes']
    # pattern_yarn_texture = pattern_yarn.json()['yarns'][str(yarn_id)]['texture']
    pattern_yarn_yarn_weight_name =\
        pattern_yarn.json()['yarns'][str(yarn_id)]['yarn_weight']['name']
    # put attributes into list
    attributes = []
    if pattern_yarn_attributes:
        useless_attributes = ["care", "dye", "ply", "sustanaibility"]
        for attribute in pattern_yarn_attributes:
            if attribute["yarn_attribute_group"]["permalink"] not in useless_attributes:
                attributes += [attribute["permalink"]]
    # get yarn recommendations
    # TODO figure out if/how all attributes come up in pattern
    yarns = yarnSearch(pattern_yarn_yarn_weight_name, attributes)
    # calculate how many skeins of each possible yarn are needed
    project_yardage = pattern.json()['patterns'][str(pattern_id)]['yardage']
    yarns_and_amounts = []
    for i in range(len(yarns)):
        yardage_per_skein = yarns[i]['yardage']
        if project_yardage and yardage_per_skein:
            skeins_new_yarn = -(-project_yardage // yardage_per_skein)  # ceiling division
            skein_string = "Skeins needed for your project: " + str(skeins_new_yarn)
            yarns_and_amounts.append((yarns[i], skein_string))
    return yarns_and_amounts


def getYarnAttributes():
    """returns a dict of all the possible yarn attributes, grouped"""
    with requests.Session() as a_session:
        auth_name = "read-046277a3027f680ebe3fa030e755eb34"
        auth_pass = "O+mL0KzfjgQ1eLA7K8FO9s28QPvr6QuiL+pOvFHZ"
        a_session.auth = (auth_name, auth_pass)
        ravelry_adapter = HTTPAdapter(max_retries=3)
        a_session.mount('https://ravelry.com', ravelry_adapter)
        base_request = "https://api.ravelry.com/yarn_attributes/groups.json"
        yarns_attributes = a_session.get(base_request)
        attributes = yarns_attributes.json()['yarn_attribute_groups']
        for x in attributes:
            print(x)


def prettyPrintYarn(yarn):
    """assumes yarn_object is a dict from ravelry's API
    prints a yarn object in a human readable way
    """
    print("Yarn name: " + yarn[0]["name"])
    print("Manufacturer: " + yarn[0]["yarn_company_name"])
    print("Yarn weight: " + str(yarn[0]["yarn_weight"]["name"]))
    print("Yarn texture: " + yarn[0]["texture"])
    print("Is yarn machine washable?: " + str(yarn[0]["machine_washable"]))
    print(yarn[1])
    print("Is yarn discontinued?: " + str(yarn[0]["discontinued"]))
    print("Average rating: " + str(yarn[0]["rating_average"]))
    print("Ratings count: " + str(yarn[0]["rating_count"]))
    print("Link: " + "https://www.ravelry.com/yarns/library/" + yarn[0]["permalink"])


def displayYarn(yarn):
    """assumes yarn_object is a dict from ravelry's API
    displays a yarn object on a webpage"""
    # TODO


if __name__ == "__main__":
    print("Here are some yarns that I recommend for your project:")
    print("----------------------------------")
    for yarn in suggestYarn("https://www.ravelry.com/patterns/library/velvet-cache-cou"):
        prettyPrintYarn(yarn)
        print("----------------------------------")


yarn_attributes_valid = ['dry-flat', 'hand-wash', 'hand-wash-cold','machine-dry', 'machine-wash', 'superwash', 'barber-pole', 'gradient', 'heathered', 'marled', 'multi-strand-unplied', 'self-patterning', 'self-striping', 'semi-solid', 'solid', 'speckled', 'tonal', 'tweed', 'variegated', 'chain-plied', 'chainette-i-cord', 'coils', 'halo', 'ribbon', 'ruffle', 'slub', 'tape', 'thick-and-thin', 'unspun', 'z-twist', 'beads', 'feathers', 'felt', 'other', 'ribbons', 'sequins', 'boucle', 'chenille', 'eyelash', 'flamme', 'ladder', 'mesh', 'pom-pom', 'sueded', 'single-ply', '2-ply', '3-ply', '4-ply', 'cabled', 'multi-ply-5', 'core-spun', 'semi-woolen-spun', 'semi-worsted-spun', 'woolen-spun', 'worsted-spun', 'fleece-dyed', 'hand-dyed', 'machine-dyed', 'natural-dyes', 'undyed', 'mini-skeins', 'winding-required', 'certified-organic', 'fair-trade', 'recycled', 'conductive', 'mercerized', 'moth-proofed']


# TODO optional: allow user to filter resuts

# TODO:
# write equivalent to display_map
# write equivalent to submit: document["submit"].bind("click", base64_compute)
# write equivalent to clear: document["clear-btn"].bind("click", clear_map)
