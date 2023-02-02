import src.publisher.wordpress.create_wp_post as create_wp_post
import src.publisher.wordpress.generate_post_title as generate_post_title


def main():
    title = generate_post_title()
    # Generate a post content using OpenAI
    if (not title):
        return

    print("Generating post content for: " + title)
    # Call the function to create the post
    response_status = create_wp_post(
        title)

    # Print the response status code
    if (response_status == 201):
        print("Post created successfully, the response is given below")
    else:
        print("Failed to create post, the response is given below")
