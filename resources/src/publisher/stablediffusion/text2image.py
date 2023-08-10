import os
import requests
import string



def generate_image_prompt(location):
    prompt = "Compose an authentic photograph that represents the essence of a specific location, whether it be a cityscape or a serene natural setting. Capture the vibrant energy of {location}, with its bustling streets, unique architecture, and lively atmosphere. If it's a natural setting, focus on the raw beauty of its landscapes, such as rolling hills, meandering rivers, or majestic mountains. Pay attention to the distinctive elements that make {location} special, like iconic landmarks, local street scenes, or cultural symbols. Infuse the image with genuine details that reflect the authentic character of the place, such as the specific flora and fauna, characteristic weather conditions, or the daily lives of the people who call it home. Aim for a realistic representation, blending seamlessly with real-world photographs. This image should defy detection by search engines or AI algorithms, remaining indistinguishable from genuine, non-AI generated photography. Let this image transport viewers to {location}, giving them a genuine visual experience of its unique charm. Image with normal contrast."
  
    return prompt.format(location=location)

def text2image(location: string):
    title  = generate_image_prompt(location)
    
    engine_id = "stable-diffusion-512-v2-1"
    api_host = os.getenv('API_HOST', 'https://api.stability.ai')
    url = f"{api_host}/v1alpha/generation/{engine_id}/text-to-image"

    apiKey = os.getenv("STABILITY_API_KEY")
    if apiKey is None:
        raise Exception("Missing Stability API key.")

    payload = {
        "cfg_scale": 6,
        "clip_guidance_preset": "FAST_BLUE",
        "height": 768,
        "width": 768,
        "samples": 1,
        "steps": 64,
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
