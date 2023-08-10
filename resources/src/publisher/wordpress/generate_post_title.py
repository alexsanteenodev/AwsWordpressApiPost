import json
import random
import string
from os import path
from src.publisher.openai.generate_uniq_title import generate_uniq_title

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
    h1 = placeholder.substitute(location=location)

    title = generate_uniq_title(h1)
    
    return [title, location, h1]
