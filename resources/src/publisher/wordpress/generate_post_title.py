import json
import random
import string


def generate_post_title():
    # Opening JSON file
    f = open('../../config/placeholders.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    placeholder = string.Template(random.choice(data['placeholders']))
    location = random.choice(data['locations'])
    title = placeholder.substitute(location=location)
    return title
