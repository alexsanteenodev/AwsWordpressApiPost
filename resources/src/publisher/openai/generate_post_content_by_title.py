import os
import openai
import string


def generate_post_content_by_title(title: string):

    openai.api_key = os.getenv("OPENAI_API_KEY")

    content = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
                {"role": "system", "content": "You are a helpful assistant, Seatch Engine Optimisation expert. You have to generate best response for SEO purposes"},
                {"role": "user", "content": "Create a search-optimised article for a travel blog with approximately 2,000 to 3,000 characters based on the existing title: "+title+". Use keywords and other technics which SEO expert would do to write this article. Write it in a way that google can not detect that is machine generation or ai generation. Respond only with the article, without comments."}
            ]
    )

    return content.choices[0].message.content
