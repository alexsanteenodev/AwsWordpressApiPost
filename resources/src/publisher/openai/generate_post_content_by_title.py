import os
import openai
import string


def generate_post_content_by_title(title: string):

    openai.api_key = os.getenv("OPENAI_API_KEY")

    content = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Create a seo optimized article with minimum 1500 characters about " + title + ""}
            ]
    )


    print(content)
    return content.choices[0].message.content
