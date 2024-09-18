import ollama

MODEL_LIST = ["gemma2", "llava", "llava-llama3", "llava-phi3", "phi3"]
MODEL = MODEL_LIST[3]

def get_process_answer(description: str, image_path: str): # -> tuple[str, object]:
    message = f"Provided Image is an UI image. To test this ui, we need to perform the action that {description}. What action shall we do? (output template: {{ \"action\": [click / double-click / long press / scroll], \"position\": [x, y] }})"
    messages = [{
        'role': 'user',
        'content': message,
        'images': [image_path]
    }]
    ans = get_llm_answer(messages)
    print(ans)


def get_llm_answer(messages):
    response = ollama.chat(
        model = MODEL,
        messages = messages
    )
    return response["message"]["content"]

if __name__ == "__main__":
    import time
    test_msgs = [
        {
            'role': 'user',
            'content': 'please describe image with 5 adjective + noun in a list, for instance: ["beautiful girl", "cute woman", "red car", "crazy man", "blue sky"]',
            'images': ['./xx.jpg']
        }
    ]
    start = time.time()
    get_llm_answer(test_msgs)
    end = time.time()
    print(end - start)