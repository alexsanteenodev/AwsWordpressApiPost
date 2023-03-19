

import requests
import os
from slugify import slugify
import string
from src.publisher.wordpress.get_wp_post_by_slug import get_wp_post_by_slug
from src.publisher.openai.generate_post_content_by_title import generate_post_content_by_title
from src.publisher.stablediffusion.text2image import text2image


def create_wp_post(title: string, location: string):
    # Set the endpoint URL for the WordPress site
    endpoint_url = os.environ['ENDPOINT_URL']
    # Set the basic auth credentials
    auth = (os.environ['AUTH_USERNAME'], os.environ['AUTH_PASSWORD'])

    print("auth: ", auth)

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
    if (not content):
        return 500
    else:
        print("Post content generated successfully")

    print("Generating image...")

    image_promt = "Generate featured photo for post with title " + \
        title+" , high quality, real"
    image_data = text2image(image_promt)

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
        "title": title,
        "content": content,
        'slug': slug,
        "status": "publish",
        'featured_media': media_id,
        # Replace 1 with the ID of the category you want to assign to the post
        "categories": [4]
    }

    print("Creating in WP...")
    # Make the request to create the post
    response = requests.post(endpoint_url+"/posts", auth=auth, json=data)

    # Return the response
    return response
