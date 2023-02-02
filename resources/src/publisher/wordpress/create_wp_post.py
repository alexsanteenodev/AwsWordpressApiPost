

import requests
import os
from slugify import slugify
import string
from src.publisher.wordpress.get_wp_post_by_slug import get_wp_post_by_slug
from src.publisher.openai.generate_post_content_by_title import generate_post_content_by_title


def create_wp_post(title: string):
    # Set the endpoint URL for the WordPress site
    endpoint_url = os.environ['ENDPOINT_URL']
    # Set the basic auth credentials
    auth = (os.environ['AUTH_USERNAME'], os.environ['AUTH_PASSWORD'])

    slug = slugify(title)
    post_exist_response = get_wp_post_by_slug(slug)

    if (post_exist_response.status_code == 200):
        post_exist_response_data = post_exist_response.json()

        if post_exist_response_data:
            print("Post already exist")
            return post_exist_response.status_code

    print("Generating post content...")

    content = generate_post_content_by_title(title)
    if (not content):
        return 500
    # Set the data for the new post
    data = {
        "title": title,
        "content": content,
        'slug': slug,
        "status": "publish"
    }

    # Make the request to create the post
    response = requests.post(endpoint_url, auth=auth, json=data)

    # Return the response
    return response.status_code
