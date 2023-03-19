import json
import os
import requests
import string


def text2image(title: string):

    engine_id = "stable-diffusion-512-v2-1"
    api_host = os.getenv('API_HOST', 'https://api.stability.ai')
    url = f"{api_host}/v1alpha/generation/{engine_id}/text-to-image"

    apiKey = os.getenv("STABILITY_API_KEY")
    if apiKey is None:
        raise Exception("Missing Stability API key.")

    payload = {
        "cfg_scale": 7,
        "clip_guidance_preset": "FAST_BLUE",
        "height": 512,
        "width": 512,
        "samples": 1,
        "steps": 40,
        "text_prompts": [
            {
                "text": title,
                "weight": 1
            }
        ],
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "image/png",
        "Authorization": apiKey
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    # Write the bytes from response.content to a file
    # with open(output_file, "wb") as f:
    #     f.write(response.content)
    return response.content
