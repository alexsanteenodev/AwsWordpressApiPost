

import requests
import os
from slugify import slugify
import string
from src.publisher.wordpress.get_wp_post_by_slug import get_wp_post_by_slug
from src.publisher.openai.generate_post_content_by_title import generate_post_content_by_title
from src.publisher.stablediffusion.text2image import text2image
from src.publisher.openai.generate_meta_description_by_title import generate_meta_description_by_title

def create_wp_post(title: string, location: string, h1: string):
    # Set the endpoint URL for the WordPress site
    endpoint_url = os.environ['ENDPOINT_URL']
    # Set the basic auth credentials
    auth = (os.environ['AUTH_USERNAME'], os.environ['AUTH_PASSWORD'])

    slug = slugify(title)
    print("slug: ", slug)
    post_exist_response = get_wp_post_by_slug(slug)

    if (post_exist_response.status_code == 200):
        post_exist_response_data = post_exist_response.json()

        if post_exist_response_data:
            print("Post already exist")
            return post_exist_response.status_code

    print("Generating post content...")

    content = generate_post_content_by_title(title)
    meta_desciption= generate_meta_description_by_title(title)

    if (not content):
        return 500
    else:
        print("Post content generated successfully")

    print("Generating image...")

    image_data = text2image(location)

    # Send a GET request to retrieve the image data from another HTTP request

    print("Image generated")

    print("Uploading image...")
    response = requests.post(endpoint_url + '/media',
                             headers={
                                 "Content-Type": "image/png",
                                 "Content-Disposition": "attachment; filename="+location+".png"
                             },
                             auth=auth,
                             data=image_data)
    if response.status_code != 201:
        print('Error uploading image:', response.content)
    else:
        media_id = response.json().get('id')

    print("Image uploaded media_id: ", media_id)

    # Set the data for the new post
    data = {
        "title": h1,
        "content": content,
        'slug': slug,
        "status": "publish",
        'featured_media': media_id,
        # Replace 1 with the ID of the category you want to assign to the post
        "categories": [4],
        "meta": {
            "description": meta_desciption,
            "_yoast_wpseo_metadesc": meta_desciption
        },
        "yoast_meta": {
            "yoast_wpseo_title": title,
            "yoast_wpseo_metadesc": meta_desciption,
        }
    }

    print("Creating in WP...")
    # Make the request to create the post
    response = requests.post(endpoint_url+"/posts", auth=auth, json=data)

    # Return the response
    return response