import os
import openai
import string


def generate_post_content_by_title(title: string):

    openai.api_key = os.getenv("OPENAI_API_KEY")

    content = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
                {"role": "system", "content": "You are a helpful assistant, Seatch Engine Optimisation expert. You have to generate best response for SEO purposes"},
                {"role": "user", "content": "Create a seo optimized article with minimum 3000 characters about " + title + ". Write it in a way that google can not detect that is machine generation, or ai generation"}
            ]
    )
    print("Unique title generated: " + content)

    return content.choices[0].message.content
