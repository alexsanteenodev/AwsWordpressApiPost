from src.publisher.wordpress.create_wp_post import create_wp_post
from src.publisher.wordpress.generate_post_title import generate_post_title


def generate_publish_post():
    title, location, h1 = generate_post_title()

    print(f"Title: {title}")
    print(f"Location: {location}")
    print(f"H1: {h1}")
    # Generate a post content using OpenAI
    if (not title):
        return

    print("Generating post content for: " + title)
    # Call the function to create the post
    response = create_wp_post(title, location, h1)

    # Print the response status code
    if (response and response.status_code == 201):
        print("Post created successfully. Status code:", response.status_code)
    else:
        print("Failed to create post! Status code: ", response.content)
        raise Exception("Post create failed!!!")
