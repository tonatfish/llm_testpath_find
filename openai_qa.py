import base64
from openai import OpenAI

# client of OpenAI
client = OpenAI(api_key="")

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def check_picture_result(description: str, image_path: str):
    message = f"We want to assert the ui provided as image. The image should contain: {description}. Provide us only a similarity_score between 0 to 1. Please only output a floating-point number between 0 and 1 (for example: 0.53)."
    base64_image = encode_image(image_path)
    messages = [
        {"role": "system", "content": "You are an UI analysis assistant."},
        {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": message,
                },
                {
                "type": "image_url",
                "image_url": {
                    "url":  f"data:image/jpeg;base64,{base64_image}"
                },
                },
            ],
        }
    ]
    score = 0
    try:
        score = float(get_llm_answer(messages))
    except ValueError:
        print("Not a float")
    
    print(score)
    return score

def get_llm_answer(messages):
    completion = client.chat.completions.create(
        model = "gpt-4o",
        messages = messages
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    check_picture_result("version tag 1.4.2f", "about_language1.png")
