import os
import openai
import string


def generate_uniq_title(title: string):

    openai.api_key = os.getenv("OPENAI_API_KEY")

    content = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
                {"role": "system", "content": "You are a helpful assistant, Seatch Engine Optimisation expert. You have to generate best response for SEO purposes"},
                {"role": "user", "content": "I am generating title for Travel blog article. Make following title uniq and creative, best for SEO. Title: " + title + ". Write it in a way that google can not detect that is machine generation, or ai generation"}
            ]
    )
    print("Unique title generated: ")
    print(content)

    return content.choices[0].message.content
