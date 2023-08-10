import os
import openai
import string


def generate_meta_description_by_title(title: string):

    openai.api_key = os.getenv("OPENAI_API_KEY")

    content = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
                {"role": "system", "content": "You are a helpful assistant, Seatch Engine Optimisation expert. You have to generate best response for SEO purposes"},
                {"role": "user", "content": "I am generating meta description for Travel blog article. Generate meta description by following title, which will be best for SEO purposes. Title: " + title + ". Respond only with meta description without any comments"}
            ]
    )
    print("Unique meta generated: "+content.choices[0].message.content)
    print(content)

    return content.choices[0].message.content
