import os
import openai
import string


def main(title: string):

    openai.api_key = os.getenv("OPENAI_API_KEY")
    content = openai.Completion.create(
        model="text-davinci-003",
        prompt="Create a seo optimized article with minimum 1500 characters about " + title + "",
        max_tokens=4000,
        temperature=0.8
    )
    return content.choices[0].text
