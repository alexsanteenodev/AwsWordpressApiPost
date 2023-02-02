import requests
import os
import string


def main(slug: string):
    # Set the endpoint URL for the WordPress site
    endpoint_url = os.environ['ENDPOINT_URL'] + \
        '?slug='+slug
    # Set the basic auth credentials
    auth = (os.environ['AUTH_USERNAME'], os.environ['AUTH_PASSWORD'])

    # Make the request to create the post
    response = requests.get(endpoint_url, auth=auth)

    # Return the response
    return response
