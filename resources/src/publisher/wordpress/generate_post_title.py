import json
import random
import string
from os import path

basepath = path.dirname(__file__)


def generate_post_title():
    # Opening JSON file
    filepath = path.abspath(
        path.join(basepath, "..", "..", "config/placeholders.json"))
    f = open(filepath)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    placeholder = string.Template(random.choice(data['placeholders']))
    location = random.choice(data['locations'])
    title = placeholder.substitute(location=location)
    return title
