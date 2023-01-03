import requests
import os


def create_wp_post(title, content):
    # Set the endpoint URL for the WordPress site
    endpoint_url = os.environ['ENDPOINT_URL']

    # Set the basic auth credentials
    auth = (os.environ['AUTH_USERNAME'], os.environ['AUTH_PASSWORD'])

    # Set the data for the new post
    data = {
        "title": title,
        "content": content,
        "status": "draft"
    }

    # Make the request to create the post
    response = requests.post(endpoint_url, auth=auth, json=data)

    # Return the response
    return response


def lambda_handler(event, context):
    # Call the function to create the post
    response = create_wp_post(
        "My New Post", "This is the content for my new post from lambda.")

    # Print the response status code
    print(response.status_code)
    print(response.content)
